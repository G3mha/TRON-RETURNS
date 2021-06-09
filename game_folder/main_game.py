"""
Programa do mini-game_state de Motos
Autor: Enricco Gemha
Data: 18/05/2021
"""

import random
import sys
import pygame
from functions import yellowLightCicle, blueLightCicle, tutorial_screen, score


# Algumas variáveis essenciais para a aplicação
screen_size = (800,800) # Largura e altura da tela

# Define o código RGB das cores utilizadas
BLACK = (0,0,0)
BLUE_MIDNIGHT = (0,0,30)
BLUE = (12,12,100)
BLUE_ICE = (0,255,251)
YELLOW_GOLD = (255,215,0)
WHITE = (255,255,255)

b_score = 0
y_score = 0
while True:

    # Rotina Inicial do jogo
    pygame.init()  # inicializa as rotinas do PyGame
    surface = pygame.display.set_mode(screen_size) # cria a tela do jogo com tamanho personalizado
    page_title = "Corrida de motos" # Define o nome desta página
    pygame.display.set_caption(page_title) # título da janela do jogo

    # Rotinas de aúdio
    pygame.mixer.music.load('AUDIO/DerezzedSong.ogg')
    pygame.mixer.music.set_volume(0.04)
    pygame.mixer.music.play(-1)

    # Breve tutorial de instruções deste modo de jogo
    tutorial_screen(surface)

    # variável que declara o clock do jogo
    clock = pygame.time.Clock()

    # cria sprite das Motos
    sprites = pygame.sprite.Group()
    yellow = yellowLightCicle(sprites)
    blue = blueLightCicle(sprites)

    # Variáveis para regular processos
    stop_sound = True
    game_state = "RUNNING"
    game = True

    # variáveis de fonte
    font_paused = pygame.font.Font(pygame.font.get_default_font(), 40)

    # Início do Loop da corrida de moto
    while game:
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
                    if game_state != "PAUSED":
                        pygame.mixer.music.pause()
                        surface.blit(pygame.image.load('SOLID GAME SCREEN/pause_menu_screen.jpeg').convert_alpha(),(0,0))
                        game_state = "PAUSED"
                    else:
                        pygame.mixer.music.unpause()
                        game_state = "RUNNING"

        if game_state == "PAUSED":
            pygame.display.flip()
            continue

        # Desenha o Background
        surface.fill(BLUE)
        thickness = 10
        distance = screen_size[0]/8 # espaço entre cada quadrado
        i = 0
        while i < 9:
            pygame.draw.line(surface, BLUE_MIDNIGHT, (0,(i*distance)), (screen_size[0],(i*distance)), thickness) # Desenha linha horizontal
            pygame.draw.line(surface, BLUE_MIDNIGHT, ((i*distance),0), ((i*distance),screen_size[0]), thickness) # Desenha linha vertical
            i+=1

        # Desenha o rastro, que cessa quando há uma explosão
        if yellow.explode == False and blue.explode == False:
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
        yellow.update(time)
        blue.update(time)

        # Verifica se houve colisão
        if yellow.explode:
            b_score += 1
            game = False
        if blue.explode:
            y_score += 1
            game = False
        for t in blue.trace:
            if yellow.rect.collidepoint(t):
                derezzed_visual = pygame.image.load('SPRITES/VFX DEREZZED EXPLOSION.png').convert_alpha()
                derezzed_visual = pygame.transform.scale(derezzed_visual, (80, 80))
                surface.blit(derezzed_visual, yellow.rect.center)
                yellow.kill()
                b_score += 1
                game = False
                break
        for t in yellow.trace:
            if blue.rect.collidepoint(t):
                derezzed_visual = pygame.image.load('SPRITES/VFX DEREZZED EXPLOSION.png').convert_alpha()
                derezzed_visual = pygame.transform.scale(derezzed_visual, (80, 80))
                surface.blit(derezzed_visual, blue.rect.center)
                blue.kill()
                y_score += 1
                game = False
                break
        if pygame.sprite.collide_mask(blue,yellow) != None:
            yellow.kill()
            blue.kill()
            game = False

        if (b_score == False or y_score == False) and stop_sound == True:
            derezzed_sound = pygame.mixer.Sound('AUDIO/DerezzedFX.ogg')
            derezzed_sound.set_volume(0.08)
            derezzed_sound.play()
            stop_sound = False

        score(y_score, b_score, surface)

        pygame.display.update() # atualiza o display
    
    # while boss_ticket:
    #     a=0