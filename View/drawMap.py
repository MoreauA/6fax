import pygame
import math

SALADE = pygame.image.load('View/Data/Monster/Salade.png')
AUBERGINE = pygame.image.load('View/Data/Monster/aubergine.png')
MAIS = pygame.image.load('View/Data/Monster/Maïs.png')

def drawMap(window,x,y,width):
    pygame.draw.rect(window, (255, 0, 0), pygame.Rect(x, y, width, 20))
    pygame.draw.rect(window, (255, 0, 0), pygame.Rect(x, y, 20, width))
    pygame.draw.rect(window, (255, 0, 0), pygame.Rect(x, (y + width - 20), width, 20))
    pygame.draw.rect(window, (255, 0, 0), pygame.Rect((x + width - 20), y, 20, width))

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
    elif monster.value = 10:
        image = pygame.transform.scale(AUBERGINE, (width, heigth))


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

def drawRessort(window, x, y, size):
    image = pygame.image.load('View/Data/ressort.png')
    image = pygame.transform.scale(image, (20, 20))
    image = pygame.transform.rotate(image, 45)

    # -50 pour taille des cube de l'arène (20)
    #           - taille image (20)
    #           - moitié taille image (10)


    window.blit(image, (x + size - 50, y + 20))
    window.blit(image, (x + 20, y + size - 50))

    image = pygame.transform.rotate(image, 90)
    window.blit(image, (x + 20, y + 20))
    window.blit(image, (x + size - 50, y + size - 50))
