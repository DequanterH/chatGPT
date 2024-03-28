import curses
import time
import speech_recognition as sr
import time

# Maak een herkenningsinstantie
recognizer = sr.Recognizer()

# Initialiseren van de curses module
stdscr = curses.initscr()
curses.curs_set(0)  # Verberg de cursor
stdscr.keypad(True)  # Zet de keypad-modus aan

# Schermgrootte
HEIGHT, WIDTH = 12, 10

# Tekens voor het mannetje en de lege ruimte
CHARACTER = 'M'
EMPTY_SPACE = '.'

# Positie van het mannetje
character_x = WIDTH // 2
character_y = HEIGHT // 2

# Variabele voor de gesproken tekst
spoken_text = ""

# Functie om het scherm bij te werken
def update_screen():
    stdscr.clear()
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if x == character_x and y == character_y:
                stdscr.addstr(CHARACTER)
            else:
                stdscr.addstr(EMPTY_SPACE)
        stdscr.addstr('\n')
    
    # Voeg de gesproken tekst onderaan het scherm toe
    stdscr.addstr(HEIGHT + 1, 0, "handlijding: naar links, naar recht, naar boven en naar benden, gesproken tekst: " + spoken_text)
    stdscr.refresh()

# Main loop
while True:
    update_screen()  # Bijwerken van het scherm binnen de lus

    # Opnemen van audio vanaf de microfoon
    with sr.Microphone() as source:
        print("Zeg iets...")
        audio = recognizer.listen(source)

    try:
        # Probeer de gesproken woorden om te zetten in tekst
        text = recognizer.recognize_google(audio, language='nl-NL')
        print("Gesproken tekst: " + text)
        spoken_text = text  # Bewaar de gesproken tekst voor weergave op het scherm
        
        # Beweeg het mannetje op basis van de gesproken tekst
        if text == "naar boven":
            character_y = max(0, character_y - 1)
        elif text == "naar beneden":
            character_y = min(HEIGHT - 1, character_y + 1)
        elif text == "naar links":
            character_x = max(0, character_x - 1)
        elif text == "naar rechts":
            character_x = min(WIDTH - 1, character_x + 1)
        elif text != "naar links":
            time.sleep(1)

        
    except sr.UnknownValueError:
        print("Kan spraak niet herkennen")
    except sr.RequestError as e:
        print("Fout bij het verwerken van de spraakherkenning: {0}".format(e))
    
    time.sleep(0.1)
    
    # Sluit curses af binnen de while-lus
    curses.endwin()
