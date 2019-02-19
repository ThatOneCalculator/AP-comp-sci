"""This modules contains the code representing the items in the game."""

from . import item, attack

iron_sword = item.Item(
    display_name="Phone",
    type_=item.EQUIPPABLE,
    equip_location="pocket (not backpack)",
    effects=[item.ItemEffect(stat="strength", modifier=5), item.ItemEffect(stat="dexterity", modifier=-2)],
    attacks=[
        attack.Attack(
            name="text",
            display_name="Text",
            type_=attack.MELEE,
            damage=3,
            stamina_cost=2,
            description_of_being_used="dabbed"
        ),
        attack.Attack(
            name="check time",
            display_name="Check time",
            type_=attack.MELEE,
            damage=5,
            stamina_cost=4,
            description_of_being_used="flashed your phone"
        )
    ]
)

iron_helmet = item.Item(
    display_name="Hood",
    type_=item.EQUIPPABLE,
    equip_location="head",
    effects=[
        item.ItemEffect(stat="defence", modifier=4),
        item.ItemEffect(stat="strength", modifier=1),
        item.ItemEffect(stat="dexterity", modifier=-1)
    ]
)

iron_breastplate = item.Item(
    display_name="Same shirt as yesterday, and the day before, and the day before that...",
    type_=item.EQUIPPABLE,
    equip_location="torso",
    effects=[item.ItemEffect(stat="defence", modifier=6), item.ItemEffect(stat="strength", modifier=2), item.ItemEffect(stat="dexterity", modifier=-2)]
)

iron_platelegs = item.Item(
    display_name="Weston's shorts you couldn't stop glancing at",
    type_=item.EQUIPPABLE,
    equip_location="legs",
    effects=[item.ItemEffect(stat="defence", modifier=5), item.ItemEffect(stat="strength", modifier=1), item.ItemEffect(stat="dexterity", modifier=-1)]
)

oak_bow = item.Item(
    display_name="Samsung S9+",
    type_=item.EQUIPPABLE,
    equip_location="arms",
    effects=[item.ItemEffect(stat="archery", modifier=5), item.ItemEffect(stat="dexterity", modifier=-1)],
    attacks=[
        attack.Attack(
            name="bixby",
            display_name="Bixby",
            type_=attack.RANGED,
            damage=3,
            stamina_cost=1,
            description_of_being_used="said Bixby was better than Google Assistant"
        )
    ]
)

cow_hide_body = item.Item(
    display_name="LTT shirt",
    type_=item.EQUIPPABLE,
    equip_location="torso",
    effects=[item.ItemEffect(stat="defence", modifier=5), item.ItemEffect(stat="archery", modifier=3)]
)


ice_staff = item.Item(
    display_name="Custom python module",
    type_=item.EQUIPPABLE,
    equip_location="arms",
    effects=[item.ItemEffect(stat="magic", modifier=5), item.ItemEffect(stat="dexterity", modifier=-2)],
    attacks=[
        attack.Attack(
            name="custom python module",
            display_name="Custom python module",
            type_=attack.MAGIC,
            damage=3,
            mana_cost=4,
            description_of_being_used="installed with pip"
        )
    ]
)

robe = item.Item(
    display_name="Anime shirt",
    type_=item.EQUIPPABLE,
    equip_location="torso",
    effects=[item.ItemEffect(stat="defence", modifier=4), item.ItemEffect(stat="magic", modifier=4)]
)

hood = item.Item(
    display_name="Earbuds",
    type_=item.EQUIPPABLE,
    equip_location="head",
    effects=[item.ItemEffect(stat="defence", modifier=3), item.ItemEffect(stat="magic", modifier=3)]
)

steel_sword = item.Item(
    display_name="Late pass",
    type_=item.EQUIPPABLE,
    equip_location="arms",
    effects=[item.ItemEffect(stat="strength", modifier=10), item.ItemEffect(stat="dexterity", modifier=-4)],
    attacks=[
        attack.Attack(
            name="i'm sorry",
            display_name="I'm sorry",
            type_=attack.MELEE,
            damage=6,
            stamina_cost=4,
            description_of_being_used="showed up late"
        ),
        attack.Attack(
            name="student body meeting",
            display_name="Student body meeting",
            type_=attack.MELEE,
            damage=10,
            stamina_cost=8,
            description_of_being_used="abbrubtly left"
        )
    ]
)


willow_bow = item.Item(
    display_name="PC",
    type_=item.EQUIPPABLE,
    equip_location="arms",
    effects=[item.ItemEffect(stat="archery", modifier=10), item.ItemEffect(stat="dexterity", modifier=-2)],
    attacks=[
        attack.Attack(
            name="look at the specs",
            display_name="Look at the specs",
            type_=attack.RANGED,
            damage=6,
            stamina_cost=2,
            description_of_being_used="showed the specsheet"
        )
    ]
)

bear_hide_body = item.Item(
    display_name="OnePlus Backpack",
    type_=item.EQUIPPABLE,
    equip_location="torso",
    effects=[item.ItemEffect(stat="defence", modifier=10), item.ItemEffect(stat="archery", modifier=6)]
)

fire_staff = item.Item(
    display_name="Koa phone",
    type_=item.EQUIPPABLE,
    equip_location="arms",
    effects=[item.ItemEffect(stat="magic", modifier=10), item.ItemEffect(stat="dexterity", modifier=-4)],
    attacks=[
        attack.Attack(
            name="proof of existence",
            display_name="Proof of existence",
            type_=attack.MAGIC,
            damage=6,
            mana_cost=6,
            description_of_being_used="showed the prototype video and promised it would be live soon on indiegogo"
        )
    ]
)

battle_robe = item.Item(
    display_name="Headphones",
    type_=item.EQUIPPABLE,
    equip_location="torso",
    effects=[item.ItemEffect(stat="defence", modifier=8), item.ItemEffect(stat="magic", modifier=8)]
)

battle_hood = item.Item(
    display_name="Trendy sweatshirt",
    type_=item.EQUIPPABLE,
    equip_location="head",
    effects=[item.ItemEffect(stat="defence", modifier=6), item.ItemEffect(stat="magic", modifier=6)]
)

def health_potion():
    return item.Item(
        display_name="Health potion",
        type_=item.CONSUMABLE,
        effects=[item.ItemEffect(stat="health", modifier=10)]
    )

def stamina_potion():
    return item.Item(
        display_name="Stamina potion",
        type_=item.CONSUMABLE,
        effects=[item.ItemEffect(stat="stamina", modifier=10)]
    )

def mana_potion():
    return item.Item(
        display_name="Mana potion",
        type_=item.CONSUMABLE,
        effects=[item.ItemEffect(stat="mana", modifier=10)]
    )
