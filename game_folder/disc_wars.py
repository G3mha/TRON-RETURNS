import pygame
import sys
import random

BLUE_ICE = (0,255,251)
YELLOW_GOLD = (255,215,0)
BLACK = (0,0,0)
WHITE = (255,255,255)

class Disk(pygame.sprite.Sprite):
    def __init__(self, group, colour, creator, angle_index):
        super().__init__(group)
        self.v = 2
        if colour == "yellow":
            self.image = pygame.image.load('SPRITES_BOSS/disk_orange.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (31,28))
            self.angle_list = [(-self.v,-self.v), (-self.v,-self.v/2), (-self.v,0), (-self.v,self.v/2), (-self.v,self.v)]
            self.velocity = self.angle_list[angle_index]
        if colour == "blue":
            self.image = pygame.image.load('SPRITES_BOSS/disk_blue.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (31,28))
            self.angle_list = [(self.v,-self.v), (self.v,-self.v/2), (self.v,0), (self.v,self.v/2), (self.v,self.v)]
            self.velocity = self.angle_list[angle_index]
        self.colour = colour
        self.rect = pygame.Rect(creator.rect.x, creator.rect.y, 50, 50)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, time):
        self.rect.center = ((self.rect.center[0] + (self.velocity[0] * time)), (self.rect.center[1] + (self.velocity[1] * time)))
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
        self.v = 2
        if colour == "yellow":
            self.angle_list = [(-self.v,-self.v), (-self.v,-self.v/2), (-self.v,0), (-self.v,self.v/2), (-self.v,self.v)]
            self.image = pygame.image.load('SPRITES_BOSS/boss_sem_disco.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (50,88))
            self.mask = pygame.mask.from_surface(self.image)
            self.yellow = True
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(500,700),random.randint(100,700))
        if colour == "blue":
            self.angle_list = [(self.v,-self.v), (self.v,-self.v/2), (self.v,0), (self.v,self.v/2), (self.v,self.v)]
            self.image = pygame.image.load('SPRITES_BOSS/normal_sem_disco.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (50,88))
            self.mask = pygame.mask.from_surface(self.image)
            self.yellow = False
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(100,300),random.randint(100,700))
        self.velocity = [0,0]

    def game_controls(self, event):
        if self.yellow == False:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.velocity[1] = 1 # TODO: change value
                elif event.key == pygame.K_w:
                    self.velocity[1] = 1 # TODO: change value
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s or event.key == pygame.K_w:
                    self.velocity[1] = 0
        if self.yellow == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.velocity[1] = 1 # TODO: change value
                elif event.key == pygame.K_UP:
                    self.velocity[1] = 1 # TODO: change value
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    self.velocity[1] = 0
    
    def update(self):
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

# Variáveis para regular processos
b_disk_on = False
y_disk_on = False
c_pressed_blue = False
c_pressed_yellow = False
y_score = 0
b_score = 0
angle_index = 0
v=2


# variáveis de fonte
font_standart = pygame.font.Font(pygame.font.get_default_font(), 40)

while True:
    time = clock.tick(60) # segura a taxa de quadros em 60 por segundo
    surface.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type in (pygame.KEYDOWN, pygame.KEYUP):
            blue.game_controls(event)
            yellow.game_controls(event)
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        c_pressed_blue = True
                    if event.key == pygame.K_RIGHT:
                        c_pressed_yellow = True
                    if event.key == pygame.K_d and c_pressed_blue == True:
                        b_disk = Disk(sprites, 'blue', blue, angle_index)
                        b_disk_on = True
                        c_pressed_blue = False
                    if event.key == pygame.K_LEFT and c_pressed_yellow == True:
                        y_disk = Disk(sprites, 'yellow', yellow, angle_index)
                        y_disk_on = True
                        c_pressed_yellow = False
    if c_pressed_blue == True:
        angle_list = [(v,-v), (v,v/2), (v,0), (v,v/2), (v,v)]
        v_15 = [int(angle_list[angle_index][0]*15), int(angle_list[angle_index][1]*15)]
        end_pos = ((list(blue.rect.center)[0] + v_15[0]),(list(blue.rect.center)[1] + v_15[1]))
        pygame.draw.line(surface, WHITE, blue.rect.center, end_pos, 5)
    if c_pressed_yellow == True:
        angle_list = [[-v,-v], [-v,-v/2], [-v,0], [-v,v/2], [-v,v]]
        v_15_ = [int(yellow.angle_list[angle_index][0]*15), int(yellow.angle_list[angle_index][1]*15)]
        end_pos1 = ((list(yellow.rect.center)[0] + v_15_[0]),(list(yellow.rect.center)[1] + v_15_[1]))
        pygame.draw.line(surface, WHITE, yellow.rect.center, end_pos1, 5)
    angle_index += 1
    if angle_index > 4:
        angle_index = 0
    


    blue.update()
    yellow.update()

    if y_disk_on == True:
        y_disk.update(time)
        if pygame.sprite.collide_mask(yellow,y_disk) != None:
            y_disk.kill()
            y_disk_on = False
        if pygame.sprite.collide_mask(blue,y_disk) != None:
            y_score += 1
            blue.kill()
            blue = Paddle(sprites, "blue")
    if b_disk_on == True:
        b_disk.update(time)
        if pygame.sprite.collide_mask(blue,b_disk) != None:
            b_disk.kill()
            b_disk_on = False
        if pygame.sprite.collide_mask(yellow,b_disk) != None:
            b_score += 1
            yellow.kill()
            yellow = Paddle(sprites, "yellow")
    
        
    sprites.draw(surface)

    pygame.display.update()