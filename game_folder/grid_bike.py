"""
Programa do mini-game de Motos
Autor: Enricco Gemha
Data: 18/05/2021
"""

import random
import sys
import pygame
from configurations import derezzedSONG_dir, derezzedFX_dir, frames, screen_size, lightcicle_size, LEFTblue_dir,RIGHTblue_dir,UPblue_dir,DOWNblue_dir,LEFTyellow_dir,RIGHTyellow_dir,UPyellow_dir,DOWNyellow_dir

# Define o código RGB das cores que utilizadas
BLUE_MIDNIGHT = (0,0,30)
BLUE = (12,12,100)
BLUE_LIGHT = (0,0,195)
YELLOW_GOLD = (255,215,0)

# Define o nome desta página
page_title = "Corrida de motos"

class yellowLightCicle():
    def __init__(self, screen_size, LEFTyellow_dir, lightcicle_size):
        self.image = pygame.image.load(LEFTyellow_dir).convert_alpha()
        pygame.transform.scale(self.image, lightcicle_size, None)
        self.rect = self.image.get_rect()
        self.set_position(screen_size[0], random.randint(0, screen_size[1]))
        self.set_velocity(-0.4,0) # VALOR TESTE
        self.direction = "LEFT"
        self.trace = []

    def set_position(self, x, y):
        self.position = pygame.math.Vector2(x, y)
    
    def set_velocity(self, vx, vy):
        self.velocity = pygame.math.Vector2(vx, vy)
    
    def update_direction(self, direction):
        if direction != self.direction:
            if direction == "UP":
                self.image = pygame.image.load(UPyellow_dir).convert_alpha()
                self.set_velocity((0,0.4)) # VALOR TESTE
            if direction == "DOWN":
                self.image = pygame.image.load(DOWNyellow_dir).convert_alpha()
                self.set_velocity((0,-0.4)) # VALOR TESTE
            if direction == "LEFT":
                self.image = pygame.image.load(LEFTyellow_dir).convert_alpha()
                self.set_velocity((-0.4,0)) # VALOR TESTE
            if direction == "RIGHT":
                self.image = pygame.image.load(RIGHTyellow_dir).convert_alpha()
                self.set_velocity((0.4,0)) # VALOR TESTE
            self.direction = direction

    def update_position(self, time):
        self.last_position = self.position
        self.position += self.velocity * time
        if self.position != self.last_position:
            self.trace.append(self.position)

class blueLightCicle():
    def __init__(self, screen_size, RIGHTblue_dir, lightcicle_size):
        self.image = pygame.image.load(RIGHTblue_dir).convert_alpha()
        pygame.transform.scale(self.image, lightcicle_size, None)
        self.rect = self.image.get_rect()
        self.set_position(screen_size[0], random.randint(0, screen_size[1]))
        self.set_velocity(0.4,0) # VALOR TESTE
        self.direction = "RIGHT"

    def set_position(self, x, y):
        self.position = pygame.math.Vector2(x, y)
    
    def set_velocity(self, vx, vy):
        self.velocity = pygame.math.Vector2(vx, vy)
    
    def update_direction(self, direction):
        if direction != self.direction:
            if direction == "UP":
                self.image = pygame.image.load(UPblue_dir).convert_alpha()
                self.set_velocity((0,0.4)) # VALOR TESTE
            if direction == "DOWN":
                self.image = pygame.image.load(DOWNblue_dir).convert_alpha()
                self.set_velocity((0,-0.4)) # VALOR TESTE
            if direction == "LEFT":
                self.image = pygame.image.load(LEFTblue_dir).convert_alpha()
                self.set_velocity((-0.4,0)) # VALOR TESTE
            if direction == "RIGHT":
                self.image = pygame.image.load(RIGHTblue_dir).convert_alpha()
                self.set_velocity((0.4,0)) # VALOR TESTE
            self.direction = direction

    def update_position(self, time):
        self.last_position = self.position
        self.position += self.velocity * time
        if self.position != self.last_position:
            self.trace.append(self.position)


# Rotina Inicial do jogo
pygame.init()  # inicializa as rotinas do PyGame
surface = pygame.display.set_mode(screen_size) # cria a tela do jogo com tamanho personalizado
pygame.display.set_caption(page_title) # título da janela do jogo


# Rotinas de aúdio
pygame.mixer.music.load(derezzedSONG_dir)
pygame.mixer.music.set_volume(0.04)  # VALOR TESTE
pygame.mixer.music.play(-1)  # VALOR TESTE

# variável que declara o clock do jogo
clock = pygame.time.Clock()

# Início do main Loop
game = True
while game:
    time = clock.tick(60) # segura a taxa de quadros em 60 por segundo

    # Adquire todos os eventos e os testa para casos desejados
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT: # quebra o loop
            game = False
    
    # Rotinas da tela "estática"
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
    
    sprites.update(time)

    pygame.display.update() # atualiza o display

pygame.quit() # encerra o pygame