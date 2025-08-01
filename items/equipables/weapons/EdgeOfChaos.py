from items.equipables.weapons.Weapon import Weapon
from gameMap.MapPosition import MapPosition
from items.equipables.Damage import Damage, DamageType
from items.equipables.Dice import Dice
from items.ItemEffect import ItemEffect
from items.ItemEffect import ItemEffectType


class EdgeOfChaos(Weapon):

    def __init__(self, position: MapPosition):
        super().__init__(
            position,
            [   
                ItemEffect(ItemEffectType.STR_BOOST, 10),
                ItemEffect(ItemEffectType.INT_BOOST, 10),
                ItemEffect(ItemEffectType.MP_BOOST, 10)
            ],
            [   
                Damage(DamageType.THRUST, Dice.from_string("3d6+2")),
                Damage(DamageType.SWING, Dice.from_string("2d6+2")),
                Damage(DamageType.MAGIC, Dice.from_string("2d6+2"))
            ]
        )
        
    def get_item_name(self) -> str:
        return "Edge of Chaos"