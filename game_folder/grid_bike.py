"""
Programa do mini-game de Motos
Autor: Enricco Gemha
Data: 18/05/2021
"""

import random
import sys
import pygame

BLACK = (0,0,0)  # código rgb para preto
BLUE_MIDNIGHT = (25,25,112)  # código rgb para azul escuro
BLUE_LIGHT = (0,0,235)  # código rgb para azul claro
YELLOW_GOLD = (255,215,0)  # código rgb para amarelo

class blueLightCicle(pygame.sprite.Sprite):
    def __init__(self, group, surface):
        super().__init__(group)
        self.image = pygame.image.load("SPRITE_TRON_LIGHTCICLE_blue").convert_alpha()
        pygame.transform.scale(self.image, (largura, altura), None)  # TODO
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.set_position(0,0)
        self.set_velocity(0.2, 0.27)

    def set_position(self, x, y):
        self.position = pygame.math.Vector2(x,y)
    
    def set_velocity(self, vx, vy):
        self.velocity = pygame.math.Vector2(vx, vy)

    def update(self, time):
        width, height = pygame.display.get_surface().get_size()
        self.position += self.velocity * time
        self.rect.topleft = self.position
        # regula o movimento do Spider Man horizontalmente, para que ele não saia da tela
        if self.rect.right > width:
            self.velocity[0] = -abs(self.velocity[0])
            self.rect.right = width
        elif self.rect.x < 0:
            self.velocity[0] = abs(self.velocity[0])
            self.rect.x = 0
        # regula o movimento do Spider Man verticalmente, para que ele não saia da tela
        if self.rect.bottom > height:
            self.velocity[1] = -abs(self.velocity[1])
            self.rect.bottom = height
        elif self.rect.y < 0:
            self.velocity[1] = abs(self.velocity[1])
            self.rect.y = 0

pygame.init()  # inicializa as rotinas do PyGame
surface = pygame.display.set_mode((500,500), pygame.RESIZABLE)  # cria a tela do jogo com tamanho personalizado
pygame.display.set_caption("Spider Man Game")