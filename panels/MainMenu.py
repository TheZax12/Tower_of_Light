import pygame
from sys import exit

from panels.Button import Button
from gameMap.MapPosition import MapPosition

from gameMap.MapSettings import *
from panels.PanelSettings import *
from UI.Colors import *


class MainMenu:
    
    @staticmethod
    def create_main_menu(display_surface: pygame.Surface, events):
        display_surface.blit(pygame.image.load("assets/background.png"), (0, 0))

        mouse_position = pygame.mouse.get_pos()

        start_button = Button(MapPosition(display_surface.get_width() // 2, 780), None, "Enter the Tower", get_pixel_font(30), text_base_color, text_hovering_color)
        controls_button = Button(MapPosition(display_surface.get_width() // 2 - 500, 780), None, "Controls", get_pixel_font(30), text_base_color, text_hovering_color)
        quit_button = Button(MapPosition(display_surface.get_width() // 2 + 530, 780), None, "Quit", get_pixel_font(30), text_base_color, text_hovering_color)

        buttons = [start_button, controls_button, quit_button]

        for button in buttons:
            button.change_color(mouse_position)
            button.update(display_surface)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.check_for_input(mouse_position):
                    return "character creation"
                elif controls_button.check_for_input(mouse_position):
                    return "controls"
                elif quit_button.check_for_input(mouse_position):
                    return "quit"
                
        return "main menu"