"""
Programa do mini-game_state de Motos
Autor: Enricco Gemha
Data: 18/05/2021
"""


import sys
import pygame
from classes_game1 import *
from classes_game2 import *
from classes_game3 import *
from functions import *


while True:
    restart_game = False
    # Algumas variáveis essenciais para a aplicação
    pygame.init()  # inicializa as rotinas do PyGame
    clock = pygame.time.Clock()

    b_score = 0
    y_score = 0

    # Rotinas de aúdio
    pygame.mixer.music.load('AUDIO/DerezzedSong.ogg')
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)
    
    time = clock.tick(60) # segura a taxa de quadros em 60 por segundo
    pygame.display.set_caption("TRON vs CLU") # título da surface do jogo
    surface = pygame.display.set_mode(SIZE_SCREEN) # cria a tela do jogo com tamanho personalizado

    initial_screen = True
    i=0
    while initial_screen:
        if i % 2 == 0:  # gera um efeito de letreiro piscante "aleatório"
            surface.blit(pygame.image.load('SOLID GAME SCREEN/game_front_page.jpeg'),(0,0))
        else:
            surface.blit(pygame.image.load('SOLID GAME SCREEN/game_insert_coin.png'),(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                initial_screen = False
        pygame.display.update()
        i+=1

    choose_screen = True
    while choose_screen:
        surface.blit(pygame.image.load('SOLID GAME SCREEN/selection_screen.jpeg'),(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game_access = "fastest_disc"
                    choose_screen = False
                if event.key == pygame.K_2:
                    game_access = "disc_wars"
                    choose_screen = False
                if event.key == pygame.K_3:
                    game_access = "lightcicle_run"
                    choose_screen = False
        pygame.display.update()



    y_score = 0
    b_score = 0
    while game_access == "disc_wars":
        page_title = "Disc Wars" # Define o nome desta página
        surface = pygame.display.set_mode(SIZE_SCREEN) # cria a tela do jogo com tamanho personalizado
        pygame.display.set_caption(page_title) # título da janela do jogo

        # variável que declara o clock do jogo
        clock = pygame.time.Clock()

        # cria sprite dos Paddles
        sprites = pygame.sprite.Group()
        yellow = Player(sprites, "yellow")
        blue = Player(sprites, "blue")

        # Variáveis para regular processos
        game_state = "RUNNING"
        b_disk_alive = False
        y_disk_alive = False
        pressed_blue = False
        pressed_yellow = False
        angle_index = 0
        sub_angle_index = 0
        v=0.2
        angle_list_1 = [(v,-v), (v,-v/2), (v,0), (v,v/2), (v,v)]
        angle_list_2 = [(-v,-v), (-v,-v/2), (-v,0), (-v,v/2), (-v,v)]

        if restart_game:
            break
        while True:
            time = clock.tick(60) # segura a taxa de quadros em 60 por segundo
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if event.type in (pygame.KEYDOWN, pygame.KEYUP):
                    blue.game_controls(event)
                    yellow.game_controls(event)
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            restart_game = True
                            break
                    if event.key == pygame.K_h:
                        if game_state != "HELPING":
                            pygame.mixer.music.pause()
                            help(game_access, surface)
                            game_state = "HELPING"
                        else:
                            pygame.mixer.music.unpause()
                            game_state = "RUNNING"
                    if event.key == pygame.K_p:
                        if game_state != "PAUSED":
                            pygame.mixer.music.pause()
                            surface.blit(pygame.image.load('SOLID GAME SCREEN/pause_menu_screen.png').convert_alpha(),(0,0))
                            game_state = "PAUSED"
                        else:
                            pygame.mixer.music.unpause()
                            game_state = "RUNNING"
                    if event.key == pygame.K_e and not pressed_blue and b_disk_alive != True:
                        pressed_blue = True
                    elif event.key == pygame.K_e and pressed_blue == True and b_disk_alive != True:
                        b_disk = Disk(sprites, 'blue', blue.rect.midright, angle_index)
                        b_disk_alive = True
                        pressed_blue = False
                    if event.key == pygame.K_RETURN and not pressed_yellow and y_disk_alive != True:
                        pressed_yellow = True
                    
                    elif event.key == pygame.K_RETURN and pressed_yellow == True and y_disk_alive != True:
                        y_disk = Disk(sprites, 'yellow', yellow.rect.midleft, angle_index)
                        y_disk_alive = True
                        pressed_yellow = False

            if restart_game:
                    break
            if game_state == "PAUSED" or game_state == "HELPING":
                pygame.display.flip()
                continue

            surface.blit(pygame.image.load('SPRITES_BOSS/wallpaper_disc_wars.png').convert_alpha(), (0,0))
            pygame.draw.line(surface, BLUE_ICE, (400,60), (400,800), 5)
                                
            if pressed_blue == True and b_disk_alive != True:
                v_15 = [int(angle_list_1[angle_index][0]*200), int(angle_list_1[angle_index][1]*200)]
                end_pos = ((list(blue.rect.center)[0] + v_15[0]),(list(blue.rect.center)[1] + v_15[1]))
                pygame.draw.line(surface, WHITE, blue.rect.center, end_pos, 5)

            if pressed_yellow == True and y_disk_alive != True:
                v_15_ = [int(angle_list_2[angle_index][0]*200), int(angle_list_2[angle_index][1]*200)]
                end_pos1 = ((list(yellow.rect.center)[0] + v_15_[0]),(list(yellow.rect.center)[1] + v_15_[1]))
                pygame.draw.line(surface, WHITE, yellow.rect.center, end_pos1, 5)

            sub_angle_index += 1
            if sub_angle_index == 12:
                sub_angle_index = 0
                angle_index += 1
            if angle_index > 4:
                angle_index = 0
            blue.update(time)
            yellow.update(time)

            if y_disk_alive == True:
                y_disk.update(time)
                if pygame.sprite.collide_mask(yellow,y_disk) != None:
                    y_disk.kill()
                    y_disk_alive = False    
                if pygame.sprite.collide_mask(blue,y_disk) != None:
                    y_score += 1
                    blue.kill()
                    blue = Player(sprites, "blue")
            if b_disk_alive == True:
                b_disk.update(time)
                if pygame.sprite.collide_mask(blue,b_disk) != None:
                    b_disk.kill()
                    b_disk_alive = False
                if pygame.sprite.collide_mask(yellow,b_disk) != None:
                    b_score += 1
                    yellow.kill()
                    yellow = Player(sprites, "yellow")

            sprites.draw(surface)
            score(y_score, b_score, surface)
            pygame.display.update()



    # # Breve tutorial de instruções deste modo de jogo
    # tutorial_screen(surface)

    y_score = 0
    b_score = 0
    while game_access == "lightcicle_run":
        page_title = "Lightcicle Chase" # Define o nome desta página
        surface = pygame.display.set_mode(SIZE_SCREEN) # cria a tela do jogo com tamanho personalizado
        pygame.display.set_caption(page_title) # título da janela do jogo

        # variável que declara o clock do jogo
        clock = pygame.time.Clock()
        
        # cria sprite das Motos
        sprites = pygame.sprite.Group()
        yellow = LightCicle(sprites, "LEFT", "yellow", (400, 200), (-VELOCITY_FAST, 0))
        blue = LightCicle(sprites, "RIGHT", "blue", (100, 400), (VELOCITY_FAST, 0))
        # Variáveis para regular processos
        stop_sound = True
        game_state = "RUNNING"
        game = True

        if restart_game:
            break
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
                    if event.key == pygame.K_BACKSPACE:
                        restart_game = True
                        break
                    if event.key == pygame.K_h:
                        if game_state != "HELPING":
                            pygame.mixer.music.pause()
                            help(game_access, surface)
                            game_state = "HELPING"
                        else:
                            pygame.mixer.music.unpause()
                            game_state = "RUNNING"
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
                            surface.blit(pygame.image.load('SOLID GAME SCREEN/pause_menu_screen.png').convert_alpha(),(0,0))
                            game_state = "PAUSED"
                        else:
                            pygame.mixer.music.unpause()
                            game_state = "RUNNING"

            if restart_game:
                break
            if game_state == "PAUSED" or game_state == "HELPING":
                pygame.display.flip()
                continue

            # Desenha o Background
            surface.fill(BLUE)
            thickness = 10
            distance = SIZE_SCREEN[0]/8 # espaço entre cada quadrado
            i = 0
            while i < 9:
                pygame.draw.line(surface, BLUE_MIDNIGHT, (0,(i*distance)), (SIZE_SCREEN[0],(i*distance)), thickness) # Desenha linha horizontal
                pygame.draw.line(surface, BLUE_MIDNIGHT, ((i*distance),0), ((i*distance),SIZE_SCREEN[0]), thickness) # Desenha linha vertical
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
        
    score_y = 0
    score_b = 0
    while game_access == "fastest_disc":
        PageTitle = "The Fastest Disc in the Grid" # Titulo da pagina
        surface = pygame.display.set_mode(SIZE_SCREEN) # cria a tela do jogo com tamanho personalizado
        pygame.display.set_caption(PageTitle) # título da janela do jogo


        sprites = pygame.sprite.Group()
        ydisks = pygame.sprite.Group()
        bdisks = pygame.sprite.Group()
        clu = CLU_BF(sprites)
        tron = TRON_BF(sprites)
        can_y_launch = True
        can_b_launch = True
        disk_y_n = 0
        disk_b_n = 0
        tron_died = False
        clu_died = False
        game_state = "RUNNING"

        ADD_YDISK = pygame.USEREVENT + 1
        pygame.time.set_timer(ADD_YDISK, 1000)
        ADD_BDISK = pygame.USEREVENT
        pygame.time.set_timer(ADD_BDISK, 3000)

        clock = pygame.time.Clock()

        if restart_game:
            break
        while True:    #True
            Time = clock.tick(60) # segura a taxa de quadros em 60 por segundo
            # Adquire todos os eventos e os testa para casos desejados
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): # quebra o loop
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        restart_game = True
                        break
                    if event.key == pygame.K_h:
                        if game_state != "HELPING":
                            pygame.mixer.music.pause()
                            help(game_access, surface)
                            game_state = "HELPING"
                        else:
                            pygame.mixer.music.unpause()
                            game_state = "RUNNING"
                    if event.key == pygame.K_s:
                        tron.duck()
                    if event.key == pygame.K_w:
                        tron.jump()
                    if event.key == pygame.K_d and can_b_launch:
                        can_b_launch = False
                        disk_b = Disk_BF(bdisks, "blue", (170,568))
                        disk_b_n += 1
                    if event.key == pygame.K_i and can_y_launch:
                        can_y_launch = False
                        disk_y = Disk_BF(ydisks, "yellow", (580,538))
                        disk_y_n += 1
                    if event.key == pygame.K_k and can_y_launch:
                        can_y_launch = False
                        disk_y = Disk_BF(ydisks, "yellow", (580,568))
                        disk_y_n += 1
                    if event.key == pygame.K_m and can_y_launch:
                        can_y_launch = False
                        disk_y = Disk_BF(ydisks, "yellow", (580,598))
                        disk_y_n += 1
                    if event.key == pygame.K_p:
                        if game_state != "PAUSED":
                            pygame.mixer.music.pause()
                            surface.blit(pygame.image.load('SOLID GAME SCREEN/pause_menu_screen.png').convert_alpha(),(0,0))
                            game_state = "PAUSED"
                        else:
                            pygame.mixer.music.unpause()
                            game_state = "RUNNING"

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_s:
                        tron.stand()
                if event.type == ADD_BDISK:
                    can_b_launch = True
                if event.type == ADD_YDISK:
                    can_y_launch = True

            if restart_game:
                break
            if game_state == "PAUSED" or game_state == "HELPING":
                pygame.display.update()
                continue

            surface.blit(pygame.image.load('SPRITES_BOSS/wallpaper_boss_fight.jpg').convert_alpha(), (0,0))

            sprites.draw(surface)
            tron.update(Time)

            score(score_y, score_b, surface)
            

            if disk_y_n != 0:
                ydisks.draw(surface)
                ydisks.update(Time)
                for disky in ydisks.sprites():
                    for diskb in bdisks.sprites():
                        if disk_b_n != 0: # Se a contagem for 0, não faz sentido verificar a colisão (perde o objeto da colisão)
                            if (pygame.sprite.collide_mask(diskb,disky)) != None:
                                diskb.kill()
                                disk_b_n -= 1
                                disky.kill()
                                disk_y_n -= 1
                    if disky.rect.x == 0:
                        disky.kill()
                        disk_y_n -= 1
                    if (pygame.sprite.collide_mask(tron,disky)) != None:
                        tron.kill()
                        score_y += 1
                        tron_died = True
            if disk_b_n != 0:
                bdisks.draw(surface)
                bdisks.update(Time)
                for diskb in bdisks.sprites():
                    if (pygame.sprite.collide_mask(clu,diskb)) != None:
                        clu.kill()
                        score_b += 1
                        clu_died = True
            

            if clu_died:
                break
            if tron_died:
                break

            pygame.display.update()