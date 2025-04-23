import pygame

from gameMap.MapSettings import *


screen_width = map_width * tile_size
""" The width of the game window """

screen_height = map_height * tile_size
""" The height of the game window """

log_width = 400
""" The width of the log panel """

log_height = screen_height
""" The height of the log panel """

def get_pixel_font(size):
    return pygame.font.Font("assets/Grand9K_Pixel.ttf", size)