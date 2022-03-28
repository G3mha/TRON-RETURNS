import sys
import pygame
import random
import numpy as np
from classes_game2 import *
from classes_game3 import *
from functions import *


# Define o código RGB das cores utilizadas
BLACK = (0,0,0)
BLUE = (12,12,100)
BLUE_ICE = (0,255,251)
WHITE = (255,255,255)
YELLOW_GOLD = (255,215,0)

pygame.init()


class Disk_BF(pygame.sprite.Sprite):
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
    self.v : float
        a variável fria para ser utilizada no self.angle_list, facilitando a manutenção do código
    self.rect : pygame.Rect
        a posição e tamanho da imagem do objeto
    height, width: int
        respectivamente, a largura e altura da tela 
    group : pygame.Group
        o grupo que armazena o objeto e compartilha de métodos iguais

    Métodos
    -------
    set_velocity(self, vx, vy)
        Define a velocidade do objeto
    set_position(self, x, y)
        Define a posição do objeto
    update(self, time)
        Define a nova posição, utilizando a velocidade e o tempo que passou desde a última chamada
    """
    def __init__(self, group, colour, rect):
        """
        Parameters
        ----------
        image:
        velocity:
        mask: pygame.
        """
        super().__init__(group)
        self.colour = colour
        if self.colour == "yellow":
            self.image = pygame.image.load('SPRITES_BOSS/disk_orange.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (31,28))
            self.set_velocity(-0.3,0) # TODO: mudar para um valor fixo
        if self.colour == "blue":
            self.image = pygame.image.load('SPRITES_BOSS/disk_blue.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (31,28))
            self.set_velocity(0.3,0) # TODO: mudar para um valor fixo
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = pygame.Rect(rect[0], rect[1], 31, 28)
    
    def set_position(self, x, y):
        """
        Parameters
        ----------
        midbottom:
        """
        self.rect.midbottom = pygame.math.Vector2(x, y)
    
    def set_velocity(self, vx, vy):
        """Define a velocidade
        vx: velocidade no eixo x
        vy: velocidade no eixo y"""
        self.velocity = pygame.math.Vector2(vx, vy)

    def update(self, time):
        """
        Parameters
        ----------
        rect.center:
        """
        self.rect.center += self.velocity * time

class CLU_BF(pygame.sprite.Sprite):
    """
    Uma class usada para representar o CLU
    """
    def __init__(self, group):

        """
        Parameters
        ----------
        rect.center:
        """

        super().__init__(group)
        self.image = pygame.image.load('SPRITES_BOSS/boss_sem_disco.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (40,90)) # TODO: mudar para um valor fixo
        self.rect = pygame.Rect(600, 535, 40, 90) # TODO: testar valores
        self.mask = pygame.mask.from_surface(self.image)

class TRON_BF(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.images = []
        for i in ['SPRITES_BOSS/normal_sem_disco.png', 'SPRITES_BOSS/agachado.png', 'SPRITES_BOSS/desfazendo_1.png', 'SPRITES_BOSS/desfazendo_2.png']:
            size = (40,90) # height and width
            if i == 'SPRITES_BOSS/agachado.png':
                size = (40,60)
            self.images.append(pygame.transform.scale(pygame.image.load(i).convert_alpha(), size))
        self.image = self.images[0]
        self.rect = pygame.Rect(150, 535, 40, 90) # TODO: testar valores
        self.og_x = self.rect.x
        self.og_y = self.rect.y
        self.mask = pygame.mask.from_surface(self.image)
        self.state = "STANDING"
        self.gravity = pygame.math.Vector2(0, 0.1) # TODO: testar valores
        self.set_velocity(0,0)

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y
    
    def set_velocity(self, vx, vy):
        """Define a velocidade
        vx: velocidade no eixo x
        vy: velocidade no eixo y"""
        self.velocity = pygame.math.Vector2(vx, vy)
    
    def stand(self):
        self.state = "STANDING"
        self.image = self.images[0]
        self.set_position(self.og_x, self.og_y) # TODO: testar valores
        self.set_velocity(0,0)
        self.mask = pygame.mask.from_surface(self.image)

    def duck(self):
        self.state = "DUCKING"
        self.set_position(self.og_x, self.og_y+30) # TODO: testar valores
        self.image = self.images[1]
        self.mask = pygame.mask.from_surface(self.image)
    
    def jump(self):
        self.jump_rect = self.rect
        if self.state == "STANDING":
            self.state = "JUMPING"
            self.set_velocity(0,-1) # TODO: testar valores
    
    def derezzed(self, sprite_name):
        self.image = self.images[2]
        pygame.time.delay(333)
        self.image = self.images[3]
        pygame.time.delay(333)
        sprite_name.kill()

    def update(self, time):
        if self.velocity == (0,1):
            self.stand()
        if self.state == "JUMPING":
            self.velocity += self.gravity
            self.rect.midbottom += self.velocity * time

################################ FUNCOES ESSENCIAIS ################################

def score(y_score, b_score, surface):
    font = pygame.font.Font(pygame.font.get_default_font(), 18)
    text = font.render("Placar TRON: {}".format(b_score), True, BLUE_ICE)
    surface.blit(text, (310,7))
    font1 = pygame.font.Font(pygame.font.get_default_font(), 18)
    text1 = font1.render("Placar CLU: {}".format(y_score), True, YELLOW_GOLD)
    surface.blit(text1, (310,30))

def help(game_access, surface):
    font = pygame.font.Font(pygame.font.get_default_font(), 18)
    text=[]
    text.append("Quais teclas usar ?")
    text.append("ESC = fechar o jogo")
    text.append("P = pausar/despausar o jogo")
    text.append("H = pedir ajuda (quando pausado)")
    text.append("BACKSPACE = reinicia o jogo (quando pausado)")
    if game_access == "fastest_disc":
        text.append("Tron")
        text.append("W = pula")
        text.append("S = abaixa")
        text.append("D = atira disco")
        text.append("CLU")
        text.append("I = Atira disco alto")
        text.append("M = Atira disco baixo")
        text.append("K = Atira disco central")
    if game_access == "disc_wars":
        text.append("Tron")
        text.append("W = sobe")
        text.append("S = desce")
        text.append("D = vai para a direita")
        text.append("A = vai para a esquerda")
        text.append("E = atira o disco")
        text.append("CLU")
        text.append("seta_cima = sobe")
        text.append("seta_baixo = desce")
        text.append("seta_direita = vai para a direita")
        text.append("seta_esquerda = vai para a esquerda")
        text.append("ENTER ou RETURN = Atira disco")
    if game_access == "lightcicle_run":
        text.append("Tron")
        text.append("seta_cima = sobe")
        text.append("seta_baixo = desce")
        text.append("seta_direita = vai para a direita")
        text.append("seta_esquerda = vai para a esquerda")
        text.append("ENTER ou RETURN = Atira disco")
        text.append("CLU")
        text.append("W = sobe")
        text.append("S = desce")
        text.append("D = vai para a direita")
        text.append("A = vai para a esquerda")
        text.append("E = atira o disco")
    surface.fill(BLACK)
    i=0
    for t in text:
        text1 = font.render(t, True, YELLOW_GOLD)
        surface.blit(text1, (30,(30+20*i)))
        i+=1