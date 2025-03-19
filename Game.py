import pygame
from sys import exit

from panels.MainMenu import MainMenu
from panels.GameWindow import GameWindow

from panels.PanelSettings import *
from gameMap.MapSettings import *
from UI.Colors import *


pygame.init()


game_window = GameWindow()
game_window.create_display_surface()
game_window.set_caption("Tower of Light")

display_surface = game_window.get_display_surface()

game_active = True
while game_active:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            game_active = False
            pygame.quit()
            exit()
    
    MainMenu.create_main_menu(display_surface, events, game_window.play_game)