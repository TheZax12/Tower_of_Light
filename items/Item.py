import pygame

from gameMap.MapPosition import MapPosition

from gameMap.MapSettings import tile_size, item_size
from UI.Colors import undiscovered_area_color

class Item:

    def __init__(self, position: MapPosition):
        self.position = position
        self.discovered = False
        self.visible = False

    def get_item_name(self):
        pass
        
    def set_position(self, position: MapPosition):
        self.position = position
    
    def get_position(self) -> MapPosition:
        return self.position
    
    def set_rect(self, rect: pygame.Rect):
        self.rect = rect

    def get_rect(self) -> pygame.Rect:
        return self.rect
    
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

    def visibility(self, player):
        distance_to_item = self.get_position().distance_to(player.get_position())
        if distance_to_item <= player.visibility_radius:
            self.set_visible(True)
            if not self.is_discovered():
                self.set_discovered(True)
        else:
            self.set_visible(False)

    def on_corner(self):
        """Adjusts the position of the item's rectangle based on its type."""
        from items.usables.UsableItem import UsableItem
        from items.equipables.EquipableItem import EquipableItem

        if isinstance(self, UsableItem):
            x_position = self.get_position().x * tile_size + 9
            y_position = self.get_position().y * tile_size
        elif isinstance(self, EquipableItem):
            x_position = self.get_position().x * tile_size
            y_position = self.get_position().y * tile_size + 9

        self.set_rect(pygame.Rect(x_position, y_position, item_size, item_size))

    def draw_undiscovered(self, display_surface):
        pygame.draw.rect(display_surface, undiscovered_area_color, self.get_rect())

    def draw_visible(self, display_surface):
        pygame.draw.rect(display_surface, self.visible_color, self.get_rect())

    def draw_invisible(self, display_surface):
        pygame.draw.rect(display_surface, self.invisible_color, self.get_rect())

    def draw(self, display_surface: pygame.Surface):
        # Update the item's rectangle position.
        self.on_corner()
        
        # Draw the item.
        if not self.is_discovered():
            self.draw_undiscovered(display_surface)
        elif self.is_visible():
            self.draw_visible(display_surface)
        else:
            self.draw_invisible(display_surface)

        # Draw the rectangle's border.
        pygame.draw.rect(display_surface, (0, 0, 0), self.get_rect(), 1)