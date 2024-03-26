import speech_recognition as sr
import tkinter as tk
import time

# Maak een herkenningsinstantie
recognizer = sr.Recognizer()

# Maak een tkinter venster
root = tk.Tk()
root.title("Bewegend Mannetje")

# Maak een canvas
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Teken het mannetje
character = canvas.create_rectangle(180, 180, 220, 220, fill="blue")

# Oneindige lus voor continu opnemen van audio
while True:
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
            canvas.move(character, 0, -100)
        elif text == "naar beneden":
            canvas.move(character, 0, 100)
        elif text == "naar links":
            canvas.move(character, -100, 0)
        elif text == "naar rechts":
            canvas.move(character, 100, 0)

    except sr.UnknownValueError:
        print("Kan spraak niet herkennen")
    except sr.RequestError as e:
        print("Fout bij het verwerken van de spraakherkenning: {0}".format(e))
    
    time.sleep(2)

    # Voer de main loop uit
    root.update_idletasks()
    root.update()
