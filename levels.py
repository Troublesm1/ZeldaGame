import pygame

class Level:
    def __init__(self):
    #GET THE DISPLAY SURFACE
        self.display_surface = pygame.display.get_surface()

    #SPRITE SET-UP
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

    def run(self):
        #UPDATE AND DRAW GAME
        pass
