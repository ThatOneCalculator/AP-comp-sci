from . import interface
from .battle.battle_util import PlayerHasDiedError
from .create_player import create_player
from .rooms.tavern import room as tavern
from .util import GameOver
from .rooms.reset import reset as reset_rooms

def start_game():
    """
    Start and control the game.

    Returns
    -------
    None

    """

    reset_rooms()
    player = create_player()

    try:
        tavern.enter(player)
    except (PlayerHasDiedError, GameOver) as exception:
        if isinstance(exception, PlayerHasDiedError):
            interface.print_multiple_lines(
                lines=[
                    "=" * 20,
                    "",
                    "",
                    "",
                    "You have died. Oops ¯|_(ツ)_|¯",
                    "",
                    "",
                    "",
                    "=" * 20
                ],
                delay=1
            )
        else:
            interface.sleep(6)
            interface.print_multiple_lines(
                lines=[
                    "You beat her"
                    "You have won"
                    "You did it"
                    "Until you realize"
                    "You have class tommorow"
                    "Hope you had fun!"
                ],
                delay=2
            )

            interface.print_()
            interface.sleep(6)
