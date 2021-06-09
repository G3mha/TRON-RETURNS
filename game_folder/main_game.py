"""
Programa do mini-game de Motos
Autor: Enricco Gemha
Data: 18/05/2021
"""

import random
import sys
import pygame
from functions import yellowLightCicle, blueLightCicle, tutorial_screen, crash, draw_background, score

# Quantidade de vidas até o game-over
not_restart = False

# Estabelece a pasta que contem as sprites.
derezzedSFX_dir = 'AUDIO/DerezzedFX.ogg'
derezzedSONG_dir = 'AUDIO/DerezzedSong.ogg'

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

while True:
    if not_restart == True:
        break

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
    b_score = 0
    y_score = 0
    stop_sound = True
    boss_ticket = None
    restart_now = False
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
                    not_restart = True
                    restart_now = True
                if event.key == pygame.K_y:
                    not_restart = False
                    restart_now = True
                
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
                
                elif event.key == pygame.K_a:
                    yellow.update_direction("LEFT")
                elif event.key == pygame.K_d:
                    yellow.update_direction("RIGHT")
                elif event.key == pygame.K_s:
                    yellow.update_direction("UP")
                elif event.key == pygame.K_w:
                    yellow.update_direction("DOWN")
                elif event.key == pygame.K_RETURN:
                    yellow.slow_down()

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
        
        if restart_now == True:
            restart_now = False
            break

        draw_background()

        draw_trace()
        sprites.draw(surface) # desenha as sprites

        # Atualiza a posição da moto e rastro
        yellow.update(time)
        blue.update(time)

        # Verifica se houve colisão entre a moto e o rastro
        if yellow.explode:
            b_score += 1
        if blue.explode:
            y_score += 1
        for t in blue.trace:
            if yellow.rect.collidepoint(t):
                derezzed_visual = pygame.image.load('SPRITES/VFX DEREZZED EXPLOSION.png').convert_alpha()
                derezzed_visual = pygame.transform.scale(derezzed_visual, (80, 80))
                surface.blit(derezzed_visual, yellow.rect.center)
                b_score += 1
                yellow.kill()
        for t in yellow.trace:
            if blue.rect.collidepoint(t):
                derezzed_visual = pygame.image.load('SPRITES/VFX DEREZZED EXPLOSION.png').convert_alpha()
                derezzed_visual = pygame.transform.scale(derezzed_visual, (80, 80))
                surface.blit(derezzed_visual, blue.rect.center)
                y_score += 1
                blue.kill()
        if pygame.sprite.collide_mask(blue,yellow) != None:
            yellow.kill()
            blue.kill()

        if (b_score == False or y_score == False) and stop_sound == True:
            derezzed_sound = pygame.mixer.Sound(derezzedSFX_dir)
            derezzed_sound.set_volume(0.08)
            derezzed_sound.play()
            stop_sound = False

        score(b_score, y_score, surface)

        pygame.display.update() # atualiza o display
    
    while boss_ticket:
        a=0