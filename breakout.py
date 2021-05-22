#!/bin/python3
import pygame

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

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
