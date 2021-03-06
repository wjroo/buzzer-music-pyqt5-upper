# -*- coding: utf-8 -*-

"""
波特率
baudrate = [
    "110", "300", "600", "1200", "2400",
    "4800", "9600", "14400", "19200", "38400",
    "43000", "57600", "76800", "115200", "128000",
    "230400", "256000", "460800", "921600", "1000000",
    "2000000", "3000000"
]

"""

keygame = {
    '282': '65',
    '283': '69',
    '284': '73',
    '285': '78',
    '286': '82',
    '287': '87',
    '288': '92',
    '289': '98',
    '290': '104',
    '291': '110',
    '292': '117',
    '293': '123',

    '49': '131',
    '50': '139',
    '51': '147',
    '52': '156',
    '53': '165',
    '54': '175',
    '55': '185',
    '56': '196',
    '57': '208',
    '48': '220',
    '45': '233',
    '61': '247',

    '113': '262',
    '119': '277',
    '101': '294',
    '114': '311',
    '116': '330',
    '121': '349',
    '117': '370',
    '105': '392',
    '111': '415',
    '112': '440',
    '91': '466',
    '93': '494',

    '97': '523',
    '115': '554',
    '100': '587',
    '102': '622',
    '103': '659',
    '104': '698',
    '106': '740',
    '107': '784',
    '108': '831',
    '59': '880',
    '39': '932',
    '13': '988',

    '122': '1047',
    '120': '1109',
    '99': '1175',
    '118': '1245',
    '98': '1319',
    '110': '1397',
    '109': '1480',
    '44': '1568',
    '46': '1661',
    '47': '1760',
    '303': '1865',
    '92': '1976'
}

keyfre = {
    16777264: 65,
    16777265: 69,
    16777266: 73,
    16777267: 78,
    16777268: 82,
    16777269: 87,
    16777270: 92,
    16777271: 98,
    16777272: 104,
    16777273: 110,
    16777274: 117,
    16777275: 123,
    49: 131,
    50: 139,
    51: 147,
    52: 156,
    53: 165,
    54: 175,
    55: 185,
    56: 196,
    57: 208,
    48: 220,
    45: 233,
    61: 247,
    81: 262,
    87: 277,
    69: 294,
    82: 311,
    84: 330,
    89: 349,
    85: 370,
    73: 392,
    79: 415,
    80: 440,
    91: 466,
    93: 494,
    65: 523,
    83: 554,
    68: 587,
    70: 622,
    71: 659,
    72: 698,
    74: 740,
    75: 784,
    76: 831,
    59: 880,
    39: 932,
    16777220: 988,
    90: 1047,
    88: 1109,
    67: 1175,
    86: 1245,
    66: 1319,
    78: 1397,
    77: 1480,
    44: 1568,
    46: 1661,
    47: 1760,
    16777248: 1865,
    92: 1976
}
keyname = {
    16777264: "F1",
    16777265: "F2",
    16777266: "F3",
    16777267: "F4",
    16777268: "F5",
    16777269: "F6",
    16777270: "F7",
    16777271: "F8",
    16777272: "F9",
    16777273: "F10",
    16777274: "F11",
    16777275: "F12",
    49: "1",
    50: "2",
    51: "3",
    52: "4",
    53: "5",
    54: "6",
    55: "7",
    56: "8",
    57: "9",
    48: "0",
    45: "-",
    61: "=",
    81: "Q",
    87: "W",
    69: "E",
    82: "R",
    84: "T",
    89: "Y",
    85: "U",
    73: "I",
    79: "O",
    80: "P",
    91: "[",
    93: "]",
    65: "A",
    83: "S",
    68: "D",
    70: "F",
    71: "G",
    72: "H",
    74: "J",
    75: "K",
    76: "L",
    59: ";",
    39: "'",
    16777220: "Enter",
    90: "Z",
    88: "X",
    67: "C",
    86: "V",
    66: "B",
    78: "N",
    77: "M",
    44: ",",
    46: ".",
    47: "/",
    16777248: "Shift",
    92: "\\"
}
keynote = {
    16777264: 310,
    16777265: 311,
    16777266: 320,
    16777267: 321,
    16777268: 330,
    16777269: 340,
    16777270: 341,
    16777271: 350,
    16777272: 351,
    16777273: 360,
    16777274: 361,
    16777275: 370,
    49: 410,
    50: 411,
    51: 420,
    52: 421,
    53: 430,
    54: 440,
    55: 441,
    56: 450,
    57: 451,
    48: 460,
    45: 461,
    61: 470,
    81: 510,
    87: 511,
    69: 520,
    82: 521,
    84: 530,
    89: 540,
    85: 541,
    73: 550,
    79: 551,
    80: 560,
    91: 561,
    93: 570,
    65: 610,
    83: 611,
    68: 620,
    70: 621,
    71: 630,
    72: 640,
    74: 641,
    75: 650,
    76: 651,
    59: 660,
    39: 661,
    16777220: 670,
    90: 710,
    88: 711,
    67: 720,
    86: 721,
    66: 730,
    78: 740,
    77: 741,
    44: 750,
    46: 751,
    47: 760,
    16777248: 761,
    92: 770
}

# 停止位
stopBits = {"1": 1, "1.5": 3, "2": 2}

# 校验位
parity = {"None": 0, "Odd": 3, "Even": 2}

# QSerialPort.SerialPortError
serialPortError = {
    0: ("NoError", "没有发生错误"),
    1: ("DeviceNotFoundError", "尝试打开不存在的设备"),
    2: ("PermissionError", "尝试打开另一个进程已打开的设备或用户没有足够的权限和凭据来打开"),
    3: ("OpenError", "尝试打开在该设备下已打开的设备"),
    13: ("NotOpenError", "尝试执行仅在打开设备后才能成功执行的操作"),
    4: ("ParityError", "硬件在读取数据时检测到奇偶校验错误"),
    5: ("FramingError", "读取数据时硬件检测到帧错误"),
    6: ("BreakConditionError", "硬件检测到输入线上断路"),
    7: ("WriteError", "写入数据时发生I/O错误"),
    8: ("ReadError", "读取数据时发生I/O错误"),
    9: ("ResourceError", "当资源变得不可用时（例如，从系统中意外删除设备时），发生I/O错误"),
    10: ("UnsupportedOperationError", "操作系统不支持或禁止所请求的设备操作"),
    12: ("TimeoutError", "发生超时错误"),
    11: ("UnknownError", "发生无法识别的错误")
}
