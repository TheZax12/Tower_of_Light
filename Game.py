import pygame
from sys import exit

from UI.Colors import *
from gameMap.MapSettings import *

from main.GameWindow import GameWindow
from entities.Player import Player
from gameMap.tiles.TileManager import TileManager


pygame.init()

# Game Window
game_window = GameWindow(2400, 1350, 300)
screen_width, screen_height = game_window.screen_width, game_window.screen_height

# Display surface
display_surface = game_window.create_display_surface()
pygame.display.set_caption('Tower of Light')

# Map
game_map = TileManager()
game_map.map_load()

# Initialize player
player = Player(southwest)

# Setting a clock
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()

        elif event.type == pygame.KEYDOWN:
            player.motion(event, map_width, map_height, game_map.map_tiles)
            player.actions(event, game_map)
            
    display_surface.fill(background_color)

    # Update the visibility
    game_map.tile_vilibility(player)

    # Draw the map
    game_map.draw_map(display_surface)
    
    # Update levels
    game_map.advance_level(player)

    # Draw the player
    pygame.draw.rect(display_surface, player_color, player.rect)
    pygame.draw.rect(display_surface, (0, 0, 0), player.rect, 1)

    # Update the display
    pygame.display.update()

    # Setting the frame rate
    clock.tick(60)
