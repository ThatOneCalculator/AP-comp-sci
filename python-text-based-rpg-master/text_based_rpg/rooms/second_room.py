from .. import interface, enemies, items
from ..util import move, GameOver
from ..room import Room
from ..battle import Battle
import winsound
import random
map_ = """You are at the second set of desks before the whiteboard.
It is deserted, for no students dare to sit there.
Only the whiteboard remains.
The first set of desks and the outside are behind you."""

def enter(room, player):
    winsound.PlaySound("text_based_rpg/mus/GALLERY.wav", winsound.SND_FILENAME +winsound.SND_ASYNC + winsound.SND_LOOP)
    if room.has_been_entered_before:
        interface.print_multiple_lines(
            lines=map_.split("\n"),
            delay=4
        )
    else:
        room.has_been_entered_before = True

        interface.print_multiple_lines(
            lines=[
                "You enter the desks.",
                "You see her."
                "Kuper."
                "You know what you must do."

            ],
            delay=4
        )
        winsound.PlaySound(None, winsound.SND_PURGE)
        secret=Random.randint(1,10)
        if secret==1:
            winsound.PlaySound("text_based_rpg/mus/Secret1.wav", winsound.SND_FILENAME + winsound.SND_ASYNC + winsound.SND_LOOP)
            print("Get ready for the fight of your life. Let's go./n/n")
        elif secret==2 or secret==3:
            winsound.PlaySound("text_based_rpg/mus/Secret2.wav",winsound.SND_FILENAME + winsound.SND_ASYNC + winsound.SND_LOOP)
            print("You feel your bad grades rolling down your back. /n/n")
        elif secret==4 or secret==5:
            winsound.PlaySound("text_based_rpg/mus/Secret3.wav",winsound.SND_FILENAME + winsound.SND_ASYNC + winsound.SND_LOOP)
            print("\"It's kill or be killed,\" they said. You're filled with determination.")
        else:
            winsound.PlaySound("text_based_rpg/mus/FinalBoss.wav",winsound.SND_FILENAME + winsound.SND_ASYNC + winsound.SND_LOOP)
            print("You hear Kuper utter the words, \"I can do anything.\". You know you're gonna have a bad time.")
    while True:
        additional_commands = ["attack"]

        if player.second_boss_defeated:
            additional_commands = ["move"]

        command = interface.get_game_command(player, room, additional_commands)

        if command == "attack":
            target = interface.get_command(["kuper", "cancel"], True)

            if target == "kuper":
                battle = Battle(player, enemies.second_boss())
                battle.run()

                player.second_boss_defeated = True
                interface.sleep(5)
                interface.print_()

                interface.print_multiple_lines(
                    lines=[
                        "You have defeated Ms. Kuper.",
                        "You are now able to get to the whiteboard and retrieve the documents."
                    ],
                    delay=4
                )

        if command == "move":
            place_to_move = move(["first set of desks", "whiteboard"])

            if place_to_move == "first set of desks":
                from .first_room import room as first_room
                first_room.enter(player)

            if place_to_move == "whiteboard":
                raise GameOver

room = Room(
    map_=map_,
    enter=enter
)
