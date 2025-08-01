from items.Item import Item
from gameMap.MapPosition import MapPosition
from log.LogSubject import LogSubject


from UI.Colors import *


class UsableItem(Item):
    
    def __init__(self, position: MapPosition):
        super().__init__(position)
        self.visible_color = usable_tile_visible_color
        self.invisible_color = usable_tile_invisible_color
        
        self.item_name = self.get_item_name()
        self.item_effects = self.init_item_effects()
        self.uses_number = self.init_uses_number()
    
    def set_uses_number(self, uses_number: int):
        self.uses_number = uses_number
    
    def get_uses_number(self):
        return self.uses_number
    
    def init_uses_number(self):
        pass

    def init_item_effects(self):
        pass

    def use(self):
        log_subject = LogSubject()

        if self.get_uses_number() == 0:
            return []
        else:
            self.set_uses_number(self.get_uses_number() - 1)
            log_subject.notify_log_observer(f"Used a {self.item_name.lower()}.")
            return self.item_effects