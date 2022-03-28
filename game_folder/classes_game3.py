import sys
import pygame
import random
import numpy as np
from classes_game1 import *
from classes_game2 import *
from functions import *


VELOCITY_FAST, VELOCITY_LOW = 0.2, 0.1


class yellowLightCicle(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.size_vert = (32,80)
        self.size_horiz = (80,32)
        self.image = pygame.image.load('SPRITES/SPRITE_TRON_LIGHTCICLE_yellowLEFT.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size_horiz)
        self.rect = self.image.get_rect()
        self.set_position(400,200)
        self.set_velocity(-VELOCITY_FAST, 0)
        self.direction = "LEFT"
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
    
    def update_direction(self, direction):
        if direction != self.direction: # direção mudou
            position = self.rect.center
            position_dict = {"UP":'SPRITES/SPRITE_TRON_LIGHTCICLE_yellowDOWN.png', "DOWN":'SPRITES/SPRITE_TRON_LIGHTCICLE_yellowUP.png', "LEFT":'SPRITES/SPRITE_TRON_LIGHTCICLE_yellowLEFT.png', "RIGHT":'SPRITES/SPRITE_TRON_LIGHTCICLE_yellowRIGHT.png'}
            velocity_dict = {"UP":[0, VELOCITY_FAST], "DOWN":[0, -VELOCITY_FAST], "LEFT":[-VELOCITY_FAST, 0], "RIGHT":[VELOCITY_FAST, 0]}
            self.image = pygame.image.load(position_dict[direction]).convert_alpha()
            if direction == "LEFT" or direction == "RIGHT":
                self.image = pygame.transform.scale(self.image, self.size_horiz)
            else:
                self.image = pygame.transform.scale(self.image, self.size_vert)
            self.set_velocity(velocity_dict[0], velocity_dict[1])
            self.rect = self.image.get_rect()
            self.rect.center = position
            self.direction = direction

    def update(self, time):
        self.rect.center = tuple(np.add(self.rect.center, tuple(np.array(self.velocity) * time)))
        self.trace.append(self.rect.center)
        width, height = pygame.display.get_surface().get_size()
        # regula o movimento do disco horizontalmente, para que ele não saia da tela
        if self.rect.right > width:
            self.explode = True
        elif self.rect.x < 0:
            self.explode = True
        # regula o movimento do disco verticalmente, para que ele não saia da tela
        if self.rect.bottom > height:
            self.explode = True
        elif self.rect.y < 0:
            self.explode = True

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


class blueLightCicle(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.size_vert = (32,80)
        self.size_horiz = (80,32)
        self.image = pygame.image.load('SPRITES/SPRITE_TRON_LIGHTCICLE_blueRIGHT.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size_horiz)
        self.rect = self.image.get_rect()
        self.set_position(100,400)
        self.set_velocity(0.2,0) # VALOR TESTE
        self.direction = "RIGHT"
        self.trace = []
        self.explode = False

    def set_position(self, x, y):
        self.rect.center = pygame.math.Vector2(x, y)
    
    def set_velocity(self, vx, vy):
        self.velocity = pygame.math.Vector2(vx, vy)
    
    def update_direction(self, direction):
        if direction != self.direction: # direção mudou
            position = self.rect.center
            position_dict = {"UP":'SPRITES/SPRITE_TRON_LIGHTCICLE_blueDOWN.png', "DOWN":'SPRITES/SPRITE_TRON_LIGHTCICLE_blueUP.png', "LEFT":'SPRITES/SPRITE_TRON_LIGHTCICLE_blueLEFT.png', "RIGHT":'SPRITES/SPRITE_TRON_LIGHTCICLE_blueRIGHT.png'}
            velocity_dict = {"UP":[0, VELOCITY_FAST], "DOWN":[0, -VELOCITY_FAST], "LEFT":[-VELOCITY_FAST, 0], "RIGHT":[VELOCITY_FAST, 0]}
            self.image = pygame.image.load(position_dict[direction]).convert_alpha()
            if direction == "LEFT" or direction == "RIGHT":
                self.image = pygame.transform.scale(self.image, self.size_horiz)
            else:
                self.image = pygame.transform.scale(self.image, self.size_vert)
            self.set_velocity(velocity_dict[0], velocity_dict[1])
            self.rect = self.image.get_rect()
            self.rect.center = position
            self.direction = direction

    def update(self, time):
        print(self.velocity)
        self.rect.center = tuple(np.add(self.rect.center, tuple(np.array(self.velocity) * time)))
        self.trace.append(self.rect.center)
        width, height = pygame.display.get_surface().get_size()
        # regula o movimento do disco horizontalmente, para que ele não saia da tela
        if self.rect.right > width:
            self.explode = True
        elif self.rect.x < 0:
            self.explode = True
        # regula o movimento do disco verticalmente, para que ele não saia da tela
        if self.rect.bottom > height:
            self.explode = True
        elif self.rect.y < 0:
            self.explode = True
    
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
