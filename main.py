import pygame
from pygame.locals import *
import pygame.gfxdraw

pygame.init()

# welcome view
window = pygame.display.set_mode((1200,640))
window.fill((255,255,255))
runWelcome = 1

Rectplace = pygame.gfxdraw.box(window, (100, 120, 100, 100), [0, 0, 255])
pygame.display.update()

while runWelcome:
    #loop to quit
    for event in pygame.event.get():
        if event.type == QUIT:
            runWelcome = 0

    pos = pygame.mouse.get_pos()
    if Rectplace.collidepoint(pos):
        print("success")