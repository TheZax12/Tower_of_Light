import pygame

from panels.Button import Button
from gameMap.MapPosition import MapPosition

from panels.PanelSettings import *
from UI.Colors import *

class Controls:

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
        cls.current_background_idx = 0
        cls.last_background_change = pygame.time.get_ticks()
        cls.transition_finished = False
    
    @staticmethod
    def create_controls_panel(display_surface: pygame.Surface, events, previous_state: str):
        if Controls.last_background_change == 0:
            Controls.reset_state()

        current_time = pygame.time.get_ticks()

        # Animate blur transition
        if not Controls.transition_finished:
            background_change_interval = 25  # milliseconds
            if current_time - Controls.last_background_change > background_change_interval and \
                Controls.current_background_idx < len(Controls.backgrounds) - 1:
                Controls.current_background_idx += 1
                Controls.last_background_change = current_time
            if Controls.current_background_idx == len(Controls.backgrounds) - 1:
                Controls.transition_finished = True

        current_background = pygame.transform.scale(
            Controls.backgrounds[Controls.current_background_idx], (display_surface.get_width(), display_surface.get_height())
        )    
        display_surface.blit(current_background, (0, 0))

        mouse_position = pygame.mouse.get_pos()

        title_font = get_pixel_font(45)
        title_font.set_bold(True)
        title_font.set_underline(True)

        controls_font = get_pixel_font(25)
        
        title_text = title_font.render("Controls", True, text_base_color)
        title_rect = title_text.get_rect(center=(display_surface.get_width() // 2, 70))
        display_surface.blit(title_text, title_rect)

        controls = {
            "Move Up": "W / Up",
            "Move Down": "S / Down",
            "Move Left": "A / Left",
            "Move Right": "D / Right",
            "Base Attack": "Space",
            "Spell Attack": "X",
            "Rest": "R",
            "Consume Healing Potion": "H",
            "Consume Mana Potion": "M",
            "Change Main Weapon": "T",
            "Change Secondary Weapon": "Y",
            "Swap Weapons" : "U",
            "Create Beacon": "L"
        }

        y_offset = 130
        action_x = display_surface.get_width() // 2 - 330
        key_x = display_surface.get_width() // 2 + 200

        for action, key in controls.items():
            action_text = controls_font.render(f"{action}:", True, text_base_color)
            action_rect = action_text.get_rect(topleft=(action_x, y_offset))
            display_surface.blit(action_text, action_rect)

            key_text = controls_font.render(key, True, text_base_color)
            key_rect = key_text.get_rect(topleft=(key_x, y_offset))
            display_surface.blit(key_text, key_rect)
            
            y_offset += 50

        back_button = Button(MapPosition(display_surface.get_width() // 2 - 532, 780), None, "Back", get_pixel_font(30), text_base_color, text_hovering_color)

        back_button.change_color(mouse_position)
        back_button.update(display_surface)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.check_for_input(mouse_position):
                    Controls.reset_state()
                    return previous_state
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Controls.reset_state()
                    return previous_state

        return "controls"
