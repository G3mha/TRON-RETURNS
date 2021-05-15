"""
Programa principal do jogo
Autores: Enricco Gemha, Bruno Besnosik, Marcelo Rabello
Data: 13/05/2021
"""

import os
import sys
import pygame


# variáveis de cores
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)


class SpiderMan(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        try:
            self.image = pygame.image.load("SPRITE SPIDER MAN - Copia.png").convert_alpha()
        except pygame.error:
            print("Erro ao tentar ler imagem: SPRITE SPIDER MAN - Copia.png")
            sys.exit()
        self.velocity = [0.2, 0.27]  # lista de velocidades horizontal e vertical
        self.rect = self.image.get_rect()
    
    def update(self, time):
        width, height = pygame.display.get_surface().get_size()
        self.rect.x += self.velocity[0] * time
        self.rect.y += self.velocity[1] * time
        # regula o movimento do Spider Man horizontalmente, para que ele não saia da tela
        if self.rect.x > width-(self.rect.width):
            self.velocity[0] = -(self.velocity[0])
            self.rect.x = width-(self.rect.width)
        elif self.rect.x < 0:
            self.velocity[0] = -(self.velocity[0])
            self.rect.x = 0
        # regula o movimento do Spider Man verticalmente, para que ele não saia da tela
        if self.rect.y > height-(self.rect.height):
            self.velocity[1] = -(self.velocity[1])
            self.rect.y = height-(self.rect.height)
        elif self.rect.y < 0:
            self.velocity[1] = -(self.velocity[1])
            self.rect.y = 0


def main():
    """Rotina principal do jogo"""
    pygame.init()  # inicializa as rotinas do PyGame
    surface = pygame.display.set_mode((500,500))  # cria a tela do jogo com tamanho personalizado
    pygame.display.set_caption("Spider Man Game")


    # variáveis iniciais do circulo
    circle_position = [250,250]
    circle_var = {"left": 0, "right": 0, "up": 0, "down": 0}
    circle_velocity = 0.3
    circle_click = False  # variável fria

    spiderman = SpiderMan()

    # variável que absorve o clock do jogo
    clock = pygame.time.Clock()


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
        
        # mostra o Spider Man na tela
        spiderman.update(time)
        surface.blit(spiderman.image, spiderman.rect)


        # Ajustes finos na tela
        pygame.display.flip()  # atualiza o que é mostrado na tela

if __name__ == '__main__':
    main()