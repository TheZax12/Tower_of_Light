import pygame
from sys import exit

from panels.MainMenu import MainMenu
from panels.GamePanel import GamePanel
from panels.EndScreen import EndScreen
from panels.Controls import Controls
from panels.CharacterCreationPanel import CharacterCreationPanel
from panels.PauseMenu import PauseMenu

from panels.PanelSettings import *
from gameMap.MapSettings import *
from UI.Colors import *


class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("The Tower of Light")
        self.display_surface = pygame.display.set_mode((screen_width + log_width, screen_height))
        self.clock = pygame.time.Clock()

        self.game_panel = None
        self.game_state = "main menu"
        self.previous_game_state = "main menu"
        
    def start_game(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            if self.game_state == "main menu":
                self.previous_game_state = "main menu"
                self.game_state = MainMenu.create_main_menu(self.display_surface, events)
            elif self.game_state == "character creation":
                result = CharacterCreationPanel.create_character_creation_panel(self.display_surface, events)
                if isinstance(result, tuple) and len(result) == 2:
                    race, warrior = result
                    self.game_panel = GamePanel(self.display_surface, race, warrior)
                    self.game_state = "gameplay"
                else:
                    self.game_state = result
            elif self.game_state == "gameplay":
                if self.game_panel:
                    for event in events:
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                self.game_state = "pause"
                    
                    if self.game_state == "gameplay":
                        self.game_panel.play(events)
                        if self.game_panel.is_win():
                            self.game_state = "win screen"
                        elif self.game_panel.is_game_over():
                            self.game_state = "lose screen"
            elif self.game_state == "pause":
                if self.game_panel:
                    self.game_panel.draw_game_state()
                
                result = PauseMenu.create_pause_menu(self.display_surface, events)
                if result == "controls":
                    self.previous_game_state = "pause"
                self.game_state = result
            elif self.game_state == "win screen":
                self.game_state = EndScreen.winning_screen(self.display_surface, events)
            elif self.game_state == "lose screen":
                self.game_state = EndScreen.losing_screen(self.display_surface, events)
            elif self.game_state == "controls":
                self.game_state = Controls.create_controls_panel(self.display_surface, events, self.previous_game_state)
            elif self.game_state == "quit":
                pygame.quit()
                exit()

            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.start_game()