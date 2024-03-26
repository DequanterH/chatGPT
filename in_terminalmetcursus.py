import curses

# Initialiseren van de curses module
stdscr = curses.initscr()
curses.curs_set(0)  # Verberg de cursor
stdscr.keypad(True)  # Zet de keypad-modus aan

# Schermgrootte
HEIGHT, WIDTH = 10, 10

# Tekens voor het mannetje en de lege ruimte
CHARACTER = 'M'
EMPTY_SPACE = '.'

# Positie van het mannetje
character_x = WIDTH // 2
character_y = HEIGHT // 2

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
    stdscr.refresh()

# Main loop
while True:
    update_screen()

    # Wacht op gebruikersinvoer
    key = stdscr.getch()

    # Verwerk de invoer
    if key == curses.KEY_UP:
        character_y = max(0, character_y - 1)
    elif key == curses.KEY_DOWN:
        character_y = min(HEIGHT - 1, character_y + 1)
    elif key == curses.KEY_LEFT:
        character_x = max(0, character_x - 1)
    elif key == curses.KEY_RIGHT:
        character_x = min(WIDTH - 1, character_x + 1)
    elif key == ord('q'):
        break  # Stop de loop als de gebruiker 'q' indrukt

# Beëindig curses
curses.endwin()

