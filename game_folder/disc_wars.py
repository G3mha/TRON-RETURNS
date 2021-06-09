import pygame
import sys
import random

BLUE_ICE = (0,255,251)
YELLOW_GOLD = (255,215,0)
BLACK = (0,0,0)
WHITE = (255,255,255)

class Disk(pygame.sprite.Sprite):
    def __init__(self, group, colour, rect, angle_index):
        super().__init__(group)
        self.v = 0.2
        if colour == "yellow":
            self.image = pygame.image.load('SPRITES_BOSS/disk_orange.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (31,28))
            self.angle_list = [(-self.v,-self.v), (-self.v,-self.v/2), (-self.v,0), (-self.v,self.v/2), (-self.v,self.v)]
            self.rect = pygame.Rect(rect[0]-31, rect[1]-20, 31, 28)
        if colour == "blue":
            self.image = pygame.image.load('SPRITES_BOSS/disk_blue.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (31,28))
            self.angle_list = [(self.v,-self.v), (self.v,-self.v/2), (self.v,0), (self.v,self.v/2), (self.v,self.v)]
            self.rect = pygame.Rect(rect[0]+31, rect[1]+20, 31, 28)
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

    def update(self):
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

def score(y_score, b_score, surface):
    font = pygame.font.Font(pygame.font.get_default_font(), 18)
    text = font.render("Placar TRON: {}".format(b_score), True, BLUE_ICE)
    surface.blit(text, (310,7))
    font1 = pygame.font.Font(pygame.font.get_default_font(), 18)
    text1 = font1.render("Placar CLU: {}".format(y_score), True, YELLOW_GOLD)
    surface.blit(text1, (310,30))

pygame.init()  # inicializa as rotinas do PyGame
screen_size = (800,800) # Largura e altura da tela
page_title = "Batalha de Discos" # Define o nome desta página
surface = pygame.display.set_mode(screen_size) # cria a tela do jogo com tamanho personalizado
pygame.display.set_caption(page_title) # título da janela do jogo

# variável que declara o clock do jogo
clock = pygame.time.Clock()

# cria sprite dos Paddles
sprites = pygame.sprite.Group()
yellow = Player(sprites, "yellow")
blue = Player(sprites, "blue")

# Variáveis para regular processos
b_disk_alive = False
y_disk_alive = False
pressed_blue = False
pressed_yellow = False
y_score = 0
b_score = 0
angle_index = 0
sub_angle_index = 0
v=0.2
angle_list_1 = [(v,-v), (v,-v/2), (v,0), (v,v/2), (v,v)]
angle_list_2 = [(-v,-v), (-v,-v/2), (-v,0), (-v,v/2), (-v,v)]


while True:
    time = clock.tick(60) # segura a taxa de quadros em 60 por segundo
    surface.blit(pygame.image.load('SPRITES_BOSS/wallpaper_disc_wars.png').convert_alpha(), (0,0))
    pygame.draw.line(surface, BLUE_ICE, (400,60), (400,800), 5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type in (pygame.KEYDOWN, pygame.KEYUP):
            blue.game_controls(event)
            yellow.game_controls(event)
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e and not pressed_blue and b_disk_alive != True:
                        pressed_blue = True
                    elif event.key == pygame.K_e and pressed_blue == True and b_disk_alive != True:
                        rect_b = blue.rect.midright
                        b_disk = Disk(sprites, 'blue', rect_b, angle_index)
                        b_disk_alive = True
                        pressed_blue = False
                    if event.key == pygame.K_RETURN and not pressed_yellow and y_disk_alive != True:
                        pressed_yellow = True
                    
                    elif event.key == pygame.K_RETURN and pressed_yellow == True and y_disk_alive != True:
                        rect_y = yellow.rect.midleft
                        y_disk = Disk(sprites, 'yellow', rect_y, angle_index)
                        y_disk_alive = True
                        pressed_yellow = False

                        
    if pressed_blue == True and b_disk_alive != True:
        v_15 = [int(angle_list_1[angle_index][0]*200), int(angle_list_1[angle_index][1]*200)]
        end_pos = ((list(blue.rect.center)[0] + v_15[0]),(list(blue.rect.center)[1] + v_15[1]))
        pygame.draw.line(surface, WHITE, blue.rect.center, end_pos, 5)

    if pressed_yellow == True and y_disk_alive != True:
        v_15_ = [int(angle_list_2[angle_index][0]*200), int(angle_list_2[angle_index][1]*200)]
        end_pos1 = ((list(yellow.rect.center)[0] + v_15_[0]),(list(yellow.rect.center)[1] + v_15_[1]))
        pygame.draw.line(surface, WHITE, yellow.rect.center, end_pos1, 5)

    sub_angle_index += 1
    if sub_angle_index == 12:
        sub_angle_index = 0
        angle_index += 1
    if angle_index > 4:
        angle_index = 0

    blue.update()
    yellow.update()

    if y_disk_alive == True:
        y_disk.update(time)
        if pygame.sprite.collide_mask(yellow,y_disk) != None:
            y_disk.kill()
            y_disk_alive = False    
        if pygame.sprite.collide_mask(blue,y_disk) != None:
            y_score += 1
            blue.kill()
            blue = Player(sprites, "blue")
    if b_disk_alive == True:
        b_disk.update(time)
        if pygame.sprite.collide_mask(blue,b_disk) != None:
            b_disk.kill()
            b_disk_alive = False
        if pygame.sprite.collide_mask(yellow,b_disk) != None:
            b_score += 1
            yellow.kill()
            yellow = Player(sprites, "yellow")

    sprites.draw(surface)
    score(y_score, b_score, surface)
    pygame.display.update()