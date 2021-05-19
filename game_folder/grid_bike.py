"""
Programa do mini-game de Motos
Autor: Enricco Gemha
Data: 18/05/2021
"""

import random
import sys
import pygame
from os import path

# Estabelece a pasta que contem as figuras e sons.
blue_lightcicle_dir = path.join(path.dirname(__file__), 'SPRITE_TRON_LIGHTCICLE_blue.png')

# Algumas variáveis essenciais para a aplicação
screen_size = (1024,768)  # Largura e altura da tela
playable_area_size = (700,498)  # Largura e altura da área jogável
lightcicle_size = (20,50)
page_title = "Corrida de motos"

# Define o código RGB das cores que utilizadas
BLACK = (0,0,0)
BLUE_MIDNIGHT = (25,25,112)
BLUE_LIGHT = (0,0,235)
YELLOW_GOLD = (255,215,0)

class blueLightCicle():
    def __init__(self):
        self.image = pygame.image.load("SPRITE_TRON_LIGHTCICLE_blue.png").convert_alpha()
        pygame.transform.scale(self.image, lightcicle_size, None)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.set_position(playable_area_size[0], playable_area_size[1])  # VALOR TESTE
        self.velocity = 0.4  # VALOR TESTE

    def set_position(self, x, y):
        self.position = pygame.math.Vector2(x,y)

    def update(self, time, direction):
        self.position += self.velocity * time

# Rotina Principal do jogo
pygame.init()  # inicializa as rotinas do PyGame
surface = pygame.display.set_mode(screen_size)  # cria a tela do jogo com tamanho personalizado
pygame.display.set_caption(page_title)  # título da janela do jogo

# Rotinas de aúdio
pygame.mixer.music.load("Derezzed.mp3")
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1)
shot_sound = pygame.mixer.Sound("preview.mp3")

font = pygame.font.Font(pygame.font.get_default_font(), 18)  # fonte para o placar
font_paused = pygame.font.Font(pygame.font.get_default_font(), 40)  # fonte para o aviso de pausado