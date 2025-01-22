import pygame
from sys import exit

pygame.init()

# Screen chars
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

# Fonts
font = pygame.font.Font(None, 74)
small_font = pygame.font.SysFont(None, 50)

# Menu Options
menu_options = ["Play", "Quit"]
selected_option = 0
option_rects = []


def draw_menu(width, height):
    screen.fill((0, 0, 0))
    title_text = font.render("Main Menu", False, (0, 255, 0))
    screen.blit(title_text, (width // 2 - title_text.get_width() // 2, height // 6))

    options_rects = []
    for i, option in enumerate(menu_options):
        color = (0, 0, 255) if i == selected_option else (255, 255, 255)
        menu_text = small_font.render(option, False, color)
        text_x = width // 2 - menu_text.get_width() // 2
        text_y = height // 3 + i * 60
        screen.blit(menu_text, (text_x, text_y))

        options_rects.append(pygame.Rect(text_x, text_y, menu_text.get_width(), menu_text.get_height()))

    pygame.display.flip()
    return options_rects


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_option = (selected_option - 1) % len(menu_options)
            if event.key == pygame.K_DOWN:
                selected_option = (selected_option + 1) % len(menu_options)
            if event.key == pygame.K_RETURN:
                if selected_option == 0:  # Play
                    print("Starting game...")  # Probably here goes a function to start the game
                elif selected_option == 1:  # Quit
                    running = False
                    pygame.quit()
                    exit()

        if event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            for j, option_rect in enumerate(option_rects):
                if option_rect.collidepoint(mouse_pos):
                    selected_option = j

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for j, option_rect in enumerate(option_rects):
                if option_rect.collidepoint(mouse_pos):
                    selected_option = j
                    if selected_option == 0:  # Play
                        print("Starting game...")
                    elif selected_option == 1:  # Quit
                        running = False
                        pygame.quit()
                        exit()

        if event.type == pygame.VIDEORESIZE:
            screen_width, screen_height = event.w, event.h
            screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

    option_rects = draw_menu(screen_width, screen_height)
