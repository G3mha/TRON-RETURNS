# import pygame
# from configurations import yellow_dir, screen_size, lightcicle_size

# pygame.init()  # inicializa as rotinas do PyGame
# surface = pygame.display.set_mode(screen_size) # cria a tela do jogo com tamanho personalizado
# image = pygame.image.load(yellow_dir)
# # pygame.transform.scale(image, lightcicle_size)
# rect = image.get_rect()
# direction = "LEFT"
# last_direction = direction

# pygame.transform.flip(image, True, True)

# # Rotinas da tela estática
# surface.fill((0,0,0))

# # Início do main Loop
# game = True
# while game:
#     # Adquire todos os eventos e os testa para casos desejados
#     events = pygame.event.get()
#     for event in events:
#         if event.type == pygame.QUIT: # quebra o loop
#             game = False
#     surface.blit(image,(0,0))
#     pygame.display.update() # atualiza o display

# pygame.quit() # encerra o pygame