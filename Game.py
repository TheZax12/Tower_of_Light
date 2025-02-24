import pygame
from sys import exit

from UI.Colors import *
from gameMap.MapSettings import *

from main.GameWindow import GameWindow
from entities.Player import Player
from gameMap.MapPosition import MapPosition
from gameMap.MapCreation import MapCreation


pygame.init()

# Game Window
game_window = GameWindow(2400, 1350, 300)
screen_width, screen_height = game_window.screen_width, game_window.screen_height

# Display surface
display_surface = game_window.create_display_surface()
pygame.display.set_caption('Tower of Light')

# Map
game_map = MapCreation()
game_map.map_load(1)

# Initialize player position
player_pos = MapPosition(5, 48)

# Initialize player
player = Player(player_pos)
player_start_tile_x, player_start_tile_y = player.get_position().x, player.get_position().y
player_tile_x, player_tile_y = player_start_tile_x, player_start_tile_y
player_rect = pygame.Rect(player_tile_x * tile_size, player_tile_y * tile_size, tile_size, tile_size)

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
            new_x, new_y, new_rect = player.motion(event, player_tile_x, player_tile_y, map_width, map_height)

            if not player.check_collision(new_rect, game_map.map_tiles):
                player.set_position(MapPosition(new_x, new_y))
                player_tile_x, player_tile_y = new_x, new_y
                player_rect.topleft = (player_tile_x * tile_size, player_tile_y * tile_size)

    display_surface.fill(background_color)

    # Update the visibility of the tiles
    game_map.tile_vilibility(player)

    # Draw the map
    game_map.draw_map(display_surface)

    # Draw the player
    pygame.draw.rect(display_surface, player_color, player_rect)

    # Draw the grid
    game_map.draw_grid(display_surface)

    # Update the display
    pygame.display.update()

    # Setting the frame rate
    clock.tick(60)
