import speech_recognition as sr
import pygame
import time

# Initialiseren van Pygame
pygame.init()

# Vensterinstellingen
WIDTH, HEIGHT = 320, 240
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bewegend Mannetje")

# Kleuren
BLUE = (0, 0, 255)

# Maak een herkenningsinstantie
recognizer = sr.Recognizer()

# Teken het mannetje
character = pygame.Rect(180, 180, 40, 40)

# Oneindige lus voor continu opnemen van audio
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Opnemen van audio vanaf de microfoon
    with sr.Microphone() as source:
        print("Zeg iets...")
        audio = recognizer.listen(source)

    try:
        # Probeer de gesproken woorden om te zetten in tekst
        text = recognizer.recognize_google(audio, language='nl-NL')
        print("Gesproken tekst: " + text)
        
        # Beweeg het mannetje op basis van de gesproken tekst
        if text == "naar boven":
            character.y -= 100
        elif text == "naar beneden":
            character.y += 100
        elif text == "naar links":
            character.x -= 100
        elif text == "naar rechts":
            character.x += 100

    except sr.UnknownValueError:
        print("Kan spraak niet herkennen")
    except sr.RequestError as e:
        print("Fout bij het verwerken van de spraakherkenning: {0}".format(e))
    
    # Teken het mannetje op het scherm
    WINDOW.fill((0, 0, 0))
    pygame.draw.rect(WINDOW, BLUE, character)
    pygame.display.update()

    # Pauzeer voor 2 seconden
    time.sleep(2)

pygame.quit()

