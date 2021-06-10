import sys
import pygame
import random

# Define o código RGB das cores utilizadas
BLACK = (0,0,0)
BLUE = (12,12,100)
BLUE_ICE = (0,255,251)
WHITE = (255,255,255)
YELLOW_GOLD = (255,215,0)

pygame.init()


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
    self.v : float
        a variável fria para ser utilizada no self.angle_list, facilitando a manutenção do código
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

#####################################################

class yellowLightCicle(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.size_vert = (32,80)
        self.size_horiz = (80,32)
        self.image = pygame.image.load('SPRITES/SPRITE_TRON_LIGHTCICLE_yellowLEFT.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size_horiz)
        self.rect = self.image.get_rect()
        self.set_position(400,200)
        self.set_velocity(-0.2,0)
        self.direction = "LEFT"
        self.trace = []
        self.explode = False


    def set_position(self, x, y):
        self.rect.center = pygame.math.Vector2(x, y)
    
    def set_velocity(self, vx, vy):
        """
        Define a velocidade
        vx: velocidade no eixo x
        vy: velocidade no eixo y
        """
        self.velocity = pygame.math.Vector2(vx, vy)
    
    def update_direction(self, direction):
        if direction != self.direction:
            position = self.rect.center
            if direction == "UP":
                self.image = pygame.image.load('SPRITES/SPRITE_TRON_LIGHTCICLE_yellowDOWN.png').convert_alpha()
                self.image = pygame.transform.scale(self.image, self.size_vert)
                self.set_velocity(0,0.2)
            if direction == "DOWN":
                self.image = pygame.image.load('SPRITES/SPRITE_TRON_LIGHTCICLE_yellowUP.png').convert_alpha()
                self.image = pygame.transform.scale(self.image, self.size_vert)
                self.set_velocity(0,-0.2)
            if direction == "LEFT":
                self.image = pygame.image.load('SPRITES/SPRITE_TRON_LIGHTCICLE_yellowLEFT.png').convert_alpha()
                self.image = pygame.transform.scale(self.image, self.size_horiz)
                self.set_velocity(-0.2,0)
            if direction == "RIGHT":
                self.image = pygame.image.load('SPRITES/SPRITE_TRON_LIGHTCICLE_yellowRIGHT.png').convert_alpha()
                self.image = pygame.transform.scale(self.image, self.size_horiz)
                self.set_velocity(0.2,0)
            self.rect = self.image.get_rect()
            self.rect.center = position
            self.direction = direction

    def update(self, time):
        self.rect.center += self.velocity * time
        self.trace.append(self.rect.center)
        width, height = pygame.display.get_surface().get_size()
        # regula o movimento do disco horizontalmente, para que ele não saia da tela
        if self.rect.right > width:
            self.explode = True
        elif self.rect.x < 0:
            self.explode = True
        # regula o movimento do disco verticalmente, para que ele não saia da tela
        if self.rect.bottom > height:
            self.explode = True
        elif self.rect.y < 0:
            self.explode = True

    def slow_down(self):
        if self.direction == "UP":
            if self.velocity == (0,0.2):
                self.set_velocity(0,0.1)
            elif self.velocity == (0,0.1):
                self.set_velocity(0,0.2)
        if self.direction == "DOWN":
            if self.velocity == (0,-0.2):
                self.set_velocity(0,-0.1)
            elif self.velocity == (0,-0.1):
                self.set_velocity(0,-0.2)
        if self.direction == "LEFT":
            if self.velocity == (-0.2,0):
                self.set_velocity(-0.1,0)
            elif self.velocity == (-0.1,0):
                self.set_velocity(-0.2,0)
        if self.direction == "RIGHT":
            if self.velocity == (0.2,0):
                self.set_velocity(0.1,0)
            elif self.velocity == (0.1,0):
                self.set_velocity(0.2,0)

class blueLightCicle(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.size_vert = (32,80)
        self.size_horiz = (80,32)
        self.image = pygame.image.load('SPRITES/SPRITE_TRON_LIGHTCICLE_blueRIGHT.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size_horiz)
        self.rect = self.image.get_rect()
        self.set_position(100,400)
        self.set_velocity(0.2,0) # VALOR TESTE
        self.direction = "RIGHT"
        self.trace = []
        self.explode = False

    def set_position(self, x, y):
        self.rect.center = pygame.math.Vector2(x, y)
    
    def set_velocity(self, vx, vy):
        self.velocity = pygame.math.Vector2(vx, vy)
    
    def update_direction(self, direction):
        if direction != self.direction:
            position = self.rect.center
            if direction == "UP":
                self.image = pygame.image.load('SPRITES/SPRITE_TRON_LIGHTCICLE_blueDOWN.png').convert_alpha()
                self.image = pygame.transform.scale(self.image, self.size_vert)
                self.set_velocity(0,0.2)
            if direction == "DOWN":
                self.image = pygame.image.load('SPRITES/SPRITE_TRON_LIGHTCICLE_blueUP.png').convert_alpha()
                self.image = pygame.transform.scale(self.image, self.size_vert)
                self.set_velocity(0,-0.2)
            if direction == "LEFT":
                self.image = pygame.image.load('SPRITES/SPRITE_TRON_LIGHTCICLE_blueLEFT.png').convert_alpha()
                self.image = pygame.transform.scale(self.image, self.size_horiz)
                self.set_velocity(-0.2,0)
            if direction == "RIGHT":
                self.image = pygame.image.load('SPRITES/SPRITE_TRON_LIGHTCICLE_blueRIGHT.png').convert_alpha()
                self.image = pygame.transform.scale(self.image, self.size_horiz)
                self.set_velocity(0.2,0)
            self.rect = self.image.get_rect()
            self.rect.center = position
            self.direction = direction

    def update(self, time):
        self.rect.center += self.velocity * time
        self.trace.append(self.rect.center)
        width, height = pygame.display.get_surface().get_size()
        # regula o movimento do disco horizontalmente, para que ele não saia da tela
        if self.rect.right > width:
            self.explode = True
        elif self.rect.x < 0:
            self.explode = True
        # regula o movimento do disco verticalmente, para que ele não saia da tela
        if self.rect.bottom > height:
            self.explode = True
        elif self.rect.y < 0:
            self.explode = True
    
    def slow_down(self):
        if self.direction == "UP":
            if self.velocity == (0,0.2):
                self.set_velocity(0,0.1)
            elif self.velocity == (0,0.1):
                self.set_velocity(0,0.2)
        if self.direction == "DOWN":
            if self.velocity == (0,-0.2):
                self.set_velocity(0,-0.1)
            elif self.velocity == (0,-0.1):
                self.set_velocity(0,-0.2)
        if self.direction == "LEFT":
            if self.velocity == (-0.2,0):
                self.set_velocity(-0.1,0)
            elif self.velocity == (-0.1,0):
                self.set_velocity(-0.2,0)
        if self.direction == "RIGHT":
            if self.velocity == (0.2,0):
                self.set_velocity(0.1,0)
            elif self.velocity == (0.1,0):
                self.set_velocity(0.2,0)

def tutorial_screen(surface):
    line_text = [
        "Olá programa! Aqui você testará suas habilidades com motos.",
        "Você iniciará no canto inferior esquerdo da tela.",
        "Para vencer, a moto amarela deve se chocar contra o seu rastro de luz.",
        "Esse rastro é deixado por todos os pontos em que sua moto passa.",
        "Para controlar a moto, aperte as teclas CIMA, BAIXO, DIREITA, ESQUERDA.",
        "E para diminuir a velocidade pressione a BARRA DE ESPAÇO.",
        "Da mesma forma, a moto amarela também tentará o mesmo.",
        "Que os jogos começem!"
    ]
    command = "...(pressione ENTER para continuar)"
    font_instructions = pygame.font.Font(pygame.font.get_default_font(), 20)
    
    for line in line_text:
        command_pressed = True
        while command_pressed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): # quebra o loop
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    command_pressed = False
                    break
            surface.fill(BLACK)
            pygame.draw.rect(surface, BLUE_ICE, (0,0,800,800), 20)
            line_image = font_instructions.render(line, True, BLUE_ICE)
            command_image = font_instructions.render(command, True, BLUE_ICE)
            surface.blit(line_image,(20,100))
            surface.blit(command_image,(20,700))
            pygame.display.flip()

##############################################################################

class Disk_BF(pygame.sprite.Sprite):
     """
    Uma class usada para representar od dois discos
    """
    def __init__(self, group, colour, rect):
        """
        Parameters
        ----------
        image:

        velocity:

        mask:
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
        self.i = pygame.image.load('SPRITES_BOSS/normal_sem_disco.png').convert_alpha()
        self.i = pygame.transform.scale(self.i, (40,90)) # TODO: mudar para um valor fixo
        self.images.append(self.i)
        self.i = pygame.image.load('SPRITES_BOSS/agachado.png').convert_alpha()
        self.i = pygame.transform.scale(self.i, (40,60)) # TODO: mudar para um valor fixo
        self.images.append(self.i)
        self.i = pygame.image.load('SPRITES_BOSS/desfazendo_1.png').convert_alpha()
        self.i = pygame.transform.scale(self.i, (40,90)) # TODO: mudar para um valor fixo
        self.images.append(self.i)
        self.i = pygame.image.load('SPRITES_BOSS/desfazendo_2.png').convert_alpha()
        self.i = pygame.transform.scale(self.i, (40,90)) # TODO: mudar para um valor fixo
        self.images.append(self.i)
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