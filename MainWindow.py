# -*- coding: utf-8 -*-

"""
Module implementing music.

Qt在线帮助文档
https://doc.qt.io/qt-5/qtserialport-examples.html
"""

from PyQt5.QtCore import pyqtSlot, QThread, pyqtSignal
from PyQt5.QtGui import QTextCursor, QKeyEvent
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QFontDialog, QFileDialog

from Ui_MainWindow import Ui_music

from keymap import *
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
import re
from datetime import datetime
import time
import pygame
import traceback


class Music(QMainWindow, Ui_music):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Music, self).__init__(parent)
        self.setupUi(self)
        self.init_music()
        self.init_ui_states()

    def init_ui_states(self):
        self.radioButton_notes.setChecked(True)
        self.horizontalSlider_speed.setMinimum(1)
        self.horizontalSlider_speed.setMaximum(30)
        self.horizontalSlider_speed.setSingleStep(1)
        self.horizontalSlider_speed.setTickInterval(1)
        self.horizontalSlider_speed.setTickPosition(self.horizontalSlider_speed.TicksAbove)
        self.horizontalSlider_speed.setValue(15)
        self.lcdNumber_speed.display(15)
        self.comboBox_baud_rate.addItems([str(i) for i in QSerialPortInfo.standardBaudRates()])
        self.comboBox_baud_rate.setCurrentText("115200")
        self.comboBox_baud_rate.setEditable(False)
        self.comboBox_stop_bit.addItems(["1", "1.5", "2"])
        self.comboBox_data_bit.addItems(["8", "7", "6", "5"])
        self.comboBox_check_bit.addItems(["None", "Odd", "Even"])
        self.pushButton_on_off.setCheckable(True)
        self.checkBox_send16.setChecked(False)
        self.checkBox_receive16.setChecked(False)
        self.checkBox_time_r.setChecked(False)
        self.checkBox_time_s.setChecked(False)
        self.textEdit_receive.setReadOnly(True)
        self.textEdit_send.setAcceptRichText(False)

    def init_music(self):
        self.serialPort = QSerialPort()
        # self.serialPort.setReadBufferSize(200 * 1024)
        self.serialPort.readyRead.connect(self.serialPort_readyRead)
        self.serialPort.errorOccurred.connect(self.serialPort_errorOccurred)

        self.to_be_set = False
        self.timestamp_r = False
        self.timestamp_s = False
        self.port_opened = False  # 加速运行
        self.sent = 0
        self.received = 0
        self.key_fre = set()
        self.statusbar_showMessage()

        self.thread_key = KeyboardThread()
        self.thread_key.sigOut.connect(self.keyboard_piano)
        self.thread_key.start()

    def statusbar_showMessage(self):
        self.statusbar.showMessage("S:{0:<20}    R:{1}".format(self.sent, self.received))

    def serialPort_write(self, byte):
        if self.timestamp_s:
            if self.checkBox_receive16.isChecked():
                self.textEdit_receive.append(bytes('\n\n[%s]TX\n' % datetime.now(), encoding='gbk').hex() + byte.hex())
            else:
                self.textEdit_receive.append('\n\n[%s]TX\n' % datetime.now() + byte.decode(encoding='gbk'))

        self.serialPort.write(byte)
        self.sent += len(byte)
        self.statusbar_showMessage()

    def keyboard_piano(self, key_str):
        if self.port_opened:
            self.serialPort_write(
                (','.join(filter(None, [keygame.get(i, '') for i in re.findall(r'\d+', key_str)])) + '.\r\n')
                    .encode(encoding='gbk'))

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '询问', '确定退出吗？',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            if self.serialPort.isOpen():
                self.serialPort.close()
            event.accept()
        else:
            event.ignore()

    def serialPort_errorOccurred(self, Error):
        if Error > 0:
            if self.pushButton_on_off.isChecked():
                self.pushButton_on_off.click()
            QMessageBox.warning(self, "串口错误", str(serialPortError.get(Error, ("SpecialError：特殊错误"))))

    def serialPort_readyRead(self):
        """
        串口读
        """
        new_b = bytes(self.serialPort.readAll())

        if self.checkBox_receive16.isChecked():
            if self.timestamp_r:
                self.textEdit_receive.append(bytes('\n\n[%s]RX\n' % datetime.now(), encoding='gbk').hex())
            self.textEdit_receive.append(new_b.hex())
        else:
            if self.timestamp_r:
                self.textEdit_receive.append('\n\n[%s]RX\n' % datetime.now())
            self.textEdit_receive.append(new_b.decode(encoding='gbk', errors='replace'))
        self.textEdit_receive.moveCursor(QTextCursor.End)
        self.received += len(new_b)
        self.statusbar_showMessage()

        if self.to_be_set:
            sch = re.search(r'\{speed:(\d+)piano:(\d+)}', new_b.decode(encoding='gbk', errors='replace'))
            if sch:
                a, b = sch.groups()
                self.horizontalSlider_speed.setValue(int(a))
                if bool(int(b)):
                    self.radioButton_notes.setChecked(True)
                else:
                    self.radioButton_piano.setChecked(True)
                self.to_be_set = False

    @pyqtSlot(bool)
    def on_radioButton_notes_toggled(self, checked):
        """
        Slot documentation goes here.

        @param checked 播放模式
        @type bool
        """
        self.label_speed.setEnabled(checked)
        self.horizontalSlider_speed.setEnabled(checked)

    @pyqtSlot(int)
    def on_horizontalSlider_speed_valueChanged(self, value):
        """
        Slot documentation goes here.

        @param value 速度调节
        @type int
        """
        self.lcdNumber_speed.display(value)
        if self.serialPort.isOpen():
            self.serialPort_write(('1,%d\r\n' % value).encode(encoding='gbk'))

    @pyqtSlot(bool)
    def on_radioButton_piano_toggled(self, checked):
        """
        Slot documentation goes here.

        @param checked 弹奏模式
        @type bool
        """
        if self.serialPort.isOpen():
            self.serialPort_write(('2,%d\r\n' % (not checked)).encode(encoding='gbk'))

    @pyqtSlot()
    def on_pushButton_search_port_clicked(self):
        """
        Slot documentation goes here.

        串口搜索
        """
        self.comboBox_serial_port.clear()
        for i in QSerialPortInfo.availablePorts():
            self.comboBox_serial_port.addItem(i.portName() + ":" + i.description())

    @pyqtSlot(str)
    def on_comboBox_serial_port_currentTextChanged(self, p0):
        """
        Slot documentation goes here.

        @param p0 串口号
        @type str
        """
        print("串口号", p0)
        self.serialPort.setPortName(p0.split(":")[0])

    @pyqtSlot(str)
    def on_comboBox_baud_rate_currentTextChanged(self, p0):
        """
        Slot documentation goes here.

        @param p0 波特率
        @type str
        """
        self.serialPort.setBaudRate(int(p0))

    @pyqtSlot(str)
    def on_comboBox_stop_bit_currentTextChanged(self, p0):
        """
        Slot documentation goes here.

        @param p0 停止位
        @type str
        """
        self.serialPort.setStopBits(stopBits.get(p0, 1))

    @pyqtSlot(str)
    def on_comboBox_data_bit_currentTextChanged(self, p0):
        """
        Slot documentation goes here.

        @param p0 数据位
        @type str
        """
        self.serialPort.setDataBits(int(p0))

    @pyqtSlot(str)
    def on_comboBox_check_bit_currentTextChanged(self, p0):
        """
        Slot documentation goes here.

        @param p0 校验位
        @type str
        """
        self.serialPort.setParity(parity.get(p0, 0))

    @pyqtSlot(bool)
    def on_pushButton_on_off_clicked(self, checked):
        """
        Slot documentation goes here.

        @param checked 打开关闭串口
        @type bool
        """
        if checked:
            if self.serialPort.open(QSerialPort.ReadWrite):
                self.pushButton_search_port.setEnabled(False)
                self.comboBox_serial_port.setEnabled(False)
                self.comboBox_baud_rate.setEnabled(False)
                self.comboBox_stop_bit.setEnabled(False)
                self.comboBox_data_bit.setEnabled(False)
                self.comboBox_check_bit.setEnabled(False)
                self.pushButton_send.setEnabled(True)
                self.pushButton_stop.setEnabled(True)
                self.pushButton_on_off.setText("关闭串口")
                self.to_be_set = True
                self.port_opened = True
                self.serialPort_write(('9,9\r\n').encode(encoding='gbk'))
            else:
                self.pushButton_on_off.setChecked(False)
        else:
            self.serialPort.close()
            self.port_opened = False
            self.pushButton_search_port.setEnabled(True)
            self.comboBox_serial_port.setEnabled(True)
            self.comboBox_baud_rate.setEnabled(True)
            self.comboBox_stop_bit.setEnabled(True)
            self.comboBox_data_bit.setEnabled(True)
            self.comboBox_check_bit.setEnabled(True)
            self.pushButton_send.setEnabled(False)
            self.pushButton_stop.setEnabled(False)
            self.pushButton_on_off.setText("打开串口")

    @pyqtSlot()
    def on_pushButton_send_clicked(self):
        """
        Slot documentation goes here.

        发送
        """
        send_str = self.textEdit_send.toPlainText()
        if self.checkBox_send16.isChecked():
            if self.hex_check(send_str):
                self.serialPort_write(bytes.fromhex(send_str.replace(' ', '') + '0d0a'))
        else:
            self.serialPort_write((send_str + '\r\n').encode(encoding='gbk', errors='replace'))

    @pyqtSlot()
    def on_pushButton_stop_clicked(self):
        """
        Slot documentation goes here.

        停止播放音符
        """
        self.serialPort_write(('0\r\n').encode(encoding='gbk'))

    @pyqtSlot()
    def on_pushButton_send_clear_clicked(self):
        """
        Slot documentation goes here.

        清除发送
        """
        self.textEdit_send.clear()
        self.sent = 0
        self.statusbar_showMessage()

    @pyqtSlot(bool)
    def on_checkBox_send16_clicked(self, checked):
        """
        Slot documentation goes here.

        @param checked 16进制发送
        @type bool
        """
        temp = self.textEdit_send.toPlainText()
        if checked:
            self.textEdit_send.setPlainText(self.str_hex(temp))
        else:
            if self.hex_check(temp):
                self.textEdit_send.setPlainText(
                    bytes.fromhex(temp.replace(' ', '')).decode(encoding='gbk', errors='replace'))
            else:
                self.checkBox_send16.setChecked(True)

    @pyqtSlot()
    def on_pushButton_receive_clear_clicked(self):
        """
        Slot documentation goes here.

        清除接收
        """
        self.textEdit_receive.clear()
        self.received = 0
        self.sent = 0
        self.statusbar_showMessage()

    @pyqtSlot(bool)
    def on_checkBox_time_r_clicked(self, checked):
        """
        Slot documentation goes here.

        @param checked 接收时间戳
        @type bool
        """
        self.timestamp_r = checked

    @pyqtSlot(bool)
    def on_checkBox_time_s_clicked(self, checked):
        """
        Slot documentation goes here.

        @param checked 发送时间戳
        @type bool
        """
        self.timestamp_s = checked

    @pyqtSlot(bool)
    def on_checkBox_receive16_clicked(self, checked):
        """
        Slot documentation goes here.

        @param checked 16进制显示
        @type bool
        """
        temp = self.textEdit_receive.toPlainText()
        if checked:
            self.textEdit_receive.setPlainText(self.str_hex(temp))
            self.textEdit_receive.moveCursor(QTextCursor.End)
        else:
            self.textEdit_receive.setPlainText(
                bytes.fromhex(temp.replace(' ', '')).decode(encoding='gbk', errors='replace'))
            self.textEdit_receive.moveCursor(QTextCursor.End)

    @pyqtSlot()
    def on_pushButton_save_clicked(self):
        """
        Slot documentation goes here.

        保存接收区
        """
        savepath = QFileDialog.getSaveFileName(self, '保存接收区', '.', '纯文本(*.txt);;All Files(*.*)')
        with open(savepath[0], 'w', encoding='utf-8')as f:
            f.write(self.textEdit_receive.toPlainText())

    @pyqtSlot()
    def on_action_exit_triggered(self):
        """
        Slot documentation goes here.

        退出
        """
        self.close()

    @pyqtSlot()
    def on_action_font_r_triggered(self):
        """
        Slot documentation goes here.

        接收区字体设置
        """
        font, ok = QFontDialog.getFont()
        if ok:
            self.textEdit_receive.setFont(font)

    @pyqtSlot()
    def on_action_font_s_triggered(self):
        """
        Slot documentation goes here.
        发送区字体设置
        """
        font, ok = QFontDialog.getFont()
        if ok:
            self.textEdit_send.setFont(font)

    @pyqtSlot()
    def on_action_about_triggered(self):
        """
        Slot documentation goes here.

        关于
        """
        QMessageBox.aboutQt(None)

    @staticmethod
    def str_hex(string):
        hex = bytes(string, encoding='gbk', errors='replace').hex()
        return ' '.join([hex[i:i + 2] for i in range(0, len(hex), 2)])

    def hex_check(self, hex):
        temp = re.search(r'[^0-9a-fA-F ]', hex)
        if temp:
            QMessageBox.information(self, "提示", "请输入正确的格式：0-9 a-f A-F")
            cur = self.textEdit_send.textCursor()
            cur.setPosition(temp.span()[0])
            cur.movePosition(QTextCursor.NextCharacter, QTextCursor.KeepAnchor)
            self.textEdit_send.setTextCursor(cur)
            self.textEdit_send.setFocus()
            return False
        if len(''.join(re.findall(r'[0-9a-fA-F]+', hex))) % 2 != 0:
            QMessageBox.information(self, "提示", "16进制应该是偶数位")
            return False
        return True


class KeyboardThread(QThread):
    sigOut = pyqtSignal(str)

    def __init__(self, parent=None):
        super(KeyboardThread, self).__init__(parent)
        self.old_key = '[]'
        self.new_key = ''

        pygame.init()
        self.size = (400, 300)
        self.screen = pygame.display.set_mode(self.size, pygame.RESIZABLE)
        self.background = pygame.image.load(r"./images/key.jpg").convert()
        self.screen.blit(pygame.transform.scale(self.background, self.size), (0, 0))
        pygame.display.set_caption('键位图')
        pygame.display.update()

    def __del__(self):
        try:
            pygame.quit()
        except SystemExit:
            pass
        except:
            traceback.print_exc()

    def run(self):
        while True:
            time.sleep(0.01)
            for event in pygame.event.get():
                if event.type == pygame.VIDEORESIZE:
                    self.size = event.size
                    self.screen = pygame.display.set_mode(self.size, pygame.RESIZABLE)
                    self.screen.blit(pygame.transform.scale(self.background, self.size), (0, 0))
                    pygame.display.flip()
            self.new_key = str([i for i, j in enumerate(pygame.key.get_pressed()) if j > 0])
            if self.new_key != self.old_key:
                self.sigOut.emit(self.new_key)
                self.old_key = self.new_key


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    musicWin = Music()
    try:
        musicWin.show()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        input()
    finally:
        sys.exit(app.exec_())
