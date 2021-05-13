import os
import sys
import pygame

pygame.init()  # inicializa as rotinas do PyGame

surface = pygame.display.set_mode((500,500))  # cria a tela do jogo com tamanho personalizado

try:
    image = pygame.image.load("SPRITE SPIDER MAN - Copia.png")
except pygame.error:
    print("Erro ao tentar ler imagem: SPRITE SPIDER MAN - Copia.png")
    sys.exit()

clock = pygame.time.Clock()

position = 0  # variável fria

while True:  # Loop infinito do game
    time = clock.tick(60)  # segura a taxa de quadros em 60 por segundo
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()  # termina o pygame
            sys.exit()  # sai do jogo sem aparecer mensagem de erro
    surface.fill((0,0,0))  # preenche o display em preto
    position += 0.2 * time # faz com que a imagem se mova a cada atualização
    surface.blit(image, [position,0])  # mostra a imagem na tela
    pygame.draw.circle(surface, (255,0,0), (250,250), 50)  # cria um círculo vermelho
    pygame.display.flip()  # atualiza o que é mostrado na tela
