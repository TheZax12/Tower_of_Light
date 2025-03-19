import pygame

from gameMap.MapSettings import *


screen_width = map_width * tile_size
""" The width of the game window """

screen_height = map_height * tile_size
""" The height of the game window """

log_size = 400
""" The size of the log panel """

def get_font(size):
    return pygame.font.Font("assets/Grand9K_Pixel.ttf", size)