"""
Programa do mini-game de Motos
Autor: Enricco Gemha
Data: 18/05/2021
"""

import random
import sys
import pygame

# Estabelece a pasta que contem as sprites.
LEFTblue_dir = 'SPRITES/SPRITE_TRON_LIGHTCICLE_blueLEFT.png'
RIGHTblue_dir = 'SPRITES/SPRITE_TRON_LIGHTCICLE_blueRIGHT.png'
UPblue_dir = 'SPRITES/SPRITE_TRON_LIGHTCICLE_blueUP.png'
DOWNblue_dir = 'SPRITES/SPRITE_TRON_LIGHTCICLE_blueDOWN.png'
LEFTyellow_dir = 'SPRITES/SPRITE_TRON_LIGHTCICLE_yellowLEFT.png'
RIGHTyellow_dir = 'SPRITES/SPRITE_TRON_LIGHTCICLE_yellowRIGHT.png'
UPyellow_dir = 'SPRITES/SPRITE_TRON_LIGHTCICLE_yellowUP.png'
DOWNyellow_dir = 'SPRITES/SPRITE_TRON_LIGHTCICLE_yellowDOWN.png'
derezzedSONG_dir = 'AUDIO/DerezzedSong.ogg'
derezzedSFX_dir = 'AUDIO/DerezzedFX.ogg'
derezzedVFX_dir = 'SPRITES/VFX DEREZZED EXPLOSION.png'

# Algumas variáveis essenciais para a aplicação
screen_size = (800,800) # Largura e altura da tela
lightcicle_size = (200,100) # Tamanho da bike
page_title = "Corrida de motos" # Define o nome desta página
stop_blue = True
stop_yellow = True
game = "RUNNING"

# Define o código RGB das cores utilizadas
BLACK = (0,0,0)
BLUE_MIDNIGHT = (0,0,30)
BLUE = (12,12,100)
BLUE_ICE = (0,255,251)
YELLOW_GOLD = (255,215,0)
WHITE = (255,255,255)


class yellowLightCicle(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = pygame.image.load(LEFTyellow_dir).convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width()/5),int(self.image.get_height()/5)))
        self.rect = self.image.get_rect()
        self.set_position(screen_size[0],0)
        self.set_velocity(-0.2,0) # VALOR TESTE
        self.direction = "LEFT"
        self.trace = []

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
            if direction == "UP":
                self.image = pygame.image.load(DOWNyellow_dir).convert_alpha()
                self.image = pygame.transform.scale(self.image, (int(self.image.get_width()/5),int(self.image.get_height()/5)))
                self.set_velocity(0,0.2) # VALOR TESTE
            if direction == "DOWN":
                self.image = pygame.image.load(UPyellow_dir).convert_alpha()
                self.image = pygame.transform.scale(self.image, (int(self.image.get_width()/5),int(self.image.get_height()/5)))
                self.set_velocity(0,-0.2) # VALOR TESTE
            if direction == "LEFT":
                self.image = pygame.image.load(LEFTyellow_dir).convert_alpha()
                self.image = pygame.transform.scale(self.image, (int(self.image.get_width()/5),int(self.image.get_height()/5)))
                self.set_velocity(-0.2,0) # VALOR TESTE
            if direction == "RIGHT":
                self.image = pygame.image.load(RIGHTyellow_dir).convert_alpha()
                self.image = pygame.transform.scale(self.image, (int(self.image.get_width()/5),int(self.image.get_height()/5)))
                self.set_velocity(0.2,0) # VALOR TESTE
            self.direction = direction

    def update_position(self, time):
        self.rect.center += self.velocity * time
        self.trace.append(self.rect.center)


class blueLightCicle(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = pygame.image.load(RIGHTblue_dir).convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width()/5),int(self.image.get_height()/5)))
        self.rect = self.image.get_rect()
        self.set_position(0,screen_size[0])
        self.set_velocity(0.2,0) # VALOR TESTE
        self.direction = "RIGHT"
        self.trace = []

    def set_position(self, x, y):
        self.rect.center = pygame.math.Vector2(x, y)
    
    def set_velocity(self, vx, vy):
        self.velocity = pygame.math.Vector2(vx, vy)
    
    def update_direction(self, direction):
        if direction != self.direction:
            if direction == "UP":
                self.image = pygame.image.load(DOWNblue_dir).convert_alpha()
                self.image = pygame.transform.scale(self.image, (int(self.image.get_width()/5),int(self.image.get_height()/5)))
                self.set_velocity(0,0.2) # VALOR TESTE
            if direction == "DOWN":
                self.image = pygame.image.load(UPblue_dir).convert_alpha()
                self.image = pygame.transform.scale(self.image, (int(self.image.get_width()/5),int(self.image.get_height()/5)))
                self.set_velocity(0,-0.2) # VALOR TESTE
            if direction == "LEFT":
                self.image = pygame.image.load(LEFTblue_dir).convert_alpha()
                self.image = pygame.transform.scale(self.image, (int(self.image.get_width()/5),int(self.image.get_height()/5)))
                self.set_velocity(-0.2,0) # VALOR TESTE
            if direction == "RIGHT":
                self.image = pygame.image.load(RIGHTblue_dir).convert_alpha()
                self.image = pygame.transform.scale(self.image, (int(self.image.get_width()/5),int(self.image.get_height()/5)))
                self.set_velocity(0.2,0) # VALOR TESTE
            self.direction = direction

    def update_position(self, time):
        self.rect.center += self.velocity * time
        self.trace.append(self.rect.center)


def tutorial_screen():
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
    command = "...(pressione a BARRA DE ESPAÇO para continuar)"
    font_instructions = pygame.font.Font(pygame.font.get_default_font(), 20)
    
    for line in line_text:
        command_pressed = True
        while command_pressed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): # quebra o loop
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    command_pressed = False
                    break
            surface.fill(BLACK)
            pygame.draw.rect(surface, BLUE_ICE, (0,0,800,800), 20)
            line_image = font_instructions.render(line, True, BLUE_ICE)
            command_image = font_instructions.render(command, True, BLUE_ICE)
            surface.blit(line_image,(20,100))
            surface.blit(command_image,(20,700))
            pygame.display.flip()


def crash(collor1,collor2):
    for t in collor1.trace:
        if collor2.rect.collidepoint(t):
            # derezzed_blit=blue.rect
            # surface.blit(pygame.image.load(derezzedVFX_dir).convert_alpha(), derezzed_blit)
            collor2.kill()
            return False # retorna um valor booleano "False" para parar o "trace"
    return True # Caso contrário, continua igual
        


# Rotina Inicial do jogo
pygame.init()  # inicializa as rotinas do PyGame
surface = pygame.display.set_mode(screen_size) # cria a tela do jogo com tamanho personalizado
pygame.display.set_caption(page_title) # título da janela do jogo

# Breve tutorial de instruções deste modo de jogo
tutorial_screen()

# Rotinas de aúdio
pygame.mixer.music.load(derezzedSONG_dir)
pygame.mixer.music.set_volume(0.04)  # VALOR TESTE
pygame.mixer.music.play(-1)  # VALOR TESTE

# variável que declara o clock do jogo
clock = pygame.time.Clock()

# cria sprite das Motos
sprites = pygame.sprite.Group()
yellow = yellowLightCicle(sprites)
blue = blueLightCicle(sprites)

# variáveis de fonte
font_paused = pygame.font.Font(pygame.font.get_default_font(), 40)


# Início do Loop da corrida de moto
while True:
    time = clock.tick(60) # segura a taxa de quadros em 60 por segundo
    # Adquire todos os eventos e os testa para casos desejados
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): # quebra o loop
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                blue.update_direction("LEFT")
            elif event.key == pygame.K_RIGHT:
                blue.update_direction("RIGHT")
            elif event.key == pygame.K_DOWN:
                blue.update_direction("UP")
            elif event.key == pygame.K_UP:
                blue.update_direction("DOWN")
            elif event.key == pygame.K_SPACE:
                blue.velocity = (blue.velocity)/2
            elif event.key == pygame.K_p:
                if game != "PAUSED":
                    pygame.mixer.music.pause()
                    pause = font_paused.render("PAUSE", True, BLACK, WHITE)
                    surface.blit(pause,((surface.get_width()-pause.get_width())/2,
                                        (surface.get_height()-pause.get_height())/2))
                    game = "PAUSED"
                else:
                    pygame.mixer.music.unpause()
                    game = "RUNNING"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                blue.velocity = (blue.velocity)*2

    if game == "PAUSED":
        pygame.display.flip()
        continue

    # Rotinas do Background
    surface.fill(BLUE)
    thickness = 10
    # Desenha borda da tela
    pygame.draw.line(surface, BLUE_MIDNIGHT, (0,0), (screen_size[0],0), thickness)
    pygame.draw.line(surface, BLUE_MIDNIGHT, (0,0), (0,screen_size[1]), thickness)
    pygame.draw.line(surface, BLUE_MIDNIGHT, screen_size, (screen_size[0],0), thickness)
    pygame.draw.line(surface, BLUE_MIDNIGHT, screen_size, (0,screen_size[1]), thickness)
    distance = 1024/8 # espaço entre cada quadrado
    i = 0
    while i < 9:
        pygame.draw.line(surface, BLUE_MIDNIGHT, (0,(i*distance)), (screen_size[0],(i*distance)), thickness) # Desenha linha horizontal
        pygame.draw.line(surface, BLUE_MIDNIGHT, ((i*distance),0), ((i*distance),screen_size[0]), thickness) # Desenha linha vertical
        i+=1

    i = 0
    if len(blue.trace) >= 2:
        while i < len(blue.trace):
            pygame.draw.circle(surface, BLUE_ICE, blue.trace[i], 6)
            i+=1
    
    i = 0
    if len(yellow.trace) >= 2:
        while i < len(yellow.trace):
            pygame.draw.circle(surface, YELLOW_GOLD, yellow.trace[i], 6)
            i+=1

    sprites.draw(surface) # desenha as sprites
    
    # Atualiza a posição da moto e rastro
    if stop_yellow:
        yellow.update_position(time)
    if stop_blue:
        blue.update_position(time)

    # Verifica se houve colisão entre a moto e o rastro
    stop_yellow = crash(blue,yellow)
    stop_blue = crash(yellow,blue)

    pygame.display.flip() # atualiza o display
