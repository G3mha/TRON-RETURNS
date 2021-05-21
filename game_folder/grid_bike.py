"""
Programa do mini-game de Motos
Autor: Enricco Gemha
Data: 18/05/2021
"""

import random
import sys
import pygame
from configurations import derezzed_dir, blue_dir, yellow_dir, frames, screen_size, lightcicle_size

# Define o código RGB das cores que utilizadas
BLUE_MIDNIGHT = (0,0,30)
BLUE = (12,12,100)
BLUE_LIGHT = (0,0,195)
YELLOW_GOLD = (255,215,0)

# Define o nome desta página
page_title = "Corrida de motos"

class yellowLightCicle():
    def __init__(self, screen_size, yellow_dir, lightcicle_size):
        self.image = pygame.image.load(yellow_dir).convert_alpha()
        pygame.transform.scale(self.image, lightcicle_size, None)
        self.rect = self.image.get_rect()
        self.set_position(screen_size[1], random.randint(0, screen_size[0]))
        self.set_velocity() # VALOR TESTE
        self.direction = "DOWN"
        self.last_direction

    def set_position(self, x, y):
        self.position = pygame.math.Vector2(x, y)
    
    def set_velocity(self, vx, vy):
        self.velocity = pygame.math.Vector2(vx, vy)
    
    def update(self, time, direction):
        self.direction = direction
        if self.last_direction != self.direction:
            # TODO muda a posicao da sprite
            x = 
        self.position += self.velocity * time
        self.last_direction = direction

class blueLightCicle():
    def __init__(self):
        self.image = pygame.image.load(blue_dir).convert_alpha()
        pygame.transform.scale(self.image, lightcicle_size, None)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.set_position(0, random.randint(0, random.randplayable_area_size[1])) # VALOR TESTE
        self.velocity = 0.4 # VALOR TESTE

    def set_position(self, x, y):
        self.position = pygame.math.Vector2(x,y)

    def update(self, time, direction):
        self.position += self.velocity * time
    
    def direction(self):
        e


# Rotina Inicial do jogo
pygame.init()  # inicializa as rotinas do PyGame
surface = pygame.display.set_mode(screen_size) # cria a tela do jogo com tamanho personalizado
pygame.display.set_caption(page_title) # título da janela do jogo

# Rotinas da tela estática
surface.fill(BLUE)
thickness = 15  # VALOR TESTE
# Desenha borda da tela
pygame.draw.line(surface, BLUE_MIDNIGHT, (0,0), (screen_size[0],0), thickness)
pygame.draw.line(surface, BLUE_MIDNIGHT, (0,0), (0,screen_size[1]), thickness)
pygame.draw.line(surface, BLUE_MIDNIGHT, screen_size, (screen_size[0],0), thickness)
pygame.draw.line(surface, BLUE_MIDNIGHT, screen_size, (0,screen_size[1]), thickness)
static_horizontal = 1024/6 # espaço entre cada quadrado
static_vertical = 768/6 # espaço entre cada quadrado
for static_lines in range(1,9):
    pygame.draw.line(surface, BLUE_MIDNIGHT, (0,(static_lines*static_horizontal)), (1024,(static_lines*static_horizontal)), thickness) # linha horizontal
    pygame.draw.line(surface, BLUE_MIDNIGHT, ((static_lines*static_vertical),0), ((static_lines*static_vertical),768), thickness) # linha vertical

# Rotinas de aúdio
pygame.mixer.music.load(derezzed_dir)
pygame.mixer.music.set_volume(0.04)  # VALOR TESTE
pygame.mixer.music.play(-1)  # VALOR TESTE

# Início do main Loop
game = True
while game:
    # Adquire todos os eventos e os testa para casos desejados
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT: # quebra o loop
            game = False
    
    pygame.display.update() # atualiza o display

pygame.quit() # encerra o pygame