"""
This modules handles the interface and the logic behind creating the player's
character.
"""

from . import interface
from .combat_entity import CombatEntity
from .player import Player
from . import attack

_ENTITY_DISPLAY_NAME = "You"
_CRITICAL_HIT_CHANCE = 4

_ZENON = "zenon"
_CALEB = "caleb"
_KAINOA = "kainoa"
_CLASSES = [_ZENON, _CALEB, _KAINOA]

_BE_ANNOYING = attack.Attack(
    name="be annoying",
    display_name="be annoying",
    type_=attack.MELEE,
    damage=8,
    stamina_cost=2,
    description_of_being_used="pissed off"
)

_ZENON_ENTITY = CombatEntity(
    display_name=_ENTITY_DISPLAY_NAME,
    attacks=[_BE_ANNOYING],
    maximum_health=30,
    maximum_stamina=30,
    strength=8,
    defence=10,
    dexterity=20,
    composure=20,
    critical_hit_chance=_CRITICAL_HIT_CHANCE
)

_CALEB_ENTITY = CombatEntity(
    display_name=_ENTITY_DISPLAY_NAME,
    attacks=[_BE_ANNOYING],
    maximum_health=30,
    maximum_stamina=20,
    strength=4,
    archery=15,
    defence=6,
    dexterity=20,
    composure=15,
    critical_hit_chance=_CRITICAL_HIT_CHANCE
)

_KAINOA_ENTITY = CombatEntity(
    display_name=_ENTITY_DISPLAY_NAME,
    attacks=[_BE_ANNOYING],
    maximum_health=30,
    maximum_mana=20,
    maximum_stamina=10,
    magic=12,
    strength=2,
    defence=6,
    dexterity=20,
    composure=12,
    critical_hit_chance=_CRITICAL_HIT_CHANCE
)

def create_player():
    """
    Display an interface that allows the player to create their character.

    Returns
    -------
    Player
        The Player instance representing the player.
    """
    interface.print_multiple_lines([
        "On your adventure you may be Zenon, Caleb, or Kainoa.",
        "Which do you choose?"
    ])

    command = interface.get_command(_CLASSES)

    interface.print_("You have chosen the role of {}.".format(command))
    interface.print_()

    if command == _ZENON:
        return Player(_ZENON_ENTITY, "Zenon")

    if command == _CALEB:
        return Player(_CALEB_ENTITY, "Caleb")

    return Player(_KAINOA_ENTITY, "Kainoa")
