from gameMap.MapPosition import MapPosition

class Item:

    def __init__(self, position: MapPosition):
        self.position = position
        self.discovered = False
        self.visible = False

    def get_position(self) -> MapPosition:
        return self.position
    
    def set_discovered(self, discovered: bool):
        self.discovered = discovered

    def is_discorvered(self) -> bool:
        return self.discovered
    
    def set_visible(self, visible: bool):
        self.visible = visible

    def is_visible(self) -> bool:
        return self.visible
    
    def set_visible_color(self, color):
        self.visible_color = color

    def set_invisible_color(self, color):
        self.invisible_color = color