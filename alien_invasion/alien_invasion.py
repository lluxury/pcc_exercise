import pygame

from settings import Settings


def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    
    # Start the main loop for the game.
    while True:
        screen.fill(ai_settings.bg_color)
        pygame.display.flip()


run_game()
