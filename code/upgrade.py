import pygame
from settings import *

class Upgrade:
    def __init__(self, player):
        # GENERAL SET-UP
        self.display_surface = pygame.display.get_surface()
        self.player = player

    def display(self):
        self.display_surface.fill('black')