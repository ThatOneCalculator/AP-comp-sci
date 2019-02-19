"""
This modules handles the interface and the logic behind creating the player's
character.
"""

from . import interface
from .combat_entity import CombatEntity
from .player import Player
from . import attack
import winsound
import time
import os
import sys
from fastprint import pr
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
    wish=input("Do you wish to hear the story? Enter \"N\" to skip or any other key to hear \n\n").upper()
    if wish!="N":
      st="""   Once upon a time, 
   a LEGEND was whispered among shadows...
   It was a LEGEND of GRADES.
   It was a LEGEND of STUDENTS.
   It was a LEGEND of a TASK.
   It was a LEGEND of a TEST.

   This is the legend of KUPER
   For millenia STUDENTS and ASSIGNMENTS have lived in balance
   Bringing peace to the CLASSROOM.
   But if this harmony were to shatter...
   A terrible calamity would occur.
   
   The students' GRADES will go below a C-,
   And the teacher will look bad.
   Then an without explanation...
   The PARENTS will call the school.
   Only then shining with hope...
   Three HEROES appear at CLASSROOMS' edge.


   KAINOA
   CALEB
   And ZENON.

   Only they can retrieve the RUBRIC
   And the STUDENT SAMPLES.
   Only then will balance be restored
   The curse shall be lifted,
   And the CLASSROOM saved from destruction.
   Peace shall return to the land,
   And the HEROS shall prevail.



   Once the COLLEGE BOARD-
   The company that distributes the forms-
   Helped students in need.

   But recently the website was taken down.
   And with it there are no COPIES of the DOCUMENTS...
    """
      winsound.PlaySound("text_based_rpg/mus/legend.wav", winsound.SND_ASYNC)
      pr(st, 2.6)
    winsound.PlaySound("text_based_rpg/mus/AUDIO_DRONE.wav",winsound.SND_ASYNC)
    interface.print_multiple_lines([
        "On your adventure you may be Zenon, Caleb, or Kainoa.",
        "Which do you choose?"
    ])

    command = interface.get_command(_CLASSES)
    time.sleep(2)
    interface.print_("You have chosen the role of {}.".format(command))
    winsound.PlaySound(None, winsound.SND_PURGE)
    interface.print_()

    if command == _ZENON:
        return Player(_ZENON_ENTITY, "Zenon")

    if command == _CALEB:
        return Player(_CALEB_ENTITY, "Caleb")

    return Player(_KAINOA_ENTITY, "Kainoa")
