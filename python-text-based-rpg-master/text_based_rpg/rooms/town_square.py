from .. import interface
from ..util import move
from ..room import Room

map_ = """You are in the class.
To the east is the center of the class, from where Daniel and Nikita are.
Goneril Mountain looms in the distance."""

def enter(room, player):
    if room.has_been_entered_before:
        interface.print_multiple_lines(
            lines=[
                "You are in the middle in class.",
                "Normally it would be buzzing with classmates, but as everyone is currently busy being scared of the exam, it is deserted."
            ],
            delay=4
        )
    else:
        room.has_been_entered_before = True

        interface.print_multiple_lines(
            lines=[
                "You are in the middle of class.",
                "Normally it would be buzzing with classmates, but as everyone is currently busy being scared of the exam, it is deserted.",
                "Except, for a confused student sitting on an uncomfortable chair, crying."
            ],
            delay=4
        )

    while True:
        additional_commands = ["talk"]

        if player.talked_to_cordelia:
            additional_commands = ["move"]

        command = interface.get_game_command(
            player,
            room,
            additional_commands
        )

        if command == "talk":
            npc = interface.get_command(
                ["student", "cancel"],
                True
            )

            if npc == "student":
                interface.print_multiple_lines(
                    lines=[
                        "You slowly approach the student.",
                        "\"Are you the new student?\" you ask sheepishly.",
                        "\"I saw it! It was a Quizlet! I'm not insane!\"",
                        "\"What did you see?\" you ask, intrigued.",
                        "\"I saw a 105 term Quizlet!\"",
                        "\"What did it look like?\"",
                        "\"It...wasn't on schoology, but it was on my reccomended sets. It had too many terms!\"",
                        "\"Oh please, you have to help us! The exam have been tormenting us for weeks now!\"",
                        "\"Life in class is usually so peaceful...\"",
                        "She bursts into tears and runs away before you can ask further questions.",
                        "Your path is clear to you now: you must get to the bottom of these supernatural occurances.",
                        "You should stop by Nikita."
                    ],
                    delay=4
                )
                interface.print_()
                player.talked_to_cordelia = True
        else:
            place_to_move = move(["middle of class"])

            if place_to_move == "middle of class":
                from .center_of_town import room as center_of_town
                center_of_town.enter(player)

room = Room(
    map_=map_,
    enter=enter
)
