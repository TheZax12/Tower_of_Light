from items.equipables.weapons.Weapon import Weapon
from gameMap.MapPosition import MapPosition
from items.equipables.Damage import Damage, DamageType
from items.equipables.Dice import Dice


class DivineHammer(Weapon):

    def __init__(self, position: MapPosition):
        super().__init__(position,
                         None,
                         [Damage(DamageType.THRUST, Dice.from_string("2d6+4")),
                          Damage(DamageType.MAGIC, Dice.from_string("2d6+2"))],
                         "Divine Hammer")