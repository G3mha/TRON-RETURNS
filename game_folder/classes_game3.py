import sys
import pygame
import random
import numpy as np
from classes_game1 import *
from classes_game2 import *
from functions import *


VELOCITY_FAST, VELOCITY_LOW = 0.2, 0.1
SIZE_HORIZ, SIZE_VERT = (80,32), (32,80)

class LightCicle(pygame.sprite.Sprite):
    def __init__(self, group, direction, color, position, velocity):
        super().__init__(group)
        self.direction = direction
        self.color = color
        self.set_velocity(velocity[0], velocity[1])
        self.set_position(position[0], position[1])
        self.sprite_label = f'SPRITES/SPRITE_TRON_LIGHTCICLE_{self.color}{self.direction}.png'
        self.image = pygame.image.load(self.sprite_label).convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size_horiz)
        self.rect = self.image.get_rect()
        self.trace = []
        self.explode = False

    def set_position(self, x, y):
        self.rect.center = pygame.math.Vector2(x, y)
    
    def set_velocity(self, vx, vy):
        """
        Define a velocidade
        vx: velocidade no eixo x
        vy: velocidade no eixo y
        """
        self.velocity = pygame.math.Vector2(vx, vy)

    def update_direction(self, direction, color):
        if direction != self.direction: # direção mudou
            position = self.rect.center
            velocity_dict = {"UP":[0, VELOCITY_FAST], "DOWN":[0, -VELOCITY_FAST], "LEFT":[-VELOCITY_FAST, 0], "RIGHT":[VELOCITY_FAST, 0]}
            self.image = pygame.image.load(f'SPRITES/SPRITE_TRON_LIGHTCICLE_{color}{direction}.png').convert_alpha()
            if direction == "LEFT" or direction == "RIGHT":
                self.image = pygame.transform.scale(self.image, SIZE_HORIZ)
            else:
                self.image = pygame.transform.scale(self.image, SIZE_VERT)
            self.set_velocity(velocity_dict[direction][0], velocity_dict[direction][1])
            self.rect = self.image.get_rect()
            self.rect.center = position
            self.direction = direction

    def slow_down(self):
        vel_fast, vel_low = VELOCITY_FAST, VELOCITY_LOW
        if self.direction == "DOWN" or self.direction == "LEFT":
            vel_fast, vel_low = -vel_fast, -vel_low
        vel_new = []
        for vel in self.velocity:
            if vel == vel_fast:
                vel = vel_low
            elif vel == vel_low:
                vel = vel_fast
            vel_new.append(vel)
        self.set_velocity(vel_new[0], vel_new[1])

    def update(self, time):
        self.rect.center = tuple(np.add(self.rect.center, tuple(np.array(self.velocity) * time)))
        self.trace.append(self.rect.center)
        width, height = pygame.display.get_surface().get_size()
        if self.rect.right > width: # regula o movimento da LightCycle horizontalmente, para que ele não saia da tela
            self.explode = True
        elif self.rect.x < 0:
            self.explode = True
        if self.rect.bottom > height: # regula o movimento da LightCycle verticalmente, para que ele não saia da tela
            self.explode = True
        elif self.rect.y < 0:
            self.explode = True
