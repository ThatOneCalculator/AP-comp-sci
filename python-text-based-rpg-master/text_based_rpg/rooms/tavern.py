from .. import interface
from ..util import move
from ..room import Room

map_ = """You are at Daniel's seat."""

def enter(room, player):
    talked_to_daniel = False
    talked_to_strange_person = False

    if room.has_been_entered_before:
        interface.print_multiple_lines(
            lines=[
                "You are at Daniel's seat. He's in a suit.",
                "He is still bored, and the strange person in the corner is the same as usual."
            ],
            delay=7
        )
    else:
        interface.print_multiple_lines(
            lines=[
                "You show up to 7th period."
                " You don't know where to sit."
                " You see Daniel sitting near a weird kid whose name you don't know how to say or spell."
                " You approach Daniel."
            ],
            delay=7
        )

    while True:
        additional_commands = ["talk"]

        if (
                room.has_been_entered_before or \
                (talked_to_daniel and talked_to_strange_person)
        ):
            additional_commands = ["move"]

        command = interface.get_game_command(player, room, additional_commands)

        if command == "talk":
            npc = interface.get_command(
                ["daniel", "person in corner", "cancel"],
                True
            )

            if npc == "person in corner":
                interface.print_multiple_lines(
                    lines=[
                        "You cautiously approach the strange person standing in the corner.",
                        "They sense you coming, and slowly turn around.",
                        "Their expression is blank and lifeless.",
                        "They utter, in an emotionless voice:",
                        "\"M y   c o d e   i s   j u s t   f i n e.\"",
                        "They turn back around. You think it's best not to try and make further conversation.",
                    ],
                    delay=4
                )
                interface.print_()
                talked_to_strange_person = True

            if npc == "daniel":
                interface.print_multiple_lines(
                    lines=[
                        "You approach Daniel.",
                        "He looks up at you again. He is still just as bored, and upon further inspection, looks rather down.",
                        "\"Where is everyone?\" you ask as you sit down on one of the uncomfortable chairs.",
                        "\"There's an exam coming up.\"",
                        "\"Why is that?\" you ask, worried.",
                        "\"Kuper is relentless.\"",
                        "Daniel must be able to tell that you're excited, as he says \"A classmate, are we? Your like don't come around these parts very often.\"",
                        "\"A new student came in here crying a few hours ago, saying she'd seen a Quizlet of sorts. I think I saw her run towards the middle of class. If you want to investigate, you should go talk to her.\"",
                        "\"If you could get to the bottom of this, you would do all of us a great service.\""
                    ],
                    delay=4
                )
                interface.print_()
                talked_to_daniel = True
        else:
            place_to_move = move(["rest of classroom"])

            if place_to_move == "rest of classroom":
                room.has_been_entered_before = True
                from .center_of_town import room as center_of_town
                center_of_town.enter(player)

room = Room(
    map_=map_,
    enter=enter
)
