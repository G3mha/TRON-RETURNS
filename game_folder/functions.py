import sys
import pygame
import random
import numpy as np
from classes_game1 import *
from classes_game2 import *
from classes_game3 import *


# Define o código RGB das cores utilizadas
BLACK = (0,0,0)
BLUE = (12,12,100)
BLUE_MIDNIGHT = (0,0,30)
BLUE_ICE = (0,255,251)
WHITE = (255,255,255)
YELLOW_GOLD = (255,215,0)


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
