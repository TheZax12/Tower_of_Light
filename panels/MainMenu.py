import pygame
from sys import exit

from panels.Button import Button
from gameMap.MapPosition import MapPosition

from gameMap.MapSettings import *
from panels.PanelSettings import *
from UI.Colors import *


class MainMenu:
    
    @staticmethod
    def create_main_menu(display_surface, events, start_game_callback):
        display_surface.blit(pygame.image.load("assets/background.png"), (0, 0))

        mouse_position = pygame.mouse.get_pos()

        # # Render the shadow text
        # menu_text_shadow = get_font(70).render("Main Menu", True, (0, 0, 0))
        # menu_rect_shadow = menu_text_shadow.get_rect(center=(643, 83))
        # display_surface.blit(menu_text_shadow, menu_rect_shadow)

        # # Render the main text
        # menu_text = get_font(70).render("Main Menu", True, button_base_color)
        # menu_rect = menu_text.get_rect(center=(640, 80))
        # display_surface.blit(menu_text, menu_rect)

        start_text = get_font(30).render("Press space to enter the castle", True, text_base_color)
        start_rect = start_text.get_rect(center=(620, 780))
        display_surface.blit(start_text, start_rect)

        controls_button = Button(MapPosition(120, 780), None, "Controls", get_font(30), text_base_color, text_hovering_color)
        quit_button = Button(MapPosition(1150, 780), None, "Quit", get_font(30), text_base_color, text_hovering_color)

        buttons = [controls_button, quit_button]

        for button in buttons:
            button.change_color(mouse_position)
            button.update(display_surface)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if controls_button.check_for_input(mouse_position):
                    return "controls"
                elif quit_button.check_for_input(mouse_position):
                    pygame.quit()
                    exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_game_callback()
                
        pygame.display.update()