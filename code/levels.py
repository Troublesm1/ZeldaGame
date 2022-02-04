import pygame
from settings import *
from support import *
from tile import Tile
from player import Player
from debug import debug

class Level:
    def __init__(self):
    #GET THE DISPLAY SURFACE
        self.display_surface = pygame.display.get_surface()
    #SPRITE GROUP SET-UP
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprite = pygame.sprite.Group()
    #SPRITE SETUP
        self.create_map()

    def create_map(self):
        layouts = {
            'boundary': import_csv_layout('../map/map_FloorBlocks.csv'),
            'grass': import_csv_layout('../map/map_Grass.csv'),
            'object': import_csv_layout('../map/map_Objects.csv')
        }

        for style,layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            Tile((x,y), [self.obstacle_sprite],'invisible')
                        if style == 'grass':
                            # CREATE A GRASS TILE
                            pass

                        if style == 'object':
                            # CREATE OBJECT TILE
                            pass


        self.player = Player((2000, 1430), [self.visible_sprites],self.obstacle_sprite)

    def run(self):
        #UPDATE AND DRAW GAME
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        #SET-UP
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        #CREATING THE FLOOR
        self.floor_surf = pygame.image.load('../graphics/tilemap/ground.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))

    def custom_draw(self,player):
        #GETTING THE OFFSET
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        #DRAWING THE FLOOR
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf,floor_offset_pos)

        for sprite in sorted(self.sprites(),key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)



