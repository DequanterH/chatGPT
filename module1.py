from gpiozero import Button
import time

# Definieer de GPIO-pinnen waarop de knoppen zijn aangesloten
button_pin_1 = 17
button_pin_2 = 18

# Maak Button-objecten voor elke knop
button_1 = Button(button_pin_1)
button_2 = Button(button_pin_2)

# Definieer de acties die moeten worden uitgevoerd wanneer de knoppen worden ingedrukt
def button_1_pressed():
    print("Button 1 pressed")

def button_2_pressed():
    print("Button 2 pressed")

# Wijs de acties toe aan de knoppen
button_1.when_pressed = button_1_pressed
button_2.when_pressed = button_2_pressed

# Houd het script actief
try:
    while True:
        time.sleep(0.1)  # Voorkomt dat de CPU te veel wordt belast
except KeyboardInterrupt:
    pass

