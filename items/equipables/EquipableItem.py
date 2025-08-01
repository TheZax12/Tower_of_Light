from gameMap.MapPosition import MapPosition
from items.Item import Item
from items.ItemEffect import ItemEffect

from UI.Colors import *


class EquipableItem(Item):

    def __init__(self, position: MapPosition, item_effects: list[ItemEffect]):
        super().__init__(position)
        self.visible_color = equipable_tile_visible_color
        self.invisible_color = equipable_tile_invisible_color

        self.item_name = self.get_item_name()
        self.item_effects = item_effects

    def get_item_effects(self) -> list[ItemEffect]:
        return self.item_effects
    
    def get_unequip_item_effects(self) -> list[ItemEffect]:
        return [
            ItemEffect(effect.effect_type, -effect.stat_enhancement)
            for effect in self.item_effects
        ]