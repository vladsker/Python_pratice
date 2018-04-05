import sys
import pygame
from settings import Settings

def run_game():
    
    #Screen initialisation 
    pygame.init()
    pygame.display.set_caption("Alien invasion.")

    #Setting initialisation
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    
    while True:
        screen.fill(ai_settings.bg_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        pygame.display.flip()

run_game()
