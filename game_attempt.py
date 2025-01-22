import pygame
from sys import exit
from UI.Colors import Colors


def calculate_scaling(window_width, window_height):
    scaling_factor = min(window_width / SCREEN_WIDTH, window_height / SCREEN_HEIGHT)
    scaled_tile_size = int(TILE_SIZE * scaling_factor)
    scaled_screen_width = MAP_WIDTH * scaled_tile_size
    scaled_screen_height = MAP_HEIGHT * scaled_tile_size
    return scaling_factor, scaled_tile_size, scaled_screen_width, scaled_screen_height


def check_collision(new_rect, tiles):
    for tile_type, tile_rect in tiles:
        if tile_type == "wall" and new_rect.colliderect(tile_rect):
            return True
    return False


pygame.init()

# Window, Screen, Map settings
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
MAP_WIDTH, MAP_HEIGHT = 52, 52
TILE_SIZE = 16
SCREEN_WIDTH, SCREEN_HEIGHT = MAP_WIDTH * TILE_SIZE, MAP_HEIGHT * TILE_SIZE

# Game log size
game_log_size = 300

# Reading the map from txt file
file_path = 'gameMap/levels/level_1.txt'

with open(file_path, "r") as file:
    level_data = file.readlines()

scaling_factor, scaled_tile_size, scaled_screen_width, scaled_screen_height = calculate_scaling(WINDOW_WIDTH,
                                                                                                WINDOW_HEIGHT)

display_surface = pygame.display.set_mode((scaled_screen_width + game_log_size, scaled_screen_height))
pygame.display.set_caption('Tower of Light')

tiles = []

for y, row in enumerate(level_data):
    row = row.strip().split(' ')
    for x, tile in enumerate(row):
        if tile == '1':
            tiles.append(("wall", pygame.Rect(x * scaled_tile_size, y * scaled_tile_size, scaled_tile_size,
                                              scaled_tile_size)))
        elif tile == '0':
            tiles.append(("floor", pygame.Rect(x * scaled_tile_size, y * scaled_tile_size, scaled_tile_size,
                                               scaled_tile_size)))

# Player settings
player_start_tile_x, player_start_tile_y = 5, 48
player_tile_x, player_tile_y = player_start_tile_x, player_start_tile_y
player_rect = pygame.Rect(player_tile_x * scaled_tile_size, player_tile_y * scaled_tile_size,
                          scaled_tile_size, scaled_tile_size)

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
            new_tile_x, new_tile_y = player_tile_x, player_tile_y
            if event.key == pygame.K_w and player_tile_y > 0:
                new_tile_y -= 1
            elif event.key == pygame.K_s and player_tile_y < MAP_HEIGHT - 1:
                new_tile_y += 1
            elif event.key == pygame.K_a and player_tile_x > 0:
                new_tile_x -= 1
            elif event.key == pygame.K_d and player_tile_x < MAP_WIDTH - 1:
                new_tile_x += 1

            new_rect = pygame.Rect(new_tile_x * scaled_tile_size, new_tile_y * scaled_tile_size,
                                   scaled_tile_size, scaled_tile_size)
            if not check_collision(new_rect, tiles):
                player_tile_x, player_tile_y = new_tile_x, new_tile_y
                player_rect.topleft = (player_tile_x * scaled_tile_size, player_tile_y * scaled_tile_size)

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
    for x in range(0, scaled_screen_width + scaled_tile_size, scaled_tile_size):
        pygame.draw.line(display_surface, Colors.grid_color, (x, 0), (x, scaled_screen_height))
    for y in range(0, scaled_screen_height + scaled_tile_size, scaled_tile_size):
        pygame.draw.line(display_surface, Colors.grid_color, (0, y), (scaled_screen_width, y))

    pygame.display.update()

    # Setting the frame rate
    clock.tick(60)
