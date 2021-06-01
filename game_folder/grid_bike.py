"""
Programa do mini-game de Motos
Autor: Enricco Gemha
Data: 18/05/2021
"""

import random
import sys
import pygame

# Quantidade de vidas até o game-over
lifes = 4

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
page_title = "Corrida de motos" # Define o nome desta página

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
        self.set_position(400,200)
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
        self.set_position(100,400)
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
                self.set_velocity(0,0.2)
            if direction == "DOWN":
                self.image = pygame.image.load(UPblue_dir).convert_alpha()
                self.image = pygame.transform.scale(self.image, (int(self.image.get_width()/5),int(self.image.get_height()/5)))
                self.set_velocity(0,-0.2)
            if direction == "LEFT":
                self.image = pygame.image.load(LEFTblue_dir).convert_alpha()
                self.image = pygame.transform.scale(self.image, (int(self.image.get_width()/5),int(self.image.get_height()/5)))
                self.set_velocity(-0.2,0)
            if direction == "RIGHT":
                self.image = pygame.image.load(RIGHTblue_dir).convert_alpha()
                self.image = pygame.transform.scale(self.image, (int(self.image.get_width()/5),int(self.image.get_height()/5)))
                self.set_velocity(0.2,0)
            self.direction = direction
    
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

def crash(collor1,collor2):
    if collor1.rect.topright[0] == 800 or collor1.rect.topright[1] == 0 or collor1.rect.bottomleft[1] == 800 or collor1.rect.bottomleft[0] == 0:
        derezzed_visual = pygame.image.load(derezzedVFX_dir).convert_alpha()
        derezzed_visual = pygame.transform.scale(derezzed_visual, (int(derezzed_visual.get_width()/5),int(derezzed_visual.get_height()/5)))
        surface.blit(derezzed_visual, collor1.rect.center)
        collor1.kill()
        return False # retorna um valor booleano "False" para parar o "trace"
    if collor2.rect.topright[0] == 800 or collor2.rect.topright[1] == 0 or collor2.rect.bottomleft[1] == 800 or collor2.rect.bottomleft[0] == 0:
        derezzed_visual = pygame.image.load(derezzedVFX_dir).convert_alpha()
        derezzed_visual = pygame.transform.scale(derezzed_visual, (int(derezzed_visual.get_width()/5),int(derezzed_visual.get_height()/5)))
        surface.blit(derezzed_visual, collor2.rect.center)
        collor2.kill()
        return False # retorna um valor booleano "False" para parar o "trace"
    for t in collor1.trace:
        if collor2.rect.collidepoint(t):
            derezzed_visual = pygame.image.load(derezzedVFX_dir).convert_alpha()
            derezzed_visual = pygame.transform.scale(derezzed_visual, (int(derezzed_visual.get_width()/5),int(derezzed_visual.get_height()/5)))
            surface.blit(derezzed_visual, collor2.rect.center)
            collor2.kill()
            return False # retorna um valor booleano "False" para parar o "trace"
    return True # Caso contrário, continua igual
        
def draw_background():
    surface.fill(BLUE)
    thickness = 10
    distance = screen_size[0]/8 # espaço entre cada quadrado
    i = 0
    while i < 9:
        pygame.draw.line(surface, BLUE_MIDNIGHT, (0,(i*distance)), (screen_size[0],(i*distance)), thickness) # Desenha linha horizontal
        pygame.draw.line(surface, BLUE_MIDNIGHT, ((i*distance),0), ((i*distance),screen_size[0]), thickness) # Desenha linha vertical
        i+=1

def draw_trace():
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

def show_score(stop_blue,stop_yellow):
    if stop_blue == False:
        score = ["Você PERDEU!","Para tentar novamente, clique N"]
        font_used = pygame.font.Font(pygame.font.get_default_font(), 40)
        line_image = font_used.render(score[0], True, BLUE_ICE, BLACK)
        surface.blit(line_image,(50,200))
        line_image2 = font_used.render(score[1], True, BLUE_ICE, BLACK)
        surface.blit(line_image2,(50,300))
        


    if stop_yellow == False:
        score = "Você GANHOU!"
        font_used = pygame.font.Font(pygame.font.get_default_font(), 40)
        line_image = font_used.render(score, True, BLUE_ICE, BLACK)
        surface.blit(line_image,(400,400))

while lifes > 0:
    # Rotina Inicial do jogo
    pygame.init()  # inicializa as rotinas do PyGame
    surface = pygame.display.set_mode(screen_size) # cria a tela do jogo com tamanho personalizado
    pygame.display.set_caption(page_title) # título da janela do jogo

    # Rotinas de aúdio
    pygame.mixer.music.load(derezzedSONG_dir)
    pygame.mixer.music.set_volume(0.04)
    pygame.mixer.music.play(-1)

    # Breve tutorial de instruções deste modo de jogo
    tutorial_screen()

    # variável que declara o clock do jogo
    clock = pygame.time.Clock()

    # cria sprite das Motos
    sprites = pygame.sprite.Group()
    yellow = yellowLightCicle(sprites)
    blue = blueLightCicle(sprites)

    # Variáveis para regular processos
    stop_blue = True
    stop_yellow = True
    stop_sound = True
    restart = False
    game = "RUNNING"

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
                if event.key == pygame.K_n:
                    lifes -= 1
                    restart = True
                if event.key == pygame.K_LEFT:
                    blue.update_direction("LEFT")
                elif event.key == pygame.K_RIGHT:
                    blue.update_direction("RIGHT")
                elif event.key == pygame.K_DOWN:
                    blue.update_direction("UP")
                elif event.key == pygame.K_UP:
                    blue.update_direction("DOWN")
                elif event.key == pygame.K_SPACE:
                    blue.slow_down()
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

        if game == "PAUSED":
            pygame.display.flip()
            continue
        
        if restart == True:
            restart = False
            break

        draw_background()

        draw_trace()
        sprites.draw(surface) # desenha as sprites

        # Atualiza a posição da moto e rastro
        if stop_yellow == True and stop_blue == True:
            yellow.update_position(time)
            blue.update_position(time)

        # Verifica se houve colisão entre a moto e o rastro
        stop_yellow = crash(blue,yellow)
        stop_blue = crash(yellow,blue)

        if (stop_blue == False or stop_yellow == False) and stop_sound == True:
            derezzed_sound = pygame.mixer.Sound(derezzedSFX_dir)
            derezzed_sound.set_volume(0.08)
            derezzed_sound.play()
            stop_sound = False

        show_score(stop_blue,stop_yellow)

        pygame.display.flip() # atualiza o display