import pygame
import sys
import math

class Disk(object):
    def __init__(self, player_rect):
        self.rect = ('x','y','width','height') # TODO: change values
        self.velocity = (0,0) # TODO: change values
        self.images = []
        self.images.append(pygame.image.load('SPRITES_BOSS/disk_orange.png').convert_alpha())
        self.images.append(pygame.image.load('SPRITES_BOSS/disk_blue.png').convert_alpha())

    def define_color(self, colour):
        if colour == "orange":
            self.image = self.images[0]
        if colour == "blue":
            self.image = self.images[1]

    def update(self, time):
        self.rect.center += self.velocity * time
        