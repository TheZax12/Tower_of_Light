import pygame

from gameMap.MapPosition import MapPosition

from UI.Colors import *


class Button:

    def __init__(self, position: MapPosition, image, text_input, font, base_color, hovering_color):
        self.position = position
        self.image = image
        self.text_input = text_input
        self.font = font
        self.base_color = base_color
        self.hovering_color = hovering_color
        self.text = self.font.render(self.text_input, True, self.base_color)
        if image is not None:
             self.rect = self.image.get_rect(center=(self.position.get_x(), self.position.get_y()))
        else:
             self.rect = self.text.get_rect(center=(self.position.get_x(), self.position.get_y()))
        self.text_rect = self.text.get_rect(center=(self.position.get_x(), self.position.get_y()))

    def update(self, display_surface):
            if self.image is not None:
                 display_surface.blit(self.image, self.rect)
            display_surface.blit(self.text, self.text_rect)

    def check_for_input(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def change_color(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)