"""This modules contains the code representing the enemies in the game."""

from .combat_entity import CombatEntity
from . import attack
import winsound
import time
def bear():
    winsound.PlaySound(None, winsound.SND_PURGE)
    winsound.PlaySound("text_based_rpg/mus/battlest.wav", winsound.SND_ASYNC)
    time.sleep(1)
    winsound.PlaySound("text_based_rpg/mus/battle.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
    return CombatEntity(
        display_name="Student being normal",
        attacks=[
            attack.Attack(
                name="common sense",
                display_name="Common sense",
                type_=attack.MAGIC,
                damage=2,
                description_of_being_used="Bruh. It just works.",
                stamina_cost=4
            ),
            attack.Attack(
                name="ignore",
                display_name="Ignore",
                type_=attack.RANGED,
                damage=4,
                description_of_being_used="they hurt your feelings by ignoring you.",
                stamina_cost=6
            )
        ],
        maximum_health=20,
        maximum_stamina=15,
        strength=8,
        defence=10,
        dexterity=4,
        composure=5,
        critical_hit_chance=2
    )

def first_boss():
    winsound.PlaySound(None, winsound.SND_PURGE)
    winsound.PlaySound("text_based_rpg/mus/battlest.wav", winsound.SND_ASYNC)
    time.sleep(1)
    winsound.PlaySound("text_based_rpg/mus/battle.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
    return CombatEntity(
        display_name="Kerria",
        attacks=[
            attack.Attack(
                name="shyness",
                display_name="Shyness",
                type_=attack.RANGED,
                damage=3,
                description_of_being_used="makes you feel bad for her",
                stamina_cost=3
            ),
            attack.Attack(
                name="nose bleed",
                display_name="Nose bleed",
                type_=attack.MELEE,
                damage=6,
                description_of_being_used="You don't have a tissue",
                stamina_cost=4
            )
        ],
        maximum_health=25,
        maximum_stamina=20,
        strength=10,
        defence=15,
        dexterity=6,
        composure=7,
        critical_hit_chance=4
    )

def second_boss():
    return CombatEntity(
        display_name="Ms. Kuper herself",
        attacks=[
            attack.Attack(
                name="knowledge",
                display_name="Knowledge",
                type_=attack.MELEE,
                damage=8,
                description_of_being_used="just think about the problem and stop coming to me, otherwise you'll get a zero",
                stamina_cost=6
            ),
            attack.Attack(
                name="caught off gaurd",
                display_name="Caught off gaurd",
                type_=attack.MELEE,
                damage=14,
                description_of_being_used="PAY ATTENTION DURING CLASS!!!",
                stamina_cost=8
            ),
            attack.Attack(
                name="traceback error",
                display_name="Traceback error",
                type_=attack.MELEE,
                damage=20,
                description_of_being_used="Your program blew up, now it's gonna be deleted",
                stamina_cost=5

            )

        ],
        maximum_health=40,
        maximum_stamina=50,
        strength=15,
        defence=25,
        dexterity=7,
        composure=8,
        critical_hit_chance=4
    )
