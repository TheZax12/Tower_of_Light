import pygame

from panels.Button import Button
from gameMap.MapPosition import MapPosition

from UI.Colors import *
from panels.PanelSettings import *


class EndScreen:

    @staticmethod
    def winning_screen(display_surface: pygame.Surface, events):
        
        background = pygame.image.load("assets/background.png")
        display_surface.blit(background, (0, 0))

        winning_text_1 = get_pixel_font(30).render("Congratulations warrior!", True, text_base_color)
        winning_rect = winning_text_1.get_rect(center=(620, 80))
        winning_text_2 = get_pixel_font(30).render("You have defeated the chaos and restored the light to the tower!", True, text_base_color)
        winning_rect_2 = winning_text_2.get_rect(center=(620, 120))
        display_surface.blit(winning_text_1, winning_rect)
        display_surface.blit(winning_text_2, winning_rect_2)

        main_menu_button = Button(MapPosition(500, 300), None, "Main Menu", get_pixel_font(40), text_base_color, text_hovering_color)
        quit_button = Button(MapPosition(800, 300), None, "Quit", get_pixel_font(40), text_base_color, text_hovering_color)
        
        mouse = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if main_menu_button.check_for_input(mouse_position):
                    return "main menu"
                elif quit_button.check_for_input(mouse_position):
                    return "quit"

        main_menu_button.change_color(mouse)
        quit_button.change_color(mouse)
        main_menu_button.update(display_surface)
        quit_button.update(display_surface)

        return "win screen"

    @staticmethod
    def losing_screen(display_surface: pygame.Surface, events):
        
        background = pygame.image.load("assets/background.png")
        display_surface.blit(background, (0, 0))

        losing_text_1 = get_pixel_font(30).render("You have fallen warrior!", True, text_base_color)
        losing_rect = losing_text_1.get_rect(center=(620, 80))
        losing_text_2 = get_pixel_font(30).render("The dark forces prevailed and the tower sunked into chaos!", True, text_base_color)
        losing_rect_2 = losing_text_2.get_rect(center=(620, 120))
        display_surface.blit(losing_text_1, losing_rect)
        display_surface.blit(losing_text_2, losing_rect_2)

        main_menu_button = Button(MapPosition(500, 300), None, "Main Menu", get_pixel_font(40), text_base_color, text_hovering_color)
        quit_button = Button(MapPosition(800, 300), None, "Quit", get_pixel_font(40), text_base_color, text_hovering_color)

        
        mouse = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if main_menu_button.check_for_input(mouse_position):
                    return "main menu"
                elif quit_button.check_for_input(mouse_position):
                    return "quit"

        main_menu_button.change_color(mouse)
        quit_button.change_color(mouse)
        main_menu_button.update(display_surface)
        quit_button.update(display_surface)

        return "lose screen"