import pygame
from sys import exit

from panels.MainMenu import MainMenu
from panels.GamePanel import GamePanel

from panels.PanelSettings import *
from gameMap.MapSettings import *
from UI.Colors import *


pygame.init()


game_window = GamePanel()

game_active = True
while game_active:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            game_active = False
            pygame.quit()
            exit()

    MainMenu.create_main_menu(game_window.display_surface, game_window.play, events)