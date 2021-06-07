import pygame
import sys
import math

BLUE_ICE = (0,255,251)
YELLOW_GOLD = (255,215,0)

class Disk(object):
    def __init__(self):
        self.image = pygame.image.load('SPRITES_BOSS/neutral_disk.png').convert_alpha()
        self.rect = ('x','y',100,100) # TODO: change values for x & y
        self.velocity = (0,0) # TODO: change values

    def update(self, time):
        self.rect.center += self.velocity * time

class Paddle(object):
    def __init__(self, colour, surface):
        if colour == "blue":
            pygame.draw.rect(surface, BLUE_ICE, (0,0,0,0)) # TODO: change values
        if colour == "yellow":
            pygame.draw.rect(surface, YELLOW_GOLD, (0,0,0,0)) # TODO: change values
        self.rect = ('x','y',100,100) # TODO: change values for x & y
        self.velocity = (0,0)

    def game_controls(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.velocity = (0,0) # TODO: change values
            elif event.key == pygame.K_UP:
                self.velocity = (0,0) # TODO: change values
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                self.velocity = (0,0)