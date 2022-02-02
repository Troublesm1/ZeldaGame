import pygame
from settings import *

class Level:

    def __init__(self):
    #GET THE DISPLAY SURFACE
        self.display_surface = pygame.display.get_surface()
    #SPRITE GROUP SET-UP
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()
    #SPRITE SETUP
        self.create_map()

    def create_map(self):
        for row in WORLD_MAP:
            print(row)


    def run(self):
        #UPDATE AND DRAW GAME
        pass
