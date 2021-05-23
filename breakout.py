#!/bin/python3
import pygame

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

class Block(pygame.sprite.Sprite):
    
    def __init__(self, color, x, y):  #Comentario das cores


        super().__init__()

        self.image = pygame.Surface([block_width, block_height])

        self.image.fill(color)

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y


class Ball(pygame.sprite.Sprite):

    speed = 10.0

    x = 0.0
    y = 180.0

    direction = 200

    width = 10
    height = 10

    def __init__(self):
        
        super().__init__()

        self.image = pygame.Surface([self.width, self.height])

        self.image.fill(white)

        self.rect = self.image.get_rect()

        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()

    def bounce(self, diff):

        self.direction = (180 - self.direction) % 360
        self.direction -= diff

    def update(self):

        direction_radians = math.radians(self.direction)

        self.x += self.speed * math.sin(direction_radians)
        self.y -= self.speed * math.cos(direction_radians)

        self.rect.x = self.x
        self.rect.y = self.y

        if self.y <= 0:
            self.bounce(0)
            self.y = 1

        if self.x <= 0:
            self.direction = (360 - self.direction) % 360
            self.x = 1

        if self.x > self.screenwidth - self.width:
            self.direction = (360 - self.direction) % 360
            self.x = self.screenwidth - self.width - 1

        if self.y > 600:
            return True
        else:
            return False

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Breakout')
pygame.mouse.set_visible(0)

clock = pygame.time.Clock()

game_over = False
exit_program = False

while not exit_program:
    screen.fill(COLOR_BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_program = True

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
