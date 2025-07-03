from __future__ import annotations

from copy import copy
from enum import Enum, auto

from items.equipables.Dice import Dice


class DamageType(Enum):
    THRUST = auto()
    SWING = auto()
    MAGIC = auto()


class Damage:

    def __init__(self, damage_type: DamageType, damage_dice: Dice):
        self.damage_type = damage_type
        self.damage_dice = copy(damage_dice)

    def get_damage_amount(self) -> int:
        return self.damage_dice.roll()
    
    def enhance(self, value: int):
        self.damage_dice.add_constant_addend(value)
    
    def __repr__(self):
        return f"Damage(damage type={self.damage_type.name}, damage dice={self.damage_dice})"