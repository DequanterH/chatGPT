import board
import busio
import digitalio
from adafruit_rgb_display import color565
import adafruit_rgb_display.ili9341 as ili9341
import adafruit_touchscreen

# Configureer SPI-communicatie voor het touchscreen en het display
spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI, MISO=board.MISO)
tft_cs = digitalio.DigitalInOut(board.CE0)
tft_dc = digitalio.DigitalInOut(board.D25)
touch_cs = digitalio.DigitalInOut(board.CE1)

# Maak een schermobject voor het ILI9341-display
display = ili9341.ILI9341(spi, cs=tft_cs, dc=tft_dc)

# Maak een touchscreenobject
touch = adafruit_touchscreen.Touchscreen(spi, touch_cs)

# Hoofdloop voor het lezen van aanraakgegevens en uitvoeren van acties
while True:
    touch_point = touch.touch_point
    if touch_point is not None:
        x, y = touch_point
        # Voer hier acties uit op basis van de aanraakgebeurtenis
        print("Touched at ({0}, {1})".format(x, y))

