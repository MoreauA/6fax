import pygame
import math
from Model.Map import *

SALADE = pygame.image.load('View/Data/Monster/Salade.png')
AUBERGINE = pygame.image.load('View/Data/Monster/aubergine.png')
MAISGUNNER = pygame.image.load('View/Data/Monster/Maïs.png')


RESSORT_NORMAL = pygame.image.load('View/Data/Map/Ressort1.png')
RESSORT_LOAD = pygame.image.load('View/Data/Map/Ressort2.png')
RESSORT_UNLOAD = pygame.image.load('View/Data/Map/Ressort3.png')

RESSORT_TRIGGER = False

def drawMap(window,x,y,width):
    pygame.draw.rect(window, (255, 0, 0), pygame.Rect(x, y, width, 20))
    pygame.draw.rect(window, (255, 0, 0), pygame.Rect(x, y, 20, width))
    pygame.draw.rect(window, (255, 0, 0), pygame.Rect(x, (y + width - 20), width, 20))
    pygame.draw.rect(window, (255, 0, 0), pygame.Rect((x + width - 20), y, 20, width))

    # for plat in listPlatForm:
    #     pygame.draw.rect(window, (125, 0, 0), pygame.Rect(plat.pos[0], plat.pos[1], plat.size[0], plat.size[1]))

def drawMonster(window,monster,ratio):

    posX = monster.pos[0]
    posY = monster.pos[1]
    width = monster.size[0]
    heigth = monster.size[1]

    if monster.isMoving():
        posX += monster.speed[0] * ratio
        posY += monster.speed[1] * ratio

    #ICI on peut draw le monster à la position indiquer :
    if monster.value == 4:
        # C'est une salade
        image = pygame.transform.scale(SALADE, (width, heigth))
        window.blit(image, (posX, posY))
    elif monster.value == 2:
        # C'est une tomate
        pygame.draw.rect(window, (150, 0, 0), pygame.Rect(posX, posY, width, heigth))
    elif monster.value == 16:
        # C'est une aubergine
        image = pygame.transform.scale(AUBERGINE, (width, heigth))

        if monster.wall == 2:
            image = pygame.transform.rotate(AUBERGINE, -90)
            image = pygame.transform.scale(image, (width, heigth))
        elif monster.wall == 3:
            image = pygame.transform.rotate(image, 180)
        elif monster.wall == 4:
            image = pygame.transform.rotate(AUBERGINE, 90)
            image = pygame.transform.scale(image, (width, heigth))

        window.blit(image, (posX, posY))
    elif monster.value == 10:
        # C'est un maïs
        image = pygame.transform.scale(MAISGUNNER, (width, heigth))

        if monster.wall == 2:
            image = pygame.transform.rotate(MAISGUNNER, -90)
            image = pygame.transform.scale(image, (width, heigth))
        elif monster.wall == 3:
            image = pygame.transform.rotate(image, 180)
        elif monster.wall == 4:
            image = pygame.transform.rotate(MAISGUNNER, 90)
            image = pygame.transform.scale(image, (width, heigth))

        window.blit(image, (posX, posY))

        for corn in monster.shots:
            shotX = int(corn.pos[0] + (corn.speed[0] * ratio))
            shotY = int(corn.pos[1] + (corn.speed[1] * ratio))
            pygame.draw.circle(window, (238, 201, 0), (shotX, shotY), corn.size[0])

def drawPlayer(window,player,ratio):

    posX = player.pos[0]
    posY = player.pos[1]

    if player.isMoving():
        posX += player.speed[0] * ratio
        posY += player.speed[1] * ratio

    pygame.draw.rect(window, (0, 150, 0), pygame.Rect(posX, posY, player.size[0], player.size[1]))

    for shot in player.shots:
        shotX = int(shot.pos[0] + (shot.speed[0]*ratio))
        shotY = int(shot.pos[1] + (shot.speed[1]*ratio))
        pygame.draw.circle(window, (0, 0, 0), (shotX, shotY), shot.size[0])

    #Draw the gun of the player :
    posMouse = pygame.mouse.get_pos()

    centerX = player.pos[0] + (player.size[0]/2)
    centerY = player.pos[1] + (player.size[1]/2)



    if player.shotDir == 1:
        cX = centerX
        cY = centerY - 15
        X = abs(cX+15 - posMouse[0])
        Y = abs(cY+15 - posMouse[1])
        if posMouse[1] < centerY:
            angle = math.degrees(math.atan(Y / (X+0.01)))
        else:
            angle = -math.degrees(math.atan(Y / (X+0.01)))

        img = pygame.transform.rotate(player.gunPicLeft, angle)
        window.blit(img, (cX, cY))
    else:
        cX = centerX - 30
        cY = centerY - 15
        X = abs(cX+15 - posMouse[0])
        Y = abs(cY+15 - posMouse[1])
        if posMouse[1] < centerY:
            angle = -math.degrees(math.atan(Y / (X+0.01)))
        else:
            angle = math.degrees(math.atan(Y / (X+0.01)))

        img = pygame.transform.rotate(player.gunPicRight, angle)
        window.blit(img, (cX, cY))

    # if posMouse[0] > player.pos[0] + player.size[0]:
    #
    # else:

    # window.blit(player.gunPicRight, (player.pos[0] + 50, player.pos[1] + 50))

def drawRessort(window, x, y, size, state):
    if state != 0:
        RESSORT_TRIGGER = True

    imageLoad = RESSORT_LOAD
    imageLoad = pygame.transform.scale(imageLoad, (50, 50))
    imageLoad = pygame.transform.rotate(imageLoad, 90)

    image = RESSORT_NORMAL
    image = pygame.transform.scale(image, (50, 50))
    image = pygame.transform.rotate(image, 90)

    # -50 pour taille des cube de l'arène (20)
    #           - taille image (20)
    #           - moitié taille image (10)

    #Haut droit :
    window.blit((imageLoad if state == 4 else image), (x + size - 70, y + 20))
    imageLoad = pygame.transform.rotate(imageLoad, 180)
    image = pygame.transform.rotate(image, 180)
    # Bas gauche :
    window.blit((imageLoad if state == 2 else image), (x + 20, y + size - 70))
    imageLoad = pygame.transform.rotate(imageLoad, -90)
    image = pygame.transform.rotate(image, -90)
    # Haut gauche :
    window.blit((imageLoad if state == 1 else image), (x + 20, y + 20))
    imageLoad = pygame.transform.rotate(imageLoad, 180)
    image = pygame.transform.rotate(image, 180)
    # Bas droit :
    window.blit((imageLoad if state == 3 else image), (x + size - 70, y + size - 70))
