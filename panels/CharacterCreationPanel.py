import pygame
from sys import exit

from entities.player.races.Race import Race
from entities.player.races.warriors.Warrior import Warrior
from panels.Button import Button
from gameMap.MapPosition import MapPosition

from panels.PanelSettings import *
from UI.Colors import *


class CharacterCreationPanel:
    
    @staticmethod
    def create_character_creation_panel(display_surface: pygame.Surface):
        clock = pygame.time.Clock()

        backgrounds = [
            pygame.image.load("assets/background.png"),
            pygame.image.load("assets/background_blur_lvl_2.png"),
            pygame.image.load("assets/background_blur_lvl_4.png"),
            pygame.image.load("assets/background_blur_lvl_6.png"),
            pygame.image.load("assets/background_blur_lvl_8.png")
        ]
        current_bg_idx = 0
        bg_change_interval = 25  # milliseconds
        last_bg_change = pygame.time.get_ticks()
        transition_finished = False

        btn_starting_y_point = 230

        race_buttons = []
        race_names = ["Human", "Elf", "Orc", "Tauren"]
        for idx, race in enumerate(race_names):
            pos = MapPosition(display_surface.get_width() // 2 - 250, btn_starting_y_point + (idx * 90))
            btn = Button(pos, None, race, get_pixel_font(30), text_base_color, text_hovering_color)
            race_buttons.append(btn)

        warrior_buttons = []
        warrior_names = ["Knight", "Paladin", "Mage"]
        for idx, warrior in enumerate(warrior_names):
            pos = MapPosition(display_surface.get_width() // 2 + 250, btn_starting_y_point + (idx * 90))
            btn = Button(pos, None, warrior, get_pixel_font(30), text_base_color, text_hovering_color)
            warrior_buttons.append(btn)

        confirm_pos = MapPosition(display_surface.get_width() // 2, 650)
        confirm_button = Button(confirm_pos, None, "Confirm", get_pixel_font(30), text_base_color, text_hovering_color)

        back_pos = MapPosition(display_surface.get_width() // 2, 750)
        back_button = Button(back_pos, None, "Back", get_pixel_font(30), text_base_color, text_hovering_color)

        selected_race = None
        selected_warrior = None

        running = True
        while running:
            events = pygame.event.get()
            current_time = pygame.time.get_ticks()
            mouse_position = pygame.mouse.get_pos()

            if not transition_finished:
                if current_time - last_bg_change > bg_change_interval and current_bg_idx < len(backgrounds) - 1:
                    current_bg_idx += 1
                    last_bg_change = current_time
                if current_bg_idx == len(backgrounds) - 1:
                    transition_finished = True
            
            current_bg = pygame.transform.scale(backgrounds[current_bg_idx], (display_surface.get_width(), display_surface.get_height()))
            display_surface.blit(current_bg, (0, 0))

            for event in events:
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    exit()
                
                if transition_finished:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        click_position = event.pos

                        for button in race_buttons:
                            if button.check_for_input(click_position):
                                selected_race = button.text_input

                        for button in warrior_buttons:
                            if button.check_for_input(click_position):
                                selected_warrior = button.text_input

                        if confirm_button.check_for_input(click_position):
                            if selected_race and selected_warrior:
                                selected_race = Race.races(selected_race)
                                selected_warrior = Warrior.warriors(selected_warrior)
                                running = False
                                return selected_race, selected_warrior
                            
                        if back_button.check_for_input(click_position):
                            running = False
                            return None, None

            if transition_finished:

                # Create font for labels
                label_font = get_pixel_font(30)
                label_font.set_bold(True)
                label_font.set_underline(True)

                race_label_surface = label_font.render("Race", True, text_base_color)
                race_label_rect = race_label_surface.get_rect(center=(display_surface.get_width() // 2 - 250, btn_starting_y_point - 90))
                display_surface.blit(race_label_surface, race_label_rect)

                warrior_label_surface = label_font.render("Warrior", True, text_base_color)
                warrior_label_rect = warrior_label_surface.get_rect(center=(display_surface.get_width() // 2 + 250, btn_starting_y_point - 90))
                display_surface.blit(warrior_label_surface, warrior_label_rect)

                
                inflation_amount = 12

                # Update and draw race buttons
                for button in race_buttons:
                    if selected_race == button.text_input:
                        highlight_rect = button.rect.inflate(inflation_amount, inflation_amount)
                        pygame.draw.rect(display_surface, text_highlight_color, highlight_rect)
                        text_surface = get_pixel_font(30).render(button.text_input, True, text_base_color)
                        text_rect = text_surface.get_rect(center=button.rect.center)
                        display_surface.blit(text_surface, text_rect)
                    else:
                        button.change_color(mouse_position)
                        button.update(display_surface)
                
                # Update and draw warrior buttons
                for button in warrior_buttons:
                    if selected_warrior == button.text_input:
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

            pygame.display.update()
            clock.tick(60)

        return None, None