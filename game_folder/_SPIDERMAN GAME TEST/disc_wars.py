import pygame
import sys
import math

class Disk(object):
    def __init__(self):
        self.image = pygame.image.load('SPRITES_BOSS/neutral_disk.png').convert_alpha()
        self.rect = ('x','y',100,100) # TODO: change values for x & y
        self.velocity = (0,0) # TODO: change values

    def update(self, time):
        self.rect.center += self.velocity * time