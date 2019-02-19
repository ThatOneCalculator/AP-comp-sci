from .. import interface, items
from ..util import move
from ..room import Room
import winsound
map_ = """You are at Nikita.
You see the whiteboard in the distance"""
def enter(room, player):
    winsound.PlaySound(None, winsound.SND_PURGE)
    winsound.PlaySound("text_based_rpg/mus/tem.wav", winsound.SND_ASYNC)
    if room.has_been_entered_before:
        interface.print_multiple_lines(
            lines=[
                "You are at Nikita's seat.",
                "No one's sitting next to him."
            ],
            delay=4
        )
    else:
        room.has_been_entered_before = True

        interface.print_multiple_lines(
            lines=[
                "You tell Nikita \"hi\".",
                "He seems to have some stuff in his backpack.",
            ],
            delay=4
        )

    while True:
        additional_commands = ["talk"]

        if player.can_progress_to_mountain:
            additional_commands = ["move"]

        command = interface.get_game_command(
            player,
            room,
            additional_commands
        )

        if command == "talk":
            npc = interface.get_command(
                ["nikita", "cancel"],
                True
            )

            if npc == "nikita":
                interface.print_multiple_lines(
                    lines=[
                        "You approach him.",
                        "He turns around.",
                        "\"COMMUNISM! Want some stuff?\" he says",
                        "Sure, you say",
                        "\"That whiteboard may hold the clue to the exam coming up, and maybe even some stuff about the student samples and documents\"",
                        "\"Take some stuff!\"",
                        "You thank him.",
                        "You can hear him screaming about how the bourgosie is exploiting the proliterat as you walk away",
                    ],
                    delay=4
                )

                if player.class_ == "Zenon":
                    interface.print_multiple_lines(
                        lines=[
                            "Oh, here you go!"
                            "Check your inventory"
                        ],
                        delay=4
                    )

                    player.inventory.extend([
                        items.iron_sword,
                        items.iron_helmet,
                        items.iron_breastplate,
                        items.iron_platelegs
                    ])

                if player.class_ == "Caleb":
                    interface.print_multiple_lines(
                        lines=[
                            "Oh, here you go!"
                            "Check your inventory"
                        ],
                        delay=4
                    )

                    player.inventory.extend([
                        items.oak_bow,
                        items.cow_hide_body,
                        items.cow_hide_legs
                    ])

                if player.class_ == "Kainoa":
                    interface.print_multiple_lines(
                        lines=[
                            "Oh, here you go!"
                            "Check your inventory"
                        ],
                        delay=4
                    )

                    player.inventory.extend([
                        items.ice_staff,
                        items.hood,
                        items.robe
                    ])

                interface.print_multiple_lines(
                    lines=[
                        "\"You're also going to need some potions!\"",
                        "Three health potions have been added to your inventory."
                    ],
                    delay=4
                )

                for _ in range(3):
                    player.inventory.append(items.health_potion())

                if player.class_ in ["warrior", "archer"]:
                    interface.print_("Three stamina potions have been added to your inventory.")

                    for _ in range(3):
                        player.inventory.append(items.stamina_potion())
                else:
                    interface.print_("Three mana potions have been added to your inventory.")

                    for _ in range(3):
                        player.inventory.append(items.mana_potion())

                interface.print_("Use the \"use item\" command to use them if you need them.")

                interface.print_()
                player.can_progress_to_mountain = True
        else:
            place_to_move = move(["outside"])

            if place_to_move == "outside":
                from .center_of_town import room as center_of_town
                center_of_town.enter(player)

room = Room(
    map_=map_,
    enter=enter
)
