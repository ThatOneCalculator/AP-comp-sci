from text_based_rpg import interface
from text_based_rpg.start_game import start_game

PLAY = "play"
HELP = "help"
QUIT = "quit"
COMMANDS = [PLAY, HELP, QUIT]

def play():
    while True:
        interface.print_("Welcome to my text-based RPG, all about our class.\n")

        interface.print_("Enter " + interface.generate_readable_list(COMMANDS))
        command = interface.get_command(COMMANDS)

        if command == PLAY:
            start_game()

        if command == HELP:
            print("Made by Kainoa Kanter in Python. Read \"readme.txt\" in the master folder for more help.")

        if command == QUIT:
            break
