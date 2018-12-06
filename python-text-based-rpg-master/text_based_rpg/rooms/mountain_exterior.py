from .. import interface, enemies
from ..util import move
from ..room import Room
from ..battle import Battle

map_ = """You can see the whiteboard.
To the south is the middle of class."""

def enter(room, player):
    if room.has_been_entered_before:
        interface.print_multiple_lines(
            lines=[
                "You are at the entrace to the whiteboard.",
                "Besides for the hum of computer fans, it is quiet."
            ],
            delay=4
        )
    else:
        room.has_been_entered_before = True

        interface.print_multiple_lines(
            lines=[
                "You have left the center of class and are walking through the classroom towards the whiteboard.",
                "Besides for the hum of computer fans, it is quiet.",
                "As you are climbing over some desks, you fail to see a normal student working behind them.",
                "You disrupt him, mildly annoying him."
            ],
            delay=4
        )

        battle = Battle(player, enemies.bear())
        battle.run()

        interface.sleep(5)
        interface.print_()
        
        interface.print_multiple_lines(
            lines=[
                "Finally, you are at the entrace to the desks before the whiteboard.",
                "Besides for the hum of computer fans, it is quiet."
            ],
            delay=4
        )

    while True:
        command = interface.get_game_command(player, room, ["move"])

        place_to_move = move(["back to class", "desks near whiteboard"])

        if place_to_move == "back to class":
            from .center_of_town import room as center_of_town
            center_of_town.enter(player)

        if place_to_move == "desks near whiteboard":
            from .first_room import room as first_room
            first_room.enter(player)

room = Room(
    map_=map_,
    enter=enter
)
