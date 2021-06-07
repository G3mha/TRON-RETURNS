import pygame
import sys
import math

BLUE_ICE = (0,255,251)
YELLOW_GOLD = (255,215,0)

class Disk(pygame.sprite.Sprite):
    def __init__(self, group, colour, creator):
        super().__init__(group)
        if colour == "yellow":
            self.image = pygame.image.load('SPRITES_BOSS/disk_orange.png').convert_alpha()
            self.velocity = [0,0] # TODO: change values
        if colour == "blue":
            self.image = pygame.image.load('SPRITES_BOSS/disk_blue.png').convert_alpha()
            self.velocity = [0,0] # TODO: change values
        self.colour = colour
        self.rect = pygame.Rect(creator.rect.x, creator.rect.y, 100, 100)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, time):
        self.rect.center += self.velocity * time
        width, height = pygame.display.get_surface().get_size()
        # regula o movimento do disco horizontalmente, para que ele não saia da tela
        if self.rect.right > width:
            self.velocity[0] = -abs(self.velocity[0])
            self.rect.right = width
        elif self.rect.x < 0:
            self.velocity[0] = abs(self.velocity[0])
            self.rect.x = 0
        # regula o movimento do disco verticalmente, para que ele não saia da tela
        if self.rect.bottom > height:
            self.velocity[1] = -abs(self.velocity[1])
            self.rect.bottom = height
        elif self.rect.y < 0:
            self.velocity[1] = abs(self.velocity[1])
            self.rect.y = 0

class Paddle(pygame.sprite.Sprite):
    def __init__(self, group, colour):
        super().__init__(group)
        if colour == "yellow":
            self.image = pygame.image.load('SPRITES_BOSS/yellow_padle.png').convert_alpha()
            self.mask = pygame.mask.from_surface(self.image)
            self.yellow = True
        if colour == "blue":
            self.image = pygame.image.load('SPRITES_BOSS/blue_padle.png').convert_alpha()
            self.mask = pygame.mask.from_surface(self.image)
            self.yellow = False
        self.rect = pygame.Rect('x', 'y', 100, 100) # TODO: change values for x & y
        self.velocity = [0,0]

    def game_controls(self, event):
        if self.yellow == False:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.velocity[1] = 0 # TODO: change value
                elif event.key == pygame.K_w:
                    self.velocity[1] = 0 # TODO: change value
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s or event.key == pygame.K_w:
                    self.velocity[1] = 0
        if self.yellow == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.velocity[1] = 0 # TODO: change value
                elif event.key == pygame.K_UP:
                    self.velocity[1] = 0 # TODO: change value
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    self.velocity[1] = 0

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
b_disk = Disk(sprites, 'blue')
y_disk = Disk(sprites, 'yellow')
y_on = True
b_on = True
b_disk_on = True
y_disk_on = True
y_score = 0
b_score = 0

# Variáveis para regular processos
score = 0

# variáveis de fonte
font_standart = pygame.font.Font(pygame.font.get_default_font(), 40)

while True:
    time = clock.tick(60) # segura a taxa de quadros em 60 por segundo
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type in (pygame.KEYDOWN, pygame.KEYUP):
            blue.game_controls(event)
            yellow.game_controls(event)

    if b_disk.mask.collide_mask(blue.mask):
        b_disk.kill()
        b_disk_on = False
    if y_disk.mask.collide_mask(yellow.mask):
        y_disk.kill()
        y_disk_on = False
    
    if b_disk.mask.collide_mask(yellow.mask):
        yellow.kill()
        b_score += 1
        y_on = False
    if y_disk.mask.collide_mask(blue.mask):
        blue.kill()
        y_score += 1
        b_on = False