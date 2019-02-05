import pygame

def drawMap(window,x,y,width):
    pygame.draw.rect(window, (255, 0, 0), pygame.Rect(x, y, width, 20))
    pygame.draw.rect(window, (255, 0, 0), pygame.Rect(x, y, 20, width))
    pygame.draw.rect(window, (255, 0, 0), pygame.Rect(x, (y + width - 20), width, 20))
    pygame.draw.rect(window, (255, 0, 0), pygame.Rect((x + width - 20), y, 20, width))
    pass

def drawMonster(window,monster,ratio):

    posX = monster.pos[0]
    posY = monster.pos[1]

    if monster.isMoving():
        posX += monster.speed[0] * ratio
        posY += monster.speed[1] * ratio

    #ICI on peut draw le monster à la position indiquer :
