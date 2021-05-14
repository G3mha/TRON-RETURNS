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

    # variável que absorve o clock do jogo
    clock = pygame.time.Clock()

    # variáveis iniciais do circulo
    spiderman_position = [0, 0]  # lista fria
    spiderman_velocity = [0.2, 0.27]  # variável fria

    # variáveis iniciais do circulo
    circle_position = [250,250]
    circle_var = {"left": 0, "right": 0, "up": 0, "down": 0}
    circle_velocity = 0.3
    circle_click = False  # variável fria

    BLACK = (0,0,0)
    RED = (255,0,0)
    YELLOW = (255,255,0)

    while True:  # Loop infinito do game
        time = clock.tick(60)  # segura a taxa de quadros em 60 por segundo
        surface.fill(BLACK)  # preenche o display em preto
        events = pygame.event.get()  # variável que absorve todos os eventos do jogo


        # eventos do jogo
        for event in events:
            # termina o jogo ao clicar ESC ou no X da aba
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            # eventos de pressionamento de tecla
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    circle_var["left"] = 1
                elif event.key == pygame.K_RIGHT:
                    circle_var["right"] = 1
                elif event.key == pygame.K_UP:
                    circle_var["up"] = 1
                elif event.key == pygame.K_DOWN:
                    circle_var["down"] = 1
                elif event.key == pygame.K_SPACE:
                    circle_click = True
            # eventos de despressionamento de tecla
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    circle_var["left"] = 0
                elif event.key == pygame.K_RIGHT:
                    circle_var["right"] = 0
                elif event.key == pygame.K_UP:
                    circle_var["up"] = 0
                elif event.key == pygame.K_DOWN:
                    circle_var["down"] = 0
                elif event.key == pygame.K_SPACE:
                    circle_click = False


        # Mudança no posicionamento do círculo, conforme pressionamento de tecla
        circle_position[0] += (circle_var["right"] - circle_var["left"]) * circle_velocity * time
        circle_position[1] += (circle_var["down"] - circle_var["up"]) * circle_velocity * time
        # Mudança na cor do círculo, conforme pressionamento da BARRA DE ESPAÇO
        if circle_click:
            pygame.draw.circle(surface, YELLOW, circle_position, 50)  # desenha um círculo amarelo
        else:
            pygame.draw.circle(surface, RED, circle_position, 50)  # desenha um círculo vermelho

        
        # faz com que o Spider Man se mova a cada atualização, respectivamente na horizontal e vertical
        spiderman_position[0] += spiderman_velocity[0] * time
        spiderman_position[1] += spiderman_velocity[1] * time
        # regula o movimento do Spider Man horizontalmente, para que ele não saia da tela
        if spiderman_position[0] > (surface.get_width())-(image.get_width()):
            spiderman_velocity[0] = -(spiderman_velocity[0])
            spiderman_position[0] = (surface.get_width())-(image.get_width())
        elif spiderman_position[0] < 0:
            spiderman_velocity[0] = -(spiderman_velocity[0])
            spiderman_position[0] = 0
        # regula o movimento do Spider Man verticalmente, para que ele não saia da tela
        if spiderman_position[1] > (surface.get_height())-(image.get_height()):
            spiderman_velocity[1] = -(spiderman_velocity[1])
            spiderman_position[1] = (surface.get_height())-(image.get_height())
        elif spiderman_position[1] < 0:
            spiderman_velocity[1] = -(spiderman_velocity[1])
            spiderman_position[1] = 0
        # mostra o Spider Man na tela
        surface.blit(image, spiderman_position)


        # Ajustes finos na tela
        pygame.display.flip()  # atualiza o que é mostrado na tela

if __name__ == '__main__':
    main()