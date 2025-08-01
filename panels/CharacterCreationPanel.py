import pygame
from sys import exit

from entities.player.races.Race import Race
from entities.player.races.warriors.Warrior import Warrior
from panels.Button import Button
from gameMap.MapPosition import MapPosition

from panels.PanelSettings import *
from UI.Colors import *


class CharacterCreationPanel:
    
    selected_race = None
    selected_warrior = None

    backgrounds = [
            pygame.image.load("assets/background.png"),
            pygame.image.load("assets/background_blur_lvl_2.png"),
            pygame.image.load("assets/background_blur_lvl_4.png"),
            pygame.image.load("assets/background_blur_lvl_6.png"),
            pygame.image.load("assets/background_blur_lvl_8.png")
    ]
    current_background_idx = 0
    last_background_change = 0
    transition_finished = False

    @classmethod
    def reset_state(cls):
        cls.selected_race = None
        cls.selected_warrior = None
        cls.current_background_idx = 0
        cls.last_background_change = pygame.time.get_ticks()
        cls.transition_finished = False
    
    @staticmethod
    def create_character_creation_panel(display_surface: pygame.Surface, events):
        if CharacterCreationPanel.last_background_change == 0:
            CharacterCreationPanel.reset_state()

        current_time = pygame.time.get_ticks()
        mouse_position = pygame.mouse.get_pos()

        if not CharacterCreationPanel.transition_finished:
            background_change_interval = 25  # milliseconds
            if current_time - CharacterCreationPanel.last_background_change > background_change_interval and \
                CharacterCreationPanel.current_background_idx < len(CharacterCreationPanel.backgrounds) - 1:
                CharacterCreationPanel.current_background_idx += 1
                CharacterCreationPanel.last_background_change = current_time
            if CharacterCreationPanel.current_background_idx == len(CharacterCreationPanel.backgrounds) - 1:
                CharacterCreationPanel.transition_finished = True

        current_background = pygame.transform.scale(
            CharacterCreationPanel.backgrounds[CharacterCreationPanel.current_background_idx], (display_surface.get_width(), display_surface.get_height())
        )
        display_surface.blit(current_background, (0, 0))


        button_starting_y_point = 230

        race_buttons = []
        race_names = ["Human", "Elf", "Orc", "Tauren"]
        for idx, race in enumerate(race_names):
            pos = MapPosition(display_surface.get_width() // 2 - 250, button_starting_y_point + (idx * 90))
            btn = Button(pos, None, race, get_pixel_font(30), text_base_color, text_hovering_color)
            race_buttons.append(btn)

        warrior_buttons = []
        warrior_names = ["Knight", "Paladin", "Mage"]
        for idx, warrior in enumerate(warrior_names):
            pos = MapPosition(display_surface.get_width() // 2 + 250, button_starting_y_point + (idx * 90))
            btn = Button(pos, None, warrior, get_pixel_font(30), text_base_color, text_hovering_color)
            warrior_buttons.append(btn)

        confirm_pos = MapPosition(display_surface.get_width() // 2, 650)
        confirm_button = Button(confirm_pos, None, "Confirm", get_pixel_font(30), text_base_color, text_hovering_color)

        back_pos = MapPosition(display_surface.get_width() // 2, 750)
        back_button = Button(back_pos, None, "Back", get_pixel_font(30), text_base_color, text_hovering_color)


        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    CharacterCreationPanel.reset_state()
                    return "main menu"

            if CharacterCreationPanel.transition_finished:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in race_buttons:
                        if button.check_for_input(mouse_position):
                            CharacterCreationPanel.selected_race = button.text_input

                    for button in warrior_buttons:
                        if button.check_for_input(mouse_position):
                            CharacterCreationPanel.selected_warrior = button.text_input

                    if confirm_button.check_for_input(mouse_position):
                        if CharacterCreationPanel.selected_race and CharacterCreationPanel.selected_warrior:
                            race = Race.races(CharacterCreationPanel.selected_race)
                            warrior = Warrior.warriors(CharacterCreationPanel.selected_warrior)
                            CharacterCreationPanel.reset_state()
                            return race, warrior
                        
                    if back_button.check_for_input(mouse_position):
                        CharacterCreationPanel.reset_state()
                        return "main menu"

        if CharacterCreationPanel.transition_finished:
            label_font = get_pixel_font(30)
            label_font.set_bold(True)
            label_font.set_underline(True)

            race_label_surface = label_font.render("Race", True, text_base_color)
            race_label_rect = race_label_surface.get_rect(center=(display_surface.get_width() // 2 - 250, button_starting_y_point - 90))
            display_surface.blit(race_label_surface, race_label_rect)

            warrior_label_surface = label_font.render("Warrior", True, text_base_color)
            warrior_label_rect = warrior_label_surface.get_rect(center=(display_surface.get_width() // 2 + 250, button_starting_y_point - 90))
            display_surface.blit(warrior_label_surface, warrior_label_rect)
            
            inflation_amount = 12

            for button in race_buttons:
                if CharacterCreationPanel.selected_race == button.text_input:
                    highlight_rect = button.rect.inflate(inflation_amount, inflation_amount)
                    pygame.draw.rect(display_surface, text_highlight_color, highlight_rect)
                    text_surface = get_pixel_font(30).render(button.text_input, True, text_base_color)
                    text_rect = text_surface.get_rect(center=button.rect.center)
                    display_surface.blit(text_surface, text_rect)
                else:
                    button.change_color(mouse_position)
                    button.update(display_surface)
            
            for button in warrior_buttons:
                if CharacterCreationPanel.selected_warrior == button.text_input:
                    highlight_rect = button.rect.inflate(inflation_amount, inflation_amount)
                    pygame.draw.rect(display_surface, text_highlight_color, highlight_rect)
                    text_surface = get_pixel_font(30).render(button.text_input, True, text_base_color)
                    text_rect = text_surface.get_rect(center=button.rect.center)
                    display_surface.blit(text_surface, text_rect)
                else:
                    button.change_color(mouse_position)
                    button.update(display_surface)

            confirm_button.change_color(mouse_position)
            confirm_button.update(display_surface)

            back_button.change_color(mouse_position)
            back_button.update(display_surface)

        return "character creation"