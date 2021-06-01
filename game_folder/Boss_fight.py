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

disk_

############################
# Rotina principal do game #
############################

pygame.init() # inicia o pygame
surface =  pygame.display.set_mode(screen_size) #tamanho tela
pygame.display.set_caption(PageTitle) # titulo tela
clock = pygame.time.Clock() #Fps
while True:    #True
    Time = clock.tick(60) # segura a taxa de quadros em 60 por segundo
    # Adquire todos os eventos e os testa para casos desejados
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): # quebra o loop
                pygame.quit()
                sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                #-- TODO --#
                a = 0 #enchendo linguica
            if event.key == pygame.K_UP:
                #-- TODO --#
                a = 0 #enchendo linguica
            if event.key == pygame.K_LEFT:
                #-- TODO --#
                a = 0 #enchendo linguica
            if event.key == pygame.K_RIGHT:
                #-- TODO --#
                a = 0 #enchendo linguica
            if event.key == pygame.K_SPACE:
                #-- TODO --#
                a = 0 #enchendo linguica
    surface.fill(BLACK)