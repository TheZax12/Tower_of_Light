from gameMap.MapPosition import MapPosition
from items.Item import Item
from log.LogSubject import LogSubject

from UI.Colors import *


class UsableItem(Item):

    def __init__(self, position: MapPosition):
        super().__init__(position)
        self.visible_color = usable_tile_visible_color
        self.invisible_color = usable_tile_invisible_color

        self.uses_number = self.init_uses_number()
        self.item_effects = self.init_item_effect()  

    def item_name(self):
        pass

    def init_uses_number(self):
        pass
    
    def get_uses_number(self):
        return self.uses_number
    
    def init_item_effect(self):
        pass

    def use(self):
        log_subject = LogSubject()
        
        if self.get_uses_number == 0:
            log_subject.notify_log_observer("No more potions left.")
            return
        else:
            self.init_uses_number(self.get_uses_number() - 1)
            return self.init_item_effect()