from entities.Entity import Entity

from UI.Colors import *


class Enemy(Entity):

    def __init__(self, position):
        super().__init__(position)
        self.discovered = False
        self.visible = False

    def set_discovered(self, discovered: bool):
        self.discovered = discovered

    def is_discovered(self) -> bool:
        return self.discovered
    
    def set_visible(self, visible: bool):
        self.visible = visible
    
    def is_visible(self) -> bool:
        return self.visible
    
    def set_visible_color(self, color):
        self.visible_color = color

    def set_invisible_color(self, color):
        self.invisible_color = color