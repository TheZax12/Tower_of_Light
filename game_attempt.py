import pygame
from sys import exit

from UI.Colors import Colors
from gameMap.MapSettings import MapSettings
from entities.Player import Player


# def check_collision(new_rect, tiles):d
#     for tile_type, tile_rect in tiles:
#         if tile_type == "wall" and new_rect.colliderect(tile_rect):
#             return True
#     return False

player = Player()

pygame.init()

# Window, Screen, Map settings
WINDOW_WIDTH, WINDOW_HEIGHT = 2400, 1350
screen_width, screen_height = MapSettings.map_width * MapSettings.tile_size, MapSettings.map_height * MapSettings.tile_size

# Game log size
game_log_size = 300

# Reading the map from txt file
file_path = 'gameMap/levels/level_1.txt'

with open(file_path, "r") as file:
    level_data = file.readlines()

# display_surface = pygame.display.set_mode((scaled_screen_width + game_log_size, scaled_screen_height))
display_surface = pygame.display.set_mode((screen_width + game_log_size, screen_height))
pygame.display.set_caption('Tower of Light')

tiles = []

for y, row in enumerate(level_data):
    row = row.strip().split(' ')
    for x, tile in enumerate(row):
        if tile == '1':
            tiles.append(("wall", pygame.Rect(x * MapSettings.tile_size, y * MapSettings.tile_size, MapSettings.tile_size, MapSettings.tile_size)))
        elif tile == '0':
            tiles.append(("floor", pygame.Rect(x * MapSettings.tile_size, y * MapSettings.tile_size, MapSettings.tile_size, MapSettings.tile_size)))

# Player settings
player_start_tile_x, player_start_tile_y = 5, 48
player_tile_x, player_tile_y = player_start_tile_x, player_start_tile_y
player_rect = pygame.Rect(player_tile_x * MapSettings.tile_size, player_tile_y * MapSettings.tile_size, MapSettings.tile_size, MapSettings.tile_size)

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
            new_x, new_y, new_rect = player.motion(event, player_tile_x, player_tile_y, MapSettings.map_width, MapSettings.map_height)

            if not player.check_collision(new_rect, tiles):
                player_tile_x, player_tile_y = new_x, new_y
                player_rect.topleft = (player_tile_x * MapSettings.tile_size, player_tile_y * MapSettings.tile_size)

    display_surface.fill(Colors.background_color)

    # Draw the tiles
    for tile_type, tile_rect in tiles:
        if tile_type == "wall":
            pygame.draw.rect(display_surface, Colors.chaos_wall_tile_visible_color, tile_rect)
        elif tile_type == "floor":
            pygame.draw.rect(display_surface, Colors.chaos_floor_tile_visible_color, tile_rect)

    # Draw the player
    pygame.draw.rect(display_surface, Colors.player_color, player_rect)

    # Draw the grid
    for x in range(0, screen_width + MapSettings.tile_size, MapSettings.tile_size):
        pygame.draw.line(display_surface, Colors.grid_color, (x, 0), (x, screen_height))
    for y in range(0, screen_height + MapSettings.tile_size, MapSettings.tile_size):
        pygame.draw.line(display_surface, Colors.grid_color, (0, y), (screen_width, y))

    pygame.display.update()

    # Setting the frame rate
    clock.tick(60)
