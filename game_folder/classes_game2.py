import sys
import pygame
import random
import numpy as np
from classes_game1 import *
from classes_game3 import *
from functions import *

SIZE_DISK = (30,28) # tamanho da sprite

class Disk(pygame.sprite.Sprite):
    """
    Uma classe usada para representar um disco azul ou amarelo
    ...
    Atributos
    ----------
    self.mask : pygame.Mask
        a máscara da imagem do objeto
    colour : str
        a cor do disco
    self.image : pygame.Image
        a imagem do objeto
    self.angle_list : list
        a lista de velocidades angulares possíveis do objeto
    self.rect : pygame.Rect
        a posição e tamanho da imagem do objeto
    height, width: int
        respectivamente, a largura e altura da tela 
    Métodos
    -------
    set_velocity(self, vx, vy)
        Define a velocidade do objeto
    update(self, time)
        Define a nova posição, utilizando a velocidade e o tempo que passou desde a última chamada
    """
    def __init__(self, group, colour, character_rect, angle_index):
        super().__init__(group)
        self.image = pygame.image.load(f'SPRITES_BOSS/disk_{colour}.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, SIZE_DISK)
        factor = {"yellow":-1, "blue":1}
        self.rect = pygame.Rect(character_rect[0]+factor[colour]*SIZE_DISK[0], character_rect[1]+factor[colour]*SIZE_DISK[1], SIZE_DISK[0], SIZE_DISK[1])
        self.angle_list = [(factor[colour]*VELOCITY_FAST,-VELOCITY_FAST), (factor[colour]*VELOCITY_FAST,-VELOCITY_FAST/2), (factor[colour]*VELOCITY_FAST,0), (factor[colour]*VELOCITY_FAST,VELOCITY_FAST/2), (factor[colour]*VELOCITY_FAST,VELOCITY_FAST)]
        self.set_velocity(self.angle_list[angle_index][0], self.angle_list[angle_index][1])
        self.mask = pygame.mask.from_surface(self.image)

    def set_velocity(self, vx, vy):
        self.velocity = pygame.math.Vector2(vx, vy)

    def update(self, time):
        self.rect.center = ((self.rect.center[0] + (self.velocity[0] * time)), (self.rect.center[1] + (self.velocity[1] * time)))
        width, height = pygame.display.get_surface().get_size()
        # regula o movimento do disco horizontalmente, para que ele não saia da tela
        if self.rect.right > width:
            self.set_velocity(-abs(self.velocity[0]), self.velocity[1])
            self.rect.right = width
        elif self.rect.x < 0:
            self.set_velocity(abs(self.velocity[0]), self.velocity[1])
            self.rect.x = 0
        # regula o movimento do disco verticalmente, para que ele não saia da tela
        if self.rect.bottom > height:
            self.set_velocity(self.velocity[0], -abs(self.velocity[1]))
            self.rect.bottom = height
        elif self.rect.y < 0:
            self.set_velocity(self.velocity[0], abs(self.velocity[1]))
            self.rect.y = 0

class Player(pygame.sprite.Sprite):
    def __init__(self, group, colour):
        super().__init__(group)
        self.colour = colour
        if colour == "yellow":
            self.image = pygame.image.load('SPRITES_BOSS/boss_sem_disco.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (50,88))
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(500,700),random.randint(100,700))
        if colour == "blue":
            self.image = pygame.image.load('SPRITES_BOSS/normal_sem_disco.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (50,88))
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(100,300),random.randint(100,700))
        self.mask = pygame.mask.from_surface(self.image)
        self.set_velocity(0,0)
    
    def set_velocity(self, vx, vy):
        self.velocity = pygame.math.Vector2(vx, vy)

    def game_controls(self, event):
        if self.colour == "blue":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.set_velocity(self.velocity[0], 0.2)
                if event.key == pygame.K_w:
                    self.set_velocity(self.velocity[0], -0.2)
                if event.key == pygame.K_a:
                    self.set_velocity(-0.2, self.velocity[1])
                if event.key == pygame.K_d:
                    self.set_velocity(0.2, self.velocity[1])
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s or event.key == pygame.K_w:
                    self.set_velocity(self.velocity[0], 0)
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    self.set_velocity(0, self.velocity[1])
        if self.colour == "yellow":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.set_velocity(self.velocity[0], 0.2)
                if event.key == pygame.K_UP:
                    self.set_velocity(self.velocity[0], -0.2)
                if event.key == pygame.K_LEFT:
                    self.set_velocity(-0.2, self.velocity[1])
                if event.key == pygame.K_RIGHT:
                    self.set_velocity(0.2, self.velocity[1])
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    self.set_velocity(self.velocity[0], 0)
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    self.set_velocity(0, self.velocity[1])

    def update(self, time):
        self.rect.center = ((self.rect.center[0] + (self.velocity[0] * time)), (self.rect.center[1] + (self.velocity[1] * time)))
        width, height = pygame.display.get_surface().get_size()
        # cria barreira invisível, para que o Jogador não saia da tela
        if self.rect.right > width:
            self.rect.right = width
        elif self.rect.x < 0:
            self.rect.x = 0
        # cria barreira invisível, para que o Jogador não saia da tela
        if self.rect.bottom > height:
            self.rect.bottom = height
        elif self.rect.y < 0:
            self.rect.y = 0
