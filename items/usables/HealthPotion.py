from items.usables.UsableItem import UsableItem
from gameMap.MapPosition import MapPosition

class HealthPotion(UsableItem):

    def __init__(self, position: MapPosition):
        super().__init__(position)
        self.effect_type = "health replenishment"
        self.effect_value = 30

    def item_name(self):
        return "Health Potion"
    
    def init_uses_number(self):
        return 3
    
    def init_item_effect(self):
        self.item_effects.append((self.effect_type, self.effect_value))
        return self.item_effects