from os import uname
import board


def get_pin_definition(pinid):
    controller = uname()[0]
    machine = uname()[4]
        if controller == 'rp2040':
    	boardspins = {'A0': board.A0, 'A1': board.A1, 'A2':board.A2, 'GP0': board.GP0, 'GP1': board.GP1, 'GP10': board.GP10,
    		 'GP11': board.GP11, 'GP12': board.GP12, 'GP13': board.GP13, 'GP14': board.GP14, 'GP15': board.GP15,
    		 'GP16': board.GP16, 'GP17': board.GP17, 'GP18': board.GP18, 'GP19': board.GP19, 'GP2': board.GP15,
    		 'GP20': board.GP20, 'GP21': board.GP21, 'GP22': board.GP22, 'GP25': board.GP25, 'GP26': board.GP26,
    		 'GP26_A0': GP26_A0, 'GP27': board.GP27, 'GP27_A1': board.GP27_A1, 'GP28': board.GP28, 'GP28_A2': board.GP28_A2,
    		 'GP3': board.GP3, 'GP4': board.GP4, 'GP5':board.GP5, 'GP6': board.GP6, 'GP7': board.GP7, 'GP8': board.GP8,
    		 'GP9': board.GP9, 'LED': board.LED}
        return boardspins[pinid]
    if controller == 'esp32s2':
        boardspins = {'A0': board.A0, 'A1': board.A1, 'A2': board.A2, 'A3': board.A3, 'A4': board.A4, 'A5': board.A5,
                'IO1': board.IO1, 'IO2': board.IO2, 'IO3': board.IO3, 'IO4': board.IO4, 'IO5': board.IO5, 'IO6': board.IO6,
                'IO7': board.IO7, 'IO8': board.IO8, 'IO9': board.IO9, 'IO10': board.IO10, 'IO11': board.IO11,
                'IO12': board.IO12, 'IO13': board.IO13, 'IO14': board.IO14, 'IO15': board.IO15,
                'IO16': board.IO16, 'IO21': board.IO21, 'IO42': board.IO42}
        return boardspins[pinid]
    if controller == 'samd51':
        if machine == 'Seeeduino Wio Terminal with samd51p19':
            boardspins = {'A0': board.A0, 'A1': board.A1, 'A2': board.A2, 'A3': board.A3, 'A4': board.A4,
                        'A5': board.A5, 'A6': board.A6, 'A7': board.A7, 'A8': board.A8,
                        'D0': board.D0, 'D1': board.D1, 'D2': board.D2, 'D3': board.D3, 'D4': board.D4, 'D5': board.D5,
                        'D6': board.D6, 'D7': board.D7, 'D8': board.D8, 'D9': board.D9, 'D10': board.D10,
                        'D13': board.D13, 'LIGHT': board.LIGHT,
                        'BUTTON_1': board.BUTTON_1, 'BUTTON_2': board.BUTTON_2, 'BUTTON_3': board.BUTTON_3,
                        'BUZZER': board.BUZZER, 'LED': board.LED, 'IR': board.IR, 'MIC': board.MIC,
                        'SWITCH_DOWN': board.SWITCH_DOWN, 'SWITCH_LEFT': board.SWITCH_LEFT,
                        'SWITCH_PRESS': board.SWITCH_PRESS, 'SWITCH_RIGHT': board.SWITCH_RIGHT,
                        'SWITCH_UP': board.SWITCH_UP}
        else:
            boardspins = {'A0': board.A0, 'A1': board.A1, 'A2': board.A2, 'A3': board.A3, 'A4': board.A4, 'A5': board.A5,
                        'D0': board.D0, 'D1': board.D1, 'D2': board.D2, 'D3': board.D3, 'D4': board.D4, 'D5': board.D5,
                        'D6': board.D6, 'D7': board.D7, 'D8': board.D8, 'D9': board.D9, 'D10': board.D10,
                        'D11': board.D11, 'D12': board.D12, 'D13': board.D13}
        return boardspins[pinid]
    if controller == 'samd21':
        if machine == 'Seeeduino XIAO with samd21g18':
            boardspins = {'A0': board.A0, 'A1': board.A1, 'A2': board.A2, 'A3': board.A3, 'A4': board.A4,
                        'A5': board.A5, 'A6': board.A6, 'A7': board.A7, 'A8': board.A8, 'A9': board.A9,
                        'A10': board.A10, 
                        'D0': board.D0, 'D1': board.D1, 'D2': board.D2, 'D3': board.D3, 'D4': board.D4,
                        'D5': board.D5, 'D6': board.D6, 'D7': board.D7, 'D8': board.D8, 'D9': board.D9,
                        'D10': board.D10, 'D13': board.D13, 'BLUE_LED': board.BLUE_LED, 'LED': board.LED}
            return boardspins[pinid]
        else:
            boardspins = {'A0': board.A0, 'A1': board.A1, 'A2': board.A2, 'A3': board.A3, 'A4': board.A4,
                        'D0': board.D0, 'D1': board.D1, 'D2': board.D2, 'D3': board.D3, 'D4': board.D4,
                        'D13': board.D13}
            return boardspins[pinid]
    if controller == 'stm32f4':
        boardspins = {'A0': board.A0, 'A1': board.A1, 'A2': board.A2, 'A3': board.A3, 'A4': board.A4,
                      'A5': board.A5, 'A6': board.A6, 'A7': board.A7, 'A8': board.A8, 'A9': board.A9,
                      'A15': board.A15,
                      'B0': board.B0, 'B1': board.B1, 'B2': board.B2, 'B3': board.B3, 'B4': board.B4,
                      'B5': board.B5, 'B6': board.B6, 'B7': board.B7, 'B8': board.B8, 'B9': board.B9,
                      'B10': board.B10, 'B11': board.B11, 'B12': board.B12, 'B13': board.B13, 'B14': board.B14,
                      'B15': board.B15}
        return boardspins[pinid]
          
    return 'Not Implemented'


class Representaciones(object):
    def __init__(self, controlador):
        if controlador == 'esp32s2':
            self.pinout = ['+-------+-------+------+---+-esp32s2--+---+------+-------+-------+\n' ,
                            '|IO Nam | Name  | Mode | V | Physical | V | Mode | Name  |IO Nam |\n' ,
                            '+-------+-------+------+---+----++----+---+------+-------+-------+\n' ,
                            '|       |       |      |   |    ||    |   |NeoPIX|  45   |       |\n' ,
                            '|       |       |      |   |    || 32 |   |      |  SCL  | IO34  |\n' ,
                            '|       |       |      |   |    || 31 |   |      |  SDA  | IO33  |\n' ,
                            '|       |       |      |   |    || 30 |   |      |  Aref |       |\n' ,
                            '|       |       |      |   |    || 29 |   |      |  GND  |       |\n' ,
                            '|       |       |      |   |  1 || 28 |   |RedLed|  42   | D13   |\n' ,
                            '|       | IOref |      |   |  2 || 27 |   |      |  IO21 | D12   |\n' ,
                            '|       |  RST  |      |   |  3 || 26 |   | ADC2 |  IO16 | D11   |\n' ,
                            '|       |  3.3v |      |   |  4 || 25 |   | ADC2 |  IO15 | D10   |\n' ,
                            '|       |  VHI  |      |   |  5 || 24 |   | ADC2 |  IO14 | D9    |\n' ,
                            '|       |  GND  |      |   |  6 || 23 |   | ADC2 |  IO13 | D8    |\n' ,
                            '|       |  GND  |      |   |  7 ||    |   |      |       |       |\n' ,
                            '|       |  Vin  |      |   |  8 || 22 |   | ADC2 |  IO12 | D7    |\n' ,
                            '|       |       |      |   |    || 21 |   |      |  IO11 | D6    |\n' ,
                            '| IO17  |  A0   |  DAC |   |  9 || 20 |   | ADC1 |  IO10 | D5    |\n' ,
                            '| IO18  |  A1   |  DAC |   | 10 || 19 |   | ADC1 |  IO9  | D4    |\n' ,
                            '|  IO1  |  A2   | ADC1 |   | 11 || 18 |   | ADC1 |  IO8  | D3    |\n' ,
                            '|  IO2  |  A3   | ADC1 |   | 12 || 17 |   | ADC1 |  IO7  | D2    |\n' ,
                            '|  IO3  |  A4   | ADC1 |   | 13 || 16 |   | ADC1 |  IO5  | D1    |\n' ,
                            '|  IO4  |  A5   | ADC1 |   | 14 || 15 |   | ADC1 |  IO6  | D0    |\n' ,
                            '|                                                                |\n' ,
                            '|                        |RST |SCK |MISO|   RST:IO36 MISO:IO35   |\n' ,
                            '|                        |GND |MOSI| 5V |   MOSI:IO37            |\n' ,
                            '|                                                                |\n' ,
                            '+-------+-------+------+---+----++----+---+------+-------+-------+\n' ,
                            '|IO Nam | Name  | Mode | V | Physical | V | Mode | Name  |IO Nam |\n' ,
                            '+-------+-------+------+---+----++----+---+------+-------+-------+\n' ]

            [print(linea) for linea in self.pinout]

        if controlador == 'samd51':
            self.pinout = ['+-------+-------+------+---+-M4--+---+------+-------+-------+\n' ,
                            '|IO Nam | Name  | Mode | V | Physical | V | Mode | Name  |IO Nam |\n' ,
                            '+-------+-------+------+---+----++----+---+------+-------+-------+\n' ,
                            '|       |       |      |   |    ||    |   |NeoPIX|  40   |       |\n' ,
                            '|       |       |      |   |    || 32 |   |      |  SCL  | IO34  |\n' ,
                            '|       |       |      |   |    || 31 |   |      |  SDA  | IO33  |\n' ,
                            '|       |       |      |   |    || 30 |   |      |  Aref |       |\n' ,
                            '|       |       |      |   |    || 29 |   |      |  GND  |       |\n' ,
                            '|       |       |      |   |  1 || 28 |   |RedLed|  42   | D13   |\n' ,
                            '|       | IOref |      |   |  2 || 27 |   |      |  IO21 | D12   |\n' ,
                            '|       |  RST  |      |   |  3 || 26 |   | ADC2 |  IO16 | D11   |\n' ,
                            '|       |  3.3v |      |   |  4 || 25 |   | ADC2 |  IO15 | D10   |\n' ,
                            '|       |  VHI  |      |   |  5 || 24 |   | ADC2 |  IO14 | D9    |\n' ,
                            '|       |  GND  |      |   |  6 || 23 |   | ADC2 |  IO13 | D8    |\n' ,
                            '|       |  GND  |      |   |  7 ||    |   |      |       |       |\n' ,
                            '|       |  Vin  |      |   |  8 || 22 |   | ADC2 |  IO12 | D7    |\n' ,
                            '|       |       |      |   |    || 21 |   |      |  IO11 | D6    |\n' ,
                            '| IO17  |  A0   |  DAC |   |  9 || 20 |   | ADC1 |  IO10 | D5    |\n' ,
                            '| IO18  |  A1   |  DAC |   | 10 || 19 |   | ADC1 |  IO9  | D4    |\n' ,
                            '|  IO1  |  A2   | ADC1 |   | 11 || 18 |   | ADC1 |  IO8  | D3    |\n' ,
                            '|  IO2  |  A3   | ADC1 |   | 12 || 17 |   | ADC1 |  IO7  | D2    |\n' ,
                            '|  IO3  |  A4   | ADC1 |   | 13 || 16 |   | ADC1 |  IO5  | D1    |\n' ,
                            '|  IO4  |  A5   | ADC1 |   | 14 || 15 |   | ADC1 |  IO6  | D0    |\n' ,
                            '|                                                                |\n' ,
                            '|                        |RST |SCK |MISO|   RST:IO36 MISO:IO35   |\n' ,
                            '|                        |GND |MOSI| 5V |   MOSI:IO37            |\n' ,
                            '|                                                                |\n' ,
                            '+-------+-------+------+---+----++----+---+------+-------+-------+\n' ,
                            '|IO Nam | Name  | Mode | V | Physical | V | Mode | Name  |IO Nam |\n' ,
                            '+-------+-------+------+---+----++----+---+------+-------+-------+\n']

        [print(linea) for linea in self.pinout]

        if controlador == 'samd21':
            self.pinout = ['+-------+-------+------+---+-Trinket--+---+------+-------+-------+\n' ,
                            '|IO Nam | Name  | Mode | V | Physical | V | Mode | Name  |IO Nam |\n' ,
                            '+-------+-------+------+---+----++----+---+------+-------+-------+\n' ,
                            '|       |       |      |   |VBAT||VBUS|   |      |       |       |\n' ,
                            '|       |       |      |   |GND || 11 |   | SDA  |  IO9  | A2    |\n' ,
                            '|  A4   | MOSI  |  TX  |   | 7  ||  3 |   |      | TOUCH | A0    |\n' ,
                            '|       |  SCK  |  RX  |   | 8  || 12 |   | SCL  | MISO  | A1    |\n' ,
                            '|       |       |      |   | RST||3v3 |   |      |       |      |\n' ,
                            '+-------+-------+------+---+----++----+---+------+-------+-------+\n' ,
                            '|IO Nam | Name  | Mode | V | Physical | V | Mode | Name  |IO Nam |\n' ,
                            '+-------+-------+------+---+----++----+---+------+-------+-------+\n']

        [print(linea) for linea in self.pinout]


