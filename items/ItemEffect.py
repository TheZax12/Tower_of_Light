from enum import Enum


class ItemEffectType(Enum):
    HP_REPLENISHMENT = "health replenishment"
    MP_REPLENISHMENT = "mana replenishment"
    HP_BOOST = "health boost"
    MP_BOOST = "mana boost"
    STR_BOOST = "strength boost"
    INT_BOOST = "intellect boost"


class ItemEffect:

    def __init__(self, effect_type: ItemEffectType, stat_enhancement: int):
        self.effect_type = effect_type
        self.stat_enhancement = stat_enhancement