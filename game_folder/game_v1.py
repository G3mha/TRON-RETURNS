"""
Programa principal do jogo
Autores: Enricco Gemha, Bruno Besnosik, Marcelo Rabello
Data: 13/05/2021
"""

import os
import sys
import pygame

def main():
    """Rotina principal do jogo"""
    pygame.init()  # inicializa as rotinas do PyGame

    surface = pygame.display.set_mode((500,500))  # cria a tela do jogo com tamanho personalizado

    pygame.display.set_caption("Spider Man Game")

    try:
        image = pygame.image.load("SPRITE SPIDER MAN - Copia.png").convert_alpha()
    except pygame.error:
        print("Erro ao tentar ler imagem: SPRITE SPIDER MAN - Copia.png")
        sys.exit()

    clock = pygame.time.Clock()


    spiderman_position = [0, 0]  # lista fria
    spiderman_velocity = [0.2, 0.27]  # variável fria

    circle_position = [250,250]
    circle_var = {"left": 0, "right": 0, "up": 0, "down": 0}
    circle_velocity = 0.3
    
    BLACK = (0,0,0)
    RED = (255,0,0)

    while True:  # Loop infinito do game
        time = clock.tick(60)  # segura a taxa de quadros em 60 por segundo
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()  # termina o pygame
                sys.exit()  # sai do jogo sem aparecer mensagem de erro

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    circle_var["left"] = 1
                elif event.key == pygame.K_RIGHT:
                    circle_var["right"] = 1
                elif event.key == pygame.K_UP:
                    circle_var["up"] = 1
                elif event.key == pygame.K_DOWN:
                    circle_var["down"] = 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    circle_var["left"] = 0
                elif event.key == pygame.K_RIGHT:
                    circle_var["right"] = 0
                elif event.key == pygame.K_UP:
                    circle_var["up"] = 0
                elif event.key == pygame.K_DOWN:
                    circle_var["down"] = 0

        circle_position[0] += (circle_var["right"] - circle_var["left"]) * circle_velocity * time
        circle_position[1] += (circle_var["down"] - circle_var["up"]) * circle_velocity * time

        surface.fill(BLACK)  # preenche o display em preto
        
        spiderman_position[0] += spiderman_velocity[0] * time # faz com que a imagem se mova a cada atualização
        spiderman_position[1] += spiderman_velocity[1] * time # faz com que a imagem se mova a cada atualização

        if spiderman_position[0] > (surface.get_width())-(image.get_width()):
            spiderman_velocity[0] = -(spiderman_velocity[0])
            spiderman_position[0] = (surface.get_width())-(image.get_width())

        elif spiderman_position[0] < 0:
            spiderman_velocity[0] = -(spiderman_velocity[0])
            spiderman_position[0] = 0
        
        if spiderman_position[1] > (surface.get_height())-(image.get_height()):
            spiderman_velocity[1] = -(spiderman_velocity[1])
            spiderman_position[1] = (surface.get_height())-(image.get_height())

        elif spiderman_position[1] < 0:
            spiderman_velocity[1] = -(spiderman_velocity[1])
            spiderman_position[1] = 0

        surface.blit(image, spiderman_position)  # mostra a imagem na tela
        
        pygame.draw.circle(surface, RED, circle_position, 50)  # cria um círculo vermelho
        pygame.display.flip()  # atualiza o que é mostrado na tela

if __name__ == '__main__':
    main()