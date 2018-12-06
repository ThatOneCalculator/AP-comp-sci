from .. import interface
from ..util import move
from ..room import Room

map_ = """You are out in the class.
To your west is the middle of class.
To the east is Nikita.
To the south is Daniel.
The whiteboard looms to the north."""

def enter(room, player):
    interface.print_multiple_lines(lines=map_.split("\n"), delay=1)

    while True:
        interface.get_game_command(player, room, ["move"])

        places_to_move = ["daniel", "middle of class"]

        if player.talked_to_cordelia:
            places_to_move.append("nikita")

        if player.can_progress_to_mountain:
            places_to_move.append("whiteboard")

        move_location = move(places_to_move)

        if move_location == "daniel":
            from .tavern import room as tavern
            tavern.enter(player)

        if move_location == "middle of class":
            from .town_square import room as town_square
            town_square.enter(player)

        if move_location == "nikita":
            from .shop import room as shop
            shop.enter(player)

        if move_location == "whiteboard":
            from .mountain_exterior import room as mountain_exterior
            mountain_exterior.enter(player)

room = Room(
    map_=map_,
    enter=enter
)
