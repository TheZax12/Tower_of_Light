import pygame

from panels.Button import Button
from gameMap.MapPosition import MapPosition

from panels.PanelSettings import *
from UI.Colors import *


class PauseMenu:
    show_controls = False

    @staticmethod
    def create_pause_menu(display_surface: pygame.Surface, events):
        pause_surface = pygame.Surface((screen_width / 1.5, screen_height / 1.1))
        pause_surface.set_alpha(220) 
        pause_surface.fill(pause_menu_background_color)
        
        pause_rect = pause_surface.get_rect(center=(display_surface.get_width() / 2, display_surface.get_height() / 2))
        display_surface.blit(pause_surface, pause_rect)

        mouse_position = pygame.mouse.get_pos()

        if PauseMenu.show_controls:
            # Controls View
            title_font = get_pixel_font(50)
            title_font.set_underline(True)
            title_text = title_font.render("Controls", True, text_base_color)
            title_rect = title_text.get_rect(center=(display_surface.get_width() / 2, pause_rect.top + 70))
            display_surface.blit(title_text, title_rect)

            controls = {
                "Move Up": "W / Up", "Move Down": "S / Down", "Move Left": "A / Left", "Move Right": "D / Right",
                "Base Attack": "Space", "Spell Attack": "X", "Rest": "R", "Consume Healing Potion": "H",
                "Consume Mana Potion": "M", "Change Main Weapon": "T", "Change Secondary Weapon": "Y",
                "Swap Weapons" : "U", "Create Beacon": "L"
            }

            y_offset = pause_rect.top + 130
            x_offset_action = display_surface.get_width() / 2 - 250
            x_offset_key = display_surface.get_width() / 2 + 100
            controls_font = get_pixel_font(20)

            for action, key in controls.items():
                action_text = controls_font.render(f"{action}:", True, text_base_color)
                action_rect = action_text.get_rect(topleft=(x_offset_action, y_offset))
                display_surface.blit(action_text, action_rect)

                key_text = controls_font.render(key, True, text_base_color)
                key_rect = key_text.get_rect(topleft=(x_offset_key, y_offset))
                display_surface.blit(key_text, key_rect)
                y_offset += 40

            back_button = Button(MapPosition(display_surface.get_width() // 2, pause_rect.bottom - 50), None, "Back", get_pixel_font(30), text_base_color, text_hovering_color)
            back_button.change_color(mouse_position)
            back_button.update(display_surface)

            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.check_for_input(mouse_position):
                        PauseMenu.show_controls = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return "gameplay"

        else:
            menu_text = get_pixel_font(50).render("Paused", True, text_base_color)
            menu_rect = menu_text.get_rect(center=(display_surface.get_width() / 2, pause_rect.top + 70))
            display_surface.blit(menu_text, menu_rect)

            resume_button = Button(MapPosition(display_surface.get_width() // 2, display_surface.get_height() / 2 - 100), None, "Resume", get_pixel_font(30), text_base_color, text_hovering_color)
            controls_button = Button(MapPosition(display_surface.get_width() // 2, display_surface.get_height() / 2), None, "Controls", get_pixel_font(30), text_base_color, text_hovering_color)
            main_menu_button = Button(MapPosition(display_surface.get_width() // 2, display_surface.get_height() / 2 + 100), None, "Exit to Main Menu", get_pixel_font(30), text_base_color, text_hovering_color)
            quit_button = Button(MapPosition(display_surface.get_width() // 2, display_surface.get_height() / 2 + 200), None, "Quit", get_pixel_font(30), text_base_color, text_hovering_color)

            buttons = [resume_button, controls_button, main_menu_button, quit_button]
            for button in buttons:
                button.change_color(mouse_position)
                button.update(display_surface)

            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if resume_button.check_for_input(mouse_position):
                        return "gameplay"
                    if controls_button.check_for_input(mouse_position):
                        PauseMenu.show_controls = True
                    if main_menu_button.check_for_input(mouse_position):
                        PauseMenu.show_controls = False
                        return "main menu"
                    if quit_button.check_for_input(mouse_position):
                        return "quit"
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return "gameplay"
        
        return "pause"
