"""
Programa principal do jogo
Autores: Enricco Gemha, Bruno Besnosik, Marcelo Rabello
Data: 13/05/2021
"""

import random
import sys
import pygame


# variáveis de cores
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)

class SpiderMan(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = pygame.image.load("SPRITE SPIDER MAN - Copia.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.set_position(0,0)
        self.set_velocity(0.2, 0.27)

    def set_position(self, x, y):
        self.position = pygame.math.Vector2(x,y)
    
    def set_velocity(self, vx, vy):
        self.velocity = pygame.math.Vector2(vx, vy)

    def update(self, time):
        width, height = pygame.display.get_surface().get_size()
        self.position += self.velocity * time
        self.rect.topleft = self.position
        # regula o movimento do Spider Man horizontalmente, para que ele não saia da tela
        if self.rect.right > width:
            self.velocity[0] = -abs(self.velocity[0])
            self.rect.right = width
        elif self.rect.x < 0:
            self.velocity[0] = abs(self.velocity[0])
            self.rect.x = 0
        # regula o movimento do Spider Man verticalmente, para que ele não saia da tela
        if self.rect.bottom > height:
            self.velocity[1] = -abs(self.velocity[1])
            self.rect.bottom = height
        elif self.rect.y < 0:
            self.velocity[1] = abs(self.velocity[1])
            self.rect.y = 0


def main():
    """Rotina principal do jogo"""
    pygame.init()  # inicializa as rotinas do PyGame
    surface = pygame.display.set_mode((500,500))  # cria a tela do jogo com tamanho personalizado
    pygame.display.set_caption("Spider Man Game")

    # Rotinas de aúdio
    pygame.mixer.music.load("Spiderman.mp3")
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(-1)
    shot_sound = pygame.mixer.Sound("preview.mp3")

    font = pygame.font.Font(pygame.font.get_default_font(), 18)

    # variáveis iniciais do circulo
    circle_position = [surface.get_width()/2,surface.get_height()/2]
    circle_var = {"left": 0, "right": 0, "up": 0, "down": 0}
    circle_velocity = 0.3
    space_bar = False
    mouse_button = False

    sprites = pygame.sprite.Group()

    # variável que absorve o clock do jogo
    clock = pygame.time.Clock()

    pygame.time.set_timer(pygame.USEREVENT, 1000)  # timer de 1 segundo para cada evento

    last = 0
    score = 0
    
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
                    space_bar = True
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
                    space_bar = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_button = True
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_button = False

            if event.type == pygame.MOUSEMOTION:
                circle_position = list(pygame.mouse.get_pos())

            if event.type == pygame.USEREVENT:
                spiderman = SpiderMan(sprites)  # cria sprite do Spider Man e coloca no Sprites
                spiderman.set_position(random.randint(0, surface.get_width()-spiderman.image.get_width()),
                                       random.randint(0, surface.get_height()-spiderman.image.get_height()))
                spiderman.set_velocity(random.uniform(-0.3,0.3), random.uniform(-0.3,0.3))

        sprites.update(time)
        sprites.draw(surface)
        # Mudança no posicionamento do círculo, conforme pressionamento de tecla
        circle_position[0] += (circle_var["right"] - circle_var["left"]) * circle_velocity * time
        circle_position[1] += (circle_var["down"] - circle_var["up"]) * circle_velocity * time
        
        click = space_bar or mouse_button

        current = pygame.time.get_ticks()

        # Mudança na cor do círculo, conforme pressionamento da BARRA DE ESPAÇO
        if click and (current - last > 500):
            last = current
            shot_sound.play()
            pygame.draw.circle(surface, YELLOW, circle_position, 4)  # desenha um círculo amarelo

            for sprite in sprites:
                if sprite.rect.collidepoint(circle_position):
                    mask_point = [int(circle_position[0] - sprite.rect.x), int(circle_position[1] - sprite.rect.y)]
                    if sprite.mask.get_at(mask_point):
                        sprite.kill()
                        score += 1
        else:
            pygame.draw.circle(surface, RED, circle_position, 3)  # desenha um círculo vermelho
        
        text = font.render("Placar: {}".format(score), True, WHITE)
        surface.blit(text, (10,0))
        # Ajustes finos na tela
        pygame.display.flip()  # atualiza o que é mostrado na tela

if __name__ == '__main__':
    main()