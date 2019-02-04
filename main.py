import pygame
from pygame.locals import *
import pygame.gfxdraw

pygame.init()

# welcome view
window = pygame.display.set_mode((1200,640))
window.fill((255,255,255))
runWelcome = 1


clickable_area = pygame.Rect((100, 100), (100, 100))
rect_surf = pygame.Surface(clickable_area.size)
rect_surf.fill([0,0,255])
window.blit(rect_surf, clickable_area)

while runWelcome:
    #loop to quit
    for event in pygame.event.get():
        if event.type == QUIT:
            runWelcome = 0

    pos = pygame.mouse.get_pos()
    if clickable_area.collidepoint(pos):
        print("success")

    window.blit(rect_surf,clickable_area)