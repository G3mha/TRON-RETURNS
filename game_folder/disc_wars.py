import pygame
import sys
import math

BLUE_ICE = (0,255,251)
YELLOW_GOLD = (255,215,0)

class Disk(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = pygame.image.load('SPRITES_BOSS/neutral_disk.png').convert_alpha()
        self.rect = ('x','y',100,100) # TODO: change values for x & y
        self.velocity = (0,0) # TODO: change values

    def update(self, time):
        self.rect.center += self.velocity * time

class Paddle(pygame.sprite.Sprite):
    def __init__(self, group, colour):
        super().__init__(group)
        if colour == "yellow":
            self.image = pygame.image.load('SPRITES_BOSS/yellow_padle.png').convert_alpha()
            self.yellow = True
        if colour == "blue":
            self.image = pygame.image.load('SPRITES_BOSS/blue_padle.png').convert_alpha()
            self.yellow = False
        self.rect = ('x','y',100,100) # TODO: change values for x & y
        self.velocity = (0,0)

    def game_controls(self, event):
        if self.yellow == False:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.velocity = (0,0) # TODO: change values
                elif event.key == pygame.K_w:
                    self.velocity = (0,0) # TODO: change values
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s or event.key == pygame.K_w:
                    self.velocity = (0,0)
        if self.yellow == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.velocity = (0,0) # TODO: change values
                elif event.key == pygame.K_UP:
                    self.velocity = (0,0) # TODO: change values
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    self.velocity = (0,0)

pygame.init()  # inicializa as rotinas do PyGame
screen_size = (800,800) # Largura e altura da tela
page_title = "Batalha de Discos" # Define o nome desta página
surface = pygame.display.set_mode(screen_size) # cria a tela do jogo com tamanho personalizado
pygame.display.set_caption(page_title) # título da janela do jogo

# variável que declara o clock do jogo
clock = pygame.time.Clock()

# cria sprite dos Paddles
sprites = pygame.sprite.Group()
yellow = Paddle(sprites, "yellow")
blue = Paddle(sprites, "blue")
disk = Disk(sprites)