import pygame
from sys import exit

from UI.Colors import *
from gameMap.MapSettings import *

from main.GameWindow import GameWindow
from entities.Player import Player
from gameMap.MapPosition import MapPosition
from gameMap.tiles.TileManager import TileManager
from items.ItemManager import ItemManager


pygame.init()

# Game Window
game_window = GameWindow(2400, 1350, 300)
screen_width, screen_height = game_window.screen_width, game_window.screen_height

# Display surface
display_surface = game_window.create_display_surface()
pygame.display.set_caption('Tower of Light')

# Map
game_map = TileManager()
game_map.map_load(1)

# Items
item_manager = ItemManager()

# Initialize player
player = Player(southwest)
player_tile_x, player_tile_y = player.get_position().x, player.get_position().y
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
            player.motion(event, player_tile_x, player_tile_y, map_width, map_height, game_map.map_tiles)
            player_tile_x, player_tile_y = player.get_position().x, player.get_position().y
            player_rect.topleft = (player_tile_x * tile_size, player_tile_y * tile_size)

            player.actions(event, game_map)
            
    display_surface.fill(background_color)

    # Update the visibility
    game_map.tile_vilibility(player)
    item_manager.item_visibility(player)

    # Draw the map
    game_map.draw_map(display_surface)

    # Draw the player
    pygame.draw.rect(display_surface, player_color, player_rect)
    pygame.draw.rect(display_surface, (0, 0, 0), player_rect, 1)

    # Draw the items
    item_manager.draw_item(display_surface)

    # Update the display
    pygame.display.update()

    # Setting the frame rate
    clock.tick(60)
