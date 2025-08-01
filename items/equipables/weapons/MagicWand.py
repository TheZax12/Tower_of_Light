from items.equipables.weapons.Weapon import Weapon
from gameMap.MapPosition import MapPosition
from items.equipables.Damage import Damage, DamageType
from items.equipables.Dice import Dice


class MagicWand(Weapon):
    def __init__(self, position: MapPosition):
        super().__init__(
            position,
            [],
            [
                Damage(DamageType.MAGIC, Dice.from_string("1d3+1")),
                Damage(DamageType.SWING, Dice.from_string("1d3"))
            ]
        )
        
    def get_item_name(self) -> str:
        return "Magic Wand"