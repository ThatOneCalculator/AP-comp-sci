from .. import interface, enemies, items
from ..util import move
from ..room import Room
from ..battle import Battle

map_ = """You are in the circle of desks before the whiteboard.
There is another circle past this one, and then the final chamber.
Outside is the entrace to the front of class and the middle of the class."""

def enter(room, player):
    if room.has_been_entered_before:
        interface.print_multiple_lines(
            lines=[
                "You are at in the first circle of desks behind the whiteboard.",
                "It is very dark, and very eery."
            ],
            delay=4
        )
    else:
        room.has_been_entered_before = True

        interface.print_multiple_lines(
            lines=[
                "You enter the first circle of desks behind the whiteboard.",
                "There is a large computer, presumably leading to the room after this one.",
                "However, it has a password.",
                "To the side of the desks, there is a chest.",
                "You figure the chest contains the key.",
                "However, there is Kerria blocking the path to it.",
                "To open the chest and get the key, you will have to deal with Kerria."
            ],
            delay=4
        )

    while True:
        additional_commands = ["attack"]

        if player.first_boss_defeated:
            additional_commands = ["move"]

        command = interface.get_game_command(player, room, additional_commands)

        if command == "attack":
            target = interface.get_command(["Kerria", "cancel"], True)

            if target == "Kerria":
                battle = Battle(player, enemies.first_boss())
                battle.run()

                player.first_boss_defeated = True
                interface.sleep(5)
                interface.print_()

                interface.print_multiple_lines(
                    lines=[
                        "Opening the chest, you find the comically large key for the comically large lock.",
                        "You unlock the door, allowing you to progress to the next room.",
                        "In the chest you also find better versions of your current equipment."
                    ],
                    delay=4
                )

                if player.class_ == "warrior":
                    print("Check your inventory")

                    player.inventory.extend([
                        items.steel_sword,
                        items.steel_helmet,
                        items.steel_breastplate,
                        items.steel_platelegs
                    ])

                if player.class_ == "archer":
                    print("Check your inventory")

                    player.inventory.extend([
                        items.willow_bow,
                        items.Kerria_hide_body,
                        items.Kerria_hide_legs
                    ])

                if player.class_ == "mage":
                    print("Check your inventory")

                    player.inventory.extend([
                        items.fire_staff,
                        items.battle_hood,
                        items.battle_robe
                    ])

        if command == "move":
            place_to_move = move(["outside", "second room"])

            if place_to_move == "outside":
                from .mountain_exterior import room as mountain_exterior
                mountain_exterior.enter(player)

            if place_to_move == "second circle of desks":
                from .second_room import room as second_room
                second_room.enter(player)

room = Room(
    map_=map_,
    enter=enter
)
