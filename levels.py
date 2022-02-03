import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug

class Level:

    def __init__(self):
    #GET THE DISPLAY SURFACE
        self.display_surface = pygame.display.get_surface()
    #SPRITE GROUP SET-UP
        self.visible_sprites = YSortCameraGroup()
        self.obstacles_sprites = pygame.sprite.Group()
    #SPRITE SETUP
        self.create_map()

    def create_map(self):
        for row_index,row in enumerate(WORLD_MAP):
            for col_index,col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x,y),[self.visible_sprites,self.obstacles_sprites])
                if col == 'p':
                    self.player = Player((x,y),[self.visible_sprites],self.obstacles_sprites)

    def run(self):
        #UPDATE AND DRAW GAME
        self.visible_sprites.custom_draw()
        self.visible_sprites.update()

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        #SET-UP
        super().__init__()
        self.display_surface = pygame.display.get_surface()

    def custom_draw(self):
        for sprite in self.sprites():
            self.display_surface.blit(sprite.image,sprite.rect)


