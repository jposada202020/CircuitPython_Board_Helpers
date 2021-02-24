import displayio
import busio
import board
from adafruit_displayio_ssd1306 import SSD1306

i2c = busio.I2C(board.GP3, board.GP2)

displayio.release_displays()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = SSD1306(display_bus, width=128, height=32)

splash = displayio.Group(max_size=10)
display.show(splash)

color_bitmap = displayio.Bitmap(128, 32, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF  # White

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=1, y=1)
splash.append(bg_sprite)

inner_bitmap = displayio.Bitmap(118, 24, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000  # Black
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=5, y=4)
splash.append(inner_sprite)

longeur  = int(len(textop)*5/2)
text_area = label.Label(terminalio.FONT, text=textop, color=0xFFFF00, x=59-longeur, y=15)
splash.append(text_area)

while True:
    pass
