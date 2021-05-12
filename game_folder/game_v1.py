import sys
import pygame

pygame.init()  # inicializa as rotinas do PyGame

surface = pygame.display.set_mode((500,500))  # cria a tela do jogo com tamanho personalizado

surface.fill((0,0,0))  # preenche o display em preto

pygame.draw.circle(surface, (255,0,0), (250,250), 50)  # cria um círculo vermelho

pygame.display.update()  # atualiza o que é mostrado na tela

while True:  # Loop infinito do game
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()  # termina o pygame
            sys.exit()  # sai do jogo sem aparecer mensagem de erro