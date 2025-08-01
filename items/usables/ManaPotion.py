from items.usables.UsableItem import UsableItem
from items.ItemEffect import ItemEffect
from items.ItemEffect import ItemEffectType
from gameMap.MapPosition import MapPosition


class ManaPotion(UsableItem):

    def __init__(self, position: MapPosition):
        super().__init__(position)
    
    def get_item_name(self):
        return "Mana Potion"
    
    def init_uses_number(self) -> int:
        return 3
    
    def init_item_effects(self) -> list[ItemEffect]:
        return [ItemEffect(ItemEffectType.MP_REPLENISHMENT, 40)]