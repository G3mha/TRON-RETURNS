from pygame.constants import USEREVENT
from functions import Disk_BF, CLU_BF, TRON_BF
import pygame
import sys

PageTitle = "Final Boss" # Titulo da pagina
screen_size = (800,800)
###########################
# # # # # # RGB # # # # # # 
###########################

BLACK = (0,0,0)
BLUE_MIDNIGHT = (0,0,30)
BLUE = (12,12,100)
BLUE_ICE = (0,255,251)
YELLOW_GOLD = (255,215,0)
WHITE = (255,255,255)


sprites = pygame.sprite.Group()
clu = CLU_BF(sprites)
tron = TRON_BF(sprites)
can_y_launch = True
can_launch = True

############################
# Rotina principal do game #
############################

pygame.init() # inicia o pygame
surface =  pygame.display.set_mode(screen_size) #tamanho tela
pygame.display.set_caption(PageTitle) # titulo tela
clock = pygame.time.Clock() #Fps
pygame.time.set_timer(pygame.USEREVENT, 4000)  # timer de 4 segundos para cada evento
while True:    #True
    Time = clock.tick(60) # segura a taxa de quadros em 60 por segundo
    # Adquire todos os eventos e os testa para casos desejados
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): # quebra o loop
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                tron.crouch()
            if event.key == pygame.K_w:
                tron.jump()
            if event.key == pygame.K_d and can_launch:
                can_launch = False
                tron.launch_disk()
                disk_b = Disk_BF(sprites, "blue")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                tron.standing()
        if event.type == pygame.USEREVENT:
            can_launch = True

    if (pygame.time.get_ticks()) % 1000 == 0:
        can_y_launch = True
    surface.fill(BLACK)
    pygame.draw.line(surface, BLUE_MIDNIGHT, (0,400), (800,400), 10)


    tron.update(Time)
    sprites.draw(surface)
    
    # sprites.update(Time)

# Código extraído de https://codingshiksha.com/python/python-3-pygame-google-chrome-dinosaur-t-rex-dino-runner-game-gui-script-desktop-app-full-project-for-beginners/

    pygame.display.flip()

    # https://github.com/insper/pygame-snippets#fazendo-o-personagem-pular link de consulta