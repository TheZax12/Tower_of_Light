import pygame
from sys import exit

import main.GameWindow

pygame.init()

# Setting a clock
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()

    # Draw the tiles
    pygame.display.update()

    # Setting the frame rate
    clock.tick(60)
