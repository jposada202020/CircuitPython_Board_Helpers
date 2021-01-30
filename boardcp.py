import digitalio
from digitalio import Pull
import time
from adafruit_onewire.bus import OneWireBus
from adafruit_ds18x20 import DS18X20
from random import randint
import pulseio
import board
import analogio
import displayio
from adafruit_display_text import label
import terminalio
import adafruit_displayio_ssd1306
from controladores import get_pin_definition
from os import uname
if uname()[0] == 'esp32s2':
    import socketpool
    import adafruit_requests
    import wifi
    import ssl
    from privados import secrets


class Receiver(object):
    """
    Creates a Receiver object
    ex: sreceptor = Receiver('A2')
    """
    def __init__(self, pinid, analog: bool = False):
        if analog:
            self.pin = analogio.AnalogIn(get_pin_definition(pinid))
            self.id = pinid
        else:
            self.pin = digitalio.DigitalInOut(get_pin_definition(pinid))
            self.pin.direction = digitalio.Direction.INPUT
            self.id = pinid

    def adc_to_voltage(self):
        return self.pin.value / 65535 * self.pin.reference_voltage

    def cleanup(self):
        self.pin.deinit()

    def __str__(self):
        return r'Sensor is using IO number: {}'.format(self.id)


class Emitter(object):
    """
    Creates a Receiver object
    ex: semit = Emmiter('D13')
    """
    def __init__(self, pinid: str):
        self.pin = digitalio.DigitalInOut(get_pin_definition(pinid))
        self.pin.direction = digitalio.Direction.OUTPUT
        self.id = pinid

    def turnoff(self, pausa: float = 0.1):
        """
        Turns off the Emitter
        :param pausa: time in seconds for the Emitter to be OFF
        :return: None
        """
        self.pin.value = False
        time.sleep(pausa)

    def turnon(self, pausa: float = 0.1):
        """
        Turns on the Emitter
        :param pausa: time in seconds for the Emitter to be ON
        :return: None
        """
        self.pin.value = True
        time.sleep(pausa)

    def flashing(self, ontime: float, offtime: float, repeat: int):
        """
        Flash the led according to given parameters
        :param ontime: time in seconds for the Emitter to be ON
        :param offtime: time in seconds for the Emitter to be OFF
        :param repeat: number of repetitions
        :return: None
        """
        for _ in range(repeat):
            self.turnon(ontime)
            self.turnoff(offtime)

    def blinking(self, blinktime: int):
        """
        :param blinktime: duration in seconds
        :return: None
        """
        self.turnon(blinktime)
        self.turnoff(blinktime)

    def pattern(self, patternl: List[int]) -> None:
        """
        Converts a list of values [0 or 1] to an output in the Emitter
        :param patternl: list of [0-1] values
        :return: None
        ex: led = Emitter('D2')
        codigo = [1,1,0,1,0,0,1,1,1,0,0,1,1,0,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,0,0,0,1,1,1,0,0,0,0,1,1,1,1,0,0,0,1]
        led.pattern(codigo)
        """
        for item in patternl:
            if item == 1:
                self.turnon()
            elif item == 0:
                self.turnoff()
            else:
                continue

    def randomblink(self, iterl: int) -> None:
        """
        Emits a random output to the Emitter
        :param iterl: number of values to be randomly generated
        :return: None
        """
        self.pattern([randint(0, 1) for _ in range(iterl)])
        self.turnoff()

    @staticmethod
    def convletter(letter: str, final: str) -> str:
        """
        Converts a letter to its representation in morse code
        :param letter: Letter to be converted
        :param final: Final character encoding
        :return: string representation in morse code
        >>> Emitter('D5').convletter('a', '|')
        '.*-|'
        """

        morsetabs = {
            'A': '.-', 'a': '.-',
            'B': '-...', 'b': '-...',
            'C': '-.-.', 'c': '-.-.',
            'D': '-..', 'd': '-..',
            'E': '.', 'e': '.',
            'F': '..-.', 'f': '..-.',
            'G': '--.', 'g': '--.',
            'H': '....', 'h': '....',
            'I': '..', 'i': '..',
            'J': '.---', 'j': '.---',
            'K': '-.-', 'k': '-.-',
            'L': '.-..', 'l': '.-..',
            'M': '--', 'm': '--',
            'N': '-.', 'n': '-.',
            'O': '---', 'o': '---',
            'P': '.--.', 'p': '.--.',
            'Q': '--.-', 'q': '--.-',
            'R': '.-.', 'r': '.-.',
            'S': '...', 's': '...',
            'T': '-', 't': '-',
            'U': '..-', 'u': '..-',
            'V': '...-', 'v': '...-',
            'W': '.--', 'w': '.--',
            'X': '-..-', 'x': '-..-',
            'Y': '-.--', 'y': '-.--',
            'Z': '--..', 'z': '--..',
            '0': '-----', ',': '--..--',
            '1': '.----', '.': '.-.-.-',
            '2': '..---', '?': '..--..',
            '3': '...--', ';': '-.-.-.',
            '4': '....-', ':': '---...',
            '5': '.....', "'": '.----.',
            '6': '-....', '-': '-....-',
            '7': '--...', '/': '-..-.',
            '8': '---..', '(': '-.--.-',
            '9': '----.', ')': '-.--.-',
            ' ': ' ', '_': '..--.-',
            '!': '-·-·--'
        }

        convletter = morsetabs[letter]
        convertedletter = ''
        fin = len(convletter) - 1
        for ind, symbol in enumerate(convletter):
            if ind == fin:
                convertedletter = convertedletter + symbol + final
            else:
                convertedletter = convertedletter + symbol + '*'

        return convertedletter

    def convertword(self, word: str) -> str:
        """
        Convert a word to its representation in morse code
        :param word: word string
        :return: string of morse code
        """
        worklist = ''
        fin = len(word) - 1
        for ile, letter in enumerate(word):
            if ile == fin:
                worklist = worklist + self.convletter(letter, '#')
            else:
                worklist = worklist + self.convletter(letter, '|')
        return worklist

    def convertphrase(self, phrase: str) -> List[str]:
        """
        Convert a phrase to a list of words converted to morse code.  We use a list to allow the library
        do some threading methods
        :param phrase: string to be converted to morse code
        :return: list of words converted to morse code
        """
        phrase = phrase.split(' ')
        phraselist = []
        for word in phrase:
            phraselist.append(self.convertword(word))
        return phraselist

    def outmorse(self, phrase: str, duration: float = 0.1) -> None:
        """
        Plays the morse code
        :param phrase:
        :param duration: This value hods the logic of the morse code wpm(words per minute)
                         In this case we use 0.1 that means that we use 120/0.12
        :return: None
        """
        codes = self.convertphrase(phrase)
        for word in codes:
            for symbol in word:
                if symbol == '*':
                    self.turnoff(duration)
                elif symbol == '.':
                    self.turnon(duration)
                elif symbol == '-':
                    self.turnon(duration * 3)
                elif symbol == '|':
                    self.turnoff(duration * 3)
                elif symbol == '#':
                    self.turnoff(duration * 7)

    def convertbpm(self, bpm):
        """
        Converts beats per minute in light output
        :param bpm:
        :return: None
        """
        divider = 60 / bpm
        for _ in range(150):
            self.blinking(divider / 2)
        self.turnoff()

    def __str__(self):
        return r'Sensor is using IO number: {}'.format(self.id)


class LedRGB(object):
    """
    Creates a RGBLed Object
    use:
    rgbled1 = LedRGB(1)
    """
    def __init__(self, pinidr: str, pinidg: str, pinidb: str):
        """
        :param pinidr: pin number of the red terminal in the led
        :param pinidg: pin number of the green terminal in the led
        :param pinidb: pin number of the blue terminal in the led
        """
        self.pinred = pulseio.PWMOut(get_pin_definition(pinidr), frequency=5000, duty_cycle=0)
        self.pingreen = pulseio.PWMOut(get_pin_definition(pinidg), frequency=5000, duty_cycle=0)
        self.pinblue = pulseio.PWMOut(get_pin_definition(pinidb), frequency=5000, duty_cycle=0)
        self.components = [self.pinred, self.pingreen, self.pinblue]

    def turnoff(self, pausa: float = 0.1):
        """
        Turns off the RGBLED
        :param pausa: time in seconds for the Emitter to be OFF
        :return: None
        """
        for pin in self.components:
            pin.duty_cycle = 0
        time.sleep(pausa)

    def turnon(self, pausa: float = 0.1):
        """
        Turns on the RGBLED
        :param pausa: time in seconds for the Emitter to be ON
        :return: None
        """
        for pin in self.components:
            pin.duty_cycle = 65000
        time.sleep(pausa)

    def updatered(self, duty: int):
        """
        Changes the duty cycle of the red part of the RGBLED
        :param duty: [0-100] porcentage of the brightness
        :return: None
        """
        self.components[0].duty_cycle = int(duty * 65000 / 100)

    def updategreen(self, duty: int):
        """
        Changes the duty cycle of the green part of the RGBLED
        :param duty: [0-100] porcentage of the brightness
        :return: None
        """
        self.components[1].duty_cycle = int(duty * 65000 / 100)

    def updateblue(self, duty: int):
        """
        Changes the duty cycle of the blue part of the RGBLED
        :param duty: [0-100] porcentage of the brightness
        :return: None
        """
        self.components[2].duty_cycle = int(duty * 65000 / 100)

    def wheel(self, pos):
        # Input a value 0 to 255 to get a color value.
        # The colours are a transition r - g - b - back to r.
        if pos < 0 or pos > 255:
            return 0, 0, 0
        if pos < 85:
            return int(255 - pos * 3), int(pos * 3), 0
        if pos < 170:
            pos -= 85
            return 0, int(255 - pos * 3), int(pos * 3)
        pos -= 170
        return int(pos * 3), 0, int(255 - (pos * 3))

    def convertrgb(self, rgbcolor: tuple):
        red, green, blue = rgbcolor
        factor = 100 / 255
        self.updatered(red * factor)
        self.updategreen(green * factor)
        self.updateblue(blue * factor)


class ReedSensor(object):
    """
    Creates a Reedsensor object
    Use:
    resensor = ReedSensor('D3')
    """
    def __init__(self, pinid: str):
        self.pin = digitalio.DigitalInOut(get_pin_definition(pinid))
        self.pin.direction = digitalio.Direction.INPUT
        self.pin.pull = Pull.UP

    def state(self):
        """
        :return: State of the Sensor
        """
        time.sleep(0.05)
        return self.pin.value


class Internet(object):
    def __init__(self):
        """
        creates a internet connection
        """
        wifi.radio.connect(secrets["ssid"], secrets["password"])
        pool = socketpool.SocketPool(wifi.radio)
        self.http = adafruit_requests.Session(pool, ssl.create_default_context())
        print('Connected')

    def test(self):
        """
        Test connection of the board to internet
        :return: json file to print
        """
        json_url = "http://api.coindesk.com/v1/bpi/currentprice/USD.json"
        r = self.http.get(json_url)
        return r.json()

    @staticmethod
    def getip():
        """
        Get IP address of the board
        :return: IP address
        """
        return wifi.radio.ipv4_address


class Led(object):
    """
    Creates a LED emitter
    """

    def __init__(self, pinid: int):
        """
        :param pinid: npin number according to the BCM logic
        """
        self.brgtset = False
        self.pin = pulseio.PWMOut(get_pin_definition(pinid), frequency=5000, duty_cycle=0)

    def turnoff(self, pausa: float = 0.1):
        """
        Turns off the LED
        :param pausa: time in seconds for the Emitter to be OFF
        :return: None
        """
        self.pin.duty_cycle = 0
        time.sleep(pausa)

    def turnon(self, pausa: float = 0.1):
        """
        Turns on the LED
        :param pausa: time in seconds for the Emitter to be ON
        :return: None
        """
        self.pin.duty_cycle = 65000
        time.sleep(pausa)


class Buzzer(object):
    def __init__(self, pinid):
        self.pin = get_pin_definition(pinid)
        self.buzzy = pulseio.PWMOut(self.pin, frequency=440, duty_cycle=0, variable_frequency=True)
        self.notas = {'S':5, 'C': 262, 'D': 294, 'E': 330, 'F': 349, 'G': 392, 'a': 440, 'b': 494}

    def playtone(self, cancion):
        for nota in cancion:
            self.buzzy.frequency = self.notas[nota]
            self.buzzy.duty_cycle = 65535 // 2  # On 50%
            time.sleep(0.25)
            self.buzzy.duty_cycle = 0  # Off
            time.sleep(0.05)  # Pause between notes


class DHT11(object):
    """
    Creates a temperature object DHT11
    """
    def __init__(self, pinid):
        """
        :param pinid: pin number of the sensor according to the BCM logic
        """
        self.pin = get_pin_definition(pinid)
        self.dhtsensor= adafruit_dht.DHT11(self.pin)

    def dhtdata(self):
        return self.dhtsensor.temperature, self.dhtsensor.humidity


class Pantalla(object):
    """
    Creates a screen object for the SSD1306 OLED Display
    """
    def __init__(self):
        oled_reset = board.D9
        displayio.release_displays()
        self.display_bus = displayio.I2CDisplay(board.I2C(), device_address=0x3C, reset=oled_reset)
        self.display = adafruit_displayio_ssd1306.SSD1306(self.display_bus, width=128, height=32)

    def showtextoled(self, textop):
        splash = displayio.Group(max_size=10)
        self.display.show(splash)

        color_bitmap = displayio.Bitmap(128, 32, 1)
        color_palette = displayio.Palette(1)
        color_palette[0] = 0xFFFFFF  # White

        bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
        splash.append(bg_sprite)

        # Draw a smaller inner rectangle
        inner_bitmap = displayio.Bitmap(118, 24, 1)
        inner_palette = displayio.Palette(1)
        inner_palette[0] = 0x000000  # Black
        inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=5, y=4)
        splash.append(inner_sprite)

        # Draw a label
        longeur  = int(len(textop)*5/2)
        text_area = label.Label(terminalio.FONT, text=textop, color=0xFFFF00, x=59-longeur, y=15)
        splash.append(text_area)


class Screen(object):
    """
    Creates a screen for the WIO Terminal
    """
    def __init__(self):
        self.display = board.DISPLAY
        self.WIDTH = 320
        self.HEIGHT = 240  # Change to 64 if needed
        self.BORDER = 5

    def showtextoled(self, textop):
        splash = displayio.Group(max_size=10)
        self.display.show(splash)

        color_bitmap = displayio.Bitmap(self.WIDTH, self.HEIGHT, 1)
        color_palette = displayio.Palette(1)
        color_palette[0] = 0xFFFFFF  # White

        bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
        splash.append(bg_sprite)

        # Draw a smaller inner rectangle
        inner_bitmap = displayio.Bitmap(self.WIDTH - self.BORDER * 2, self.HEIGHT - self.BORDER * 2, 1)
        inner_palette = displayio.Palette(1)
        inner_palette[0] = 0x000000  # Black
        inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=self.BORDER, y=self.BORDER)
        splash.append(inner_sprite)

        # Draw a label
        text_area = label.Label(terminalio.FONT, text=textop, color=0xFF00FF, x=28, y=self.HEIGHT // 2 - 1, scale=3)
        splash.append(text_area)
        self.display.show(splash)


class Tempsensor1820(object):
    def __init__(self, pin):
        # Initialize one-wire bus on board pin D5.
        ow_bus = OneWireBus(board.D0)
        self.ds18 = DS18X20(ow_bus, ow_bus.scan()[0])

    def get_temp(self):
        time.sleep(1)
        return self.ds18.temperature

