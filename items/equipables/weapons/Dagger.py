from items.equipables.weapons.Weapon import Weapon
from gameMap.MapPosition import MapPosition
from items.equipables.Damage import Damage, DamageType
from items.equipables.Dice import Dice


class Dagger(Weapon):
    def __init__(self, position: MapPosition):
        super().__init__(
            position,
            [],
            [Damage(DamageType.THRUST, Dice.from_string("1d6+1"))]
        )
        
    def get_item_name(self) -> str:
        return "Dagger"