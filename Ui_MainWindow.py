# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\STM32\无源蜂鸣器-音乐\上位机\music\eric6\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_music(object):
    def setupUi(self, music):
        music.setObjectName("music")
        music.resize(800, 600)
        music.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(music)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_main = QtWidgets.QWidget()
        self.tab_main.setObjectName("tab_main")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_main)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_music = QtWidgets.QGroupBox(self.tab_main)
        self.groupBox_music.setObjectName("groupBox_music")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_music)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radioButton_notes = QtWidgets.QRadioButton(self.groupBox_music)
        self.radioButton_notes.setObjectName("radioButton_notes")
        self.gridLayout_2.addWidget(self.radioButton_notes, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_speed = QtWidgets.QLabel(self.groupBox_music)
        self.label_speed.setObjectName("label_speed")
        self.horizontalLayout_3.addWidget(self.label_speed)
        self.horizontalSlider_speed = QtWidgets.QSlider(self.groupBox_music)
        self.horizontalSlider_speed.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_speed.setObjectName("horizontalSlider_speed")
        self.horizontalLayout_3.addWidget(self.horizontalSlider_speed)
        self.lcdNumber_speed = QtWidgets.QLCDNumber(self.groupBox_music)
        self.lcdNumber_speed.setObjectName("lcdNumber_speed")
        self.horizontalLayout_3.addWidget(self.lcdNumber_speed)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)
        self.radioButton_piano = QtWidgets.QRadioButton(self.groupBox_music)
        self.radioButton_piano.setObjectName("radioButton_piano")
        self.gridLayout_2.addWidget(self.radioButton_piano, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_music)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox_music)
        self.groupBox_serial = QtWidgets.QGroupBox(self.tab_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_serial.sizePolicy().hasHeightForWidth())
        self.groupBox_serial.setSizePolicy(sizePolicy)
        self.groupBox_serial.setObjectName("groupBox_serial")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_serial)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_receive = QtWidgets.QGroupBox(self.groupBox_serial)
        self.groupBox_receive.setObjectName("groupBox_receive")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_receive)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textEdit_receive = QtWidgets.QTextEdit(self.groupBox_receive)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_receive.sizePolicy().hasHeightForWidth())
        self.textEdit_receive.setSizePolicy(sizePolicy)
        self.textEdit_receive.setObjectName("textEdit_receive")
        self.horizontalLayout_2.addWidget(self.textEdit_receive)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_receive_clear = QtWidgets.QPushButton(self.groupBox_receive)
        self.pushButton_receive_clear.setObjectName("pushButton_receive_clear")
        self.verticalLayout.addWidget(self.pushButton_receive_clear)
        self.checkBox_time_r = QtWidgets.QCheckBox(self.groupBox_receive)
        self.checkBox_time_r.setObjectName("checkBox_time_r")
        self.verticalLayout.addWidget(self.checkBox_time_r)
        self.checkBox_time_s = QtWidgets.QCheckBox(self.groupBox_receive)
        self.checkBox_time_s.setObjectName("checkBox_time_s")
        self.verticalLayout.addWidget(self.checkBox_time_s)
        self.checkBox_receive16 = QtWidgets.QCheckBox(self.groupBox_receive)
        self.checkBox_receive16.setObjectName("checkBox_receive16")
        self.verticalLayout.addWidget(self.checkBox_receive16)
        self.pushButton_save = QtWidgets.QPushButton(self.groupBox_receive)
        self.pushButton_save.setObjectName("pushButton_save")
        self.verticalLayout.addWidget(self.pushButton_save)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addWidget(self.groupBox_receive)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_serial)
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit_send = QtWidgets.QTextEdit(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_send.sizePolicy().hasHeightForWidth())
        self.textEdit_send.setSizePolicy(sizePolicy)
        self.textEdit_send.setObjectName("textEdit_send")
        self.horizontalLayout.addWidget(self.textEdit_send)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_send = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_send.setObjectName("pushButton_send")
        self.verticalLayout_2.addWidget(self.pushButton_send)
        self.pushButton_stop = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.verticalLayout_2.addWidget(self.pushButton_stop)
        self.pushButton_send_clear = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_send_clear.setObjectName("pushButton_send_clear")
        self.verticalLayout_2.addWidget(self.pushButton_send_clear)
        self.checkBox_send16 = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_send16.setObjectName("checkBox_send16")
        self.verticalLayout_2.addWidget(self.checkBox_send16)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addWidget(self.groupBox_6)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.groupBox_port_setting = QtWidgets.QGroupBox(self.groupBox_serial)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_port_setting.sizePolicy().hasHeightForWidth())
        self.groupBox_port_setting.setSizePolicy(sizePolicy)
        self.groupBox_port_setting.setMinimumSize(QtCore.QSize(350, 0))
        self.groupBox_port_setting.setObjectName("groupBox_port_setting")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_port_setting)
        self.gridLayout.setObjectName("gridLayout")
        self.label_baud_rate = QtWidgets.QLabel(self.groupBox_port_setting)
        self.label_baud_rate.setObjectName("label_baud_rate")
        self.gridLayout.addWidget(self.label_baud_rate, 1, 0, 1, 1)
        self.comboBox_baud_rate = QtWidgets.QComboBox(self.groupBox_port_setting)
        self.comboBox_baud_rate.setObjectName("comboBox_baud_rate")
        self.gridLayout.addWidget(self.comboBox_baud_rate, 1, 1, 1, 2)
        self.label_stop_bit = QtWidgets.QLabel(self.groupBox_port_setting)
        self.label_stop_bit.setObjectName("label_stop_bit")
        self.gridLayout.addWidget(self.label_stop_bit, 2, 0, 1, 1)
        self.comboBox_stop_bit = QtWidgets.QComboBox(self.groupBox_port_setting)
        self.comboBox_stop_bit.setObjectName("comboBox_stop_bit")
        self.gridLayout.addWidget(self.comboBox_stop_bit, 2, 1, 1, 2)
        self.label_data_bit = QtWidgets.QLabel(self.groupBox_port_setting)
        self.label_data_bit.setObjectName("label_data_bit")
        self.gridLayout.addWidget(self.label_data_bit, 3, 0, 1, 1)
        self.comboBox_data_bit = QtWidgets.QComboBox(self.groupBox_port_setting)
        self.comboBox_data_bit.setObjectName("comboBox_data_bit")
        self.gridLayout.addWidget(self.comboBox_data_bit, 3, 1, 1, 2)
        self.label_check_bit = QtWidgets.QLabel(self.groupBox_port_setting)
        self.label_check_bit.setObjectName("label_check_bit")
        self.gridLayout.addWidget(self.label_check_bit, 4, 0, 1, 1)
        self.comboBox_check_bit = QtWidgets.QComboBox(self.groupBox_port_setting)
        self.comboBox_check_bit.setObjectName("comboBox_check_bit")
        self.gridLayout.addWidget(self.comboBox_check_bit, 4, 1, 1, 2)
        self.label_operation = QtWidgets.QLabel(self.groupBox_port_setting)
        self.label_operation.setObjectName("label_operation")
        self.gridLayout.addWidget(self.label_operation, 5, 0, 1, 1)
        self.pushButton_on_off = QtWidgets.QPushButton(self.groupBox_port_setting)
        self.pushButton_on_off.setObjectName("pushButton_on_off")
        self.gridLayout.addWidget(self.pushButton_on_off, 5, 1, 1, 2)
        self.pushButton_search_port = QtWidgets.QPushButton(self.groupBox_port_setting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_search_port.sizePolicy().hasHeightForWidth())
        self.pushButton_search_port.setSizePolicy(sizePolicy)
        self.pushButton_search_port.setObjectName("pushButton_search_port")
        self.gridLayout.addWidget(self.pushButton_search_port, 0, 0, 1, 1)
        self.comboBox_serial_port = QtWidgets.QComboBox(self.groupBox_port_setting)
        self.comboBox_serial_port.setObjectName("comboBox_serial_port")
        self.gridLayout.addWidget(self.comboBox_serial_port, 0, 1, 1, 2)
        self.horizontalLayout_4.addWidget(self.groupBox_port_setting)
        self.verticalLayout_4.addWidget(self.groupBox_serial)
        self.tabWidget.addTab(self.tab_main, "")
        self.tab_keymap = QtWidgets.QWidget()
        self.tab_keymap.setObjectName("tab_keymap")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tab_keymap)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_keymap = QtWidgets.QLabel(self.tab_keymap)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_keymap.sizePolicy().hasHeightForWidth())
        self.label_keymap.setSizePolicy(sizePolicy)
        self.label_keymap.setStyleSheet("border-image: url(:/pic/images/key.jpg);")
        self.label_keymap.setText("")
        self.label_keymap.setObjectName("label_keymap")
        self.horizontalLayout_6.addWidget(self.label_keymap)
        self.tabWidget.addTab(self.tab_keymap, "")
        self.horizontalLayout_5.addWidget(self.tabWidget)
        music.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(music)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        self.menu_setup = QtWidgets.QMenu(self.menubar)
        self.menu_setup.setObjectName("menu_setup")
        music.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(music)
        self.statusbar.setObjectName("statusbar")
        music.setStatusBar(self.statusbar)
        self.action_about = QtWidgets.QAction(music)
        self.action_about.setObjectName("action_about")
        self.action_exit = QtWidgets.QAction(music)
        self.action_exit.setObjectName("action_exit")
        self.action_font_r = QtWidgets.QAction(music)
        self.action_font_r.setObjectName("action_font_r")
        self.action_font_s = QtWidgets.QAction(music)
        self.action_font_s.setObjectName("action_font_s")
        self.menu_file.addAction(self.action_exit)
        self.menu_help.addAction(self.action_about)
        self.menu_setup.addAction(self.action_font_r)
        self.menu_setup.addAction(self.action_font_s)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_setup.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        self.retranslateUi(music)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(music)
        music.setTabOrder(self.radioButton_notes, self.horizontalSlider_speed)
        music.setTabOrder(self.horizontalSlider_speed, self.radioButton_piano)
        music.setTabOrder(self.radioButton_piano, self.pushButton_search_port)
        music.setTabOrder(self.pushButton_search_port, self.comboBox_serial_port)
        music.setTabOrder(self.comboBox_serial_port, self.comboBox_baud_rate)
        music.setTabOrder(self.comboBox_baud_rate, self.comboBox_stop_bit)
        music.setTabOrder(self.comboBox_stop_bit, self.comboBox_data_bit)
        music.setTabOrder(self.comboBox_data_bit, self.comboBox_check_bit)
        music.setTabOrder(self.comboBox_check_bit, self.pushButton_on_off)
        music.setTabOrder(self.pushButton_on_off, self.textEdit_send)
        music.setTabOrder(self.textEdit_send, self.pushButton_send)
        music.setTabOrder(self.pushButton_send, self.pushButton_stop)
        music.setTabOrder(self.pushButton_stop, self.pushButton_send_clear)
        music.setTabOrder(self.pushButton_send_clear, self.checkBox_send16)
        music.setTabOrder(self.checkBox_send16, self.textEdit_receive)
        music.setTabOrder(self.textEdit_receive, self.pushButton_receive_clear)
        music.setTabOrder(self.pushButton_receive_clear, self.checkBox_time_r)
        music.setTabOrder(self.checkBox_time_r, self.checkBox_time_s)
        music.setTabOrder(self.checkBox_time_s, self.checkBox_receive16)
        music.setTabOrder(self.checkBox_receive16, self.pushButton_save)
        music.setTabOrder(self.pushButton_save, self.tabWidget)

    def retranslateUi(self, music):
        _translate = QtCore.QCoreApplication.translate
        music.setWindowTitle(_translate("music", "Music"))
        self.groupBox_music.setTitle(_translate("music", "音乐设置"))
        self.radioButton_notes.setText(_translate("music", "播放模式"))
        self.label_speed.setText(_translate("music", "速度调节"))
        self.radioButton_piano.setText(_translate("music", "弹奏模式"))
        self.groupBox_serial.setTitle(_translate("music", "串口"))
        self.groupBox_receive.setTitle(_translate("music", "接收区"))
        self.pushButton_receive_clear.setText(_translate("music", "清除接收"))
        self.checkBox_time_r.setText(_translate("music", "接收戳"))
        self.checkBox_time_s.setText(_translate("music", "发送戳"))
        self.checkBox_receive16.setText(_translate("music", "16进制显示"))
        self.pushButton_save.setText(_translate("music", "保存"))
        self.groupBox_6.setTitle(_translate("music", "发送区"))
        self.pushButton_send.setText(_translate("music", "发送"))
        self.pushButton_stop.setText(_translate("music", "停止"))
        self.pushButton_send_clear.setText(_translate("music", "清除发送"))
        self.checkBox_send16.setText(_translate("music", "16进制发送"))
        self.groupBox_port_setting.setTitle(_translate("music", "串口设置"))
        self.label_baud_rate.setText(_translate("music", "波特率"))
        self.label_stop_bit.setText(_translate("music", "停止位"))
        self.label_data_bit.setText(_translate("music", "数据位"))
        self.label_check_bit.setText(_translate("music", "校验位"))
        self.label_operation.setText(_translate("music", "串口操作"))
        self.pushButton_on_off.setText(_translate("music", "打开串口"))
        self.pushButton_search_port.setText(_translate("music", "串口搜索"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_main), _translate("music", "主界面"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_keymap), _translate("music", "键位图"))
        self.menu_file.setTitle(_translate("music", "文件"))
        self.menu_help.setTitle(_translate("music", "帮助"))
        self.menu_setup.setTitle(_translate("music", "设置"))
        self.action_about.setText(_translate("music", "关于"))
        self.action_exit.setText(_translate("music", "退出"))
        self.action_font_r.setText(_translate("music", "接收区字体设置"))
        self.action_font_s.setText(_translate("music", "发送区字体设置"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    music = QtWidgets.QMainWindow()
    ui = Ui_music()
    ui.setupUi(music)
    music.show()
    sys.exit(app.exec_())
