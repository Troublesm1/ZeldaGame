import pygame
from settings import *
from entity import Entity

class Enemy(Entity):
    def __init__(self, monster_name, pos, groups):

        # GENERAL SET-UP