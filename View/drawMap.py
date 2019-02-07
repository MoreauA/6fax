import pygame
import math
from Model.Map import *

SALADE = pygame.image.load('View/Data/Monster/Salade.png')
AUBERGINE = pygame.image.load('View/Data/Monster/aubergine.png')
MAISGUNNER = pygame.image.load('View/Data/Monster/Maïs.png')
TOMATE = pygame.image.load('View/Data/Monster/Tomate.png')

RESSORT_NORMAL = pygame.image.load('View/Data/Map/Ressort1.png')
RESSORT_LOAD = pygame.image.load('View/Data/Map/Ressort2.png')
RESSORT_UNLOAD = pygame.image.load('View/Data/Map/Ressort3.png')

RESSORT_TRIGGER = False

PLAYER_RIGHT = [pygame.transform.scale(pygame.image.load('View/Data/Player/Body/1.png'), (70, 80)),pygame.transform.scale(pygame.image.load('View/Data/Player/Body/2.png'), (70, 80)),pygame.transform.scale(pygame.image.load('View/Data/Player/Body/3.png'), (70, 80)), pygame.transform.scale(pygame.image.load('View/Data/Player/Body/4.png'), (70, 80)),pygame.transform.scale(pygame.image.load('View/Data/Player/Body/5.png'), (70, 80)),pygame.transform.scale(pygame.image.load('View/Data/Player/Body/6.png'), (70, 80)), pygame.transform.scale(pygame.image.load('View/Data/Player/Body/7.png'), (70, 80)),pygame.transform.scale(pygame.image.load('View/Data/Player/Body/8.png'), (70, 80)), pygame.transform.scale(pygame.image.load('View/Data/Player/Body/9.png'), (70, 80)),pygame.transform.scale(pygame.image.load('View/Data/Player/Body/10.png'), (70, 80))]
PLAYER_LEFT = [pygame.transform.scale(pygame.transform.flip(pygame.image.load('View/Data/Player/Body/1.png'), True, False), (70, 80)), pygame.transform.scale(pygame.transform.flip(pygame.image.load('View/Data/Player/Body/2.png'), True, False), (70, 80)), pygame.transform.scale(pygame.transform.flip(pygame.image.load('View/Data/Player/Body/3.png'), True, False), (70, 80)), pygame.transform.scale(pygame.transform.flip(pygame.image.load('View/Data/Player/Body/4.png'), True, False), (70, 80)), pygame.transform.scale(pygame.transform.flip(pygame.image.load('View/Data/Player/Body/5.png'), True, False), (70, 80)), pygame.transform.scale(pygame.transform.flip(pygame.image.load('View/Data/Player/Body/6.png'), True, False), (70, 80)), pygame.transform.scale(pygame.transform.flip(pygame.image.load('View/Data/Player/Body/7.png'), True, False), (70, 80)), pygame.transform.scale(pygame.transform.flip(pygame.image.load('View/Data/Player/Body/8.png'), True, False), (70, 80)), pygame.transform.scale(pygame.transform.flip(pygame.image.load('View/Data/Player/Body/9.png'), True, False), (70, 80)), pygame.transform.scale(pygame.transform.flip(pygame.image.load('View/Data/Player/Body/10.png'), True, False), (70, 80))]
PLAYER = [pygame.transform.scale(pygame.transform.flip(pygame.image.load('View/Data/Player/Body/0.png'), True, False), (70, 80)), pygame.transform.scale(pygame.image.load('View/Data/Player/Body/0.png'),(70,80))]

walkcount = 0
currFrame = 0

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
        image = pygame.transform.scale(TOMATE, (width, heigth))

        if monster.wall == 2:
            image = pygame.transform.rotate(TOMATE, -90)
            image = pygame.transform.scale(image, (width, heigth))
        elif monster.wall == 3:
            image = pygame.transform.rotate(image, 180)
        elif monster.wall == 4:
            image = pygame.transform.rotate(TOMATE, 90)
            image = pygame.transform.scale(image, (width, heigth))

        window.blit(image, (posX, posY))
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

    # Dessin des vie au dessus des monstres
    decalage = 5
    if monster.alive:
        vieEnleve = monster.MAXLIFE - monster.life
        pourcentageVieEnleve = vieEnleve * 100 / monster.MAXLIFE
        if monster.wall != 2 and monster.wall != 4:
            pxVieEnleve = pourcentageVieEnleve*(width-decalage)/100
        else:
            pxVieEnleve = pourcentageVieEnleve*(heigth-decalage)/100
    else:
        if monster.wall != 2 and monster.wall != 4:
            pxVieEnleve = width-decalage
        else:
            pxVieEnleve = heigth-decalage

    if monster.wall == 1 or monster.wall == 0:
        # mur du bas ou vole
        pygame.draw.rect(window, (0, 150, 0), pygame.Rect(posX+decalage, posY+decalage, width-decalage, decalage))
        if pxVieEnleve != 0:
            pygame.draw.rect(window, (200, 0, 0), pygame.Rect(posX+decalage, posY+decalage, pxVieEnleve, decalage))
    elif monster.wall == 2:
        # mur de gauche
        pygame.draw.rect(window, (0, 150, 0), pygame.Rect(posX + width + decalage, posY + decalage, decalage, heigth - decalage))
        if pxVieEnleve != 0:
            pygame.draw.rect(window, (200, 0, 0), pygame.Rect(posX + width + decalage, posY + decalage, decalage, pxVieEnleve))
    elif monster.wall == 3:
        # mur du haut
        pygame.draw.rect(window, (0, 150, 0), pygame.Rect(posX + decalage, posY + heigth + decalage, width - decalage, decalage))
        if pxVieEnleve != 0:
            pygame.draw.rect(window, (200, 0, 0), pygame.Rect(posX + decalage, posY + heigth + decalage, pxVieEnleve, decalage))
    else:
        # mur de droite
        pygame.draw.rect(window, (0, 150, 0), pygame.Rect(posX - decalage, posY - decalage, decalage, heigth - decalage))
        if pxVieEnleve != 0:
            pygame.draw.rect(window, (200, 0, 0), pygame.Rect(posX - decalage, posY - decalage, decalage, pxVieEnleve))

def drawPlayer(window,player,ratio):
    global walkcount
    global currFrame

    if player.left or player.right:
        if walkcount == 20:
            walkcount = 0
            currFrame += 1
            if currFrame >= 9:
                currFrame = 0
        walkcount += 1
    else :
        walkcount = 0
        currFrame = 0

    posX = player.pos[0]
    posY = player.pos[1]

    if player.isMoving():
        posX += player.speed[0] * ratio
        posY += player.speed[1] * ratio

    if player.wall == 2:
        if not player.left and not player.right:
            window.blit(pygame.transform.rotate((PLAYER[0] if player.shotDir == 0 else PLAYER[1]), -90), (posX, posY))
        elif player.left:
            window.blit(pygame.transform.rotate((PLAYER_LEFT[currFrame]), -90), (posX, posY))
        elif player.right:
            window.blit(pygame.transform.rotate((PLAYER_RIGHT[currFrame]), -90), (posX, posY))
        else:
            window.blit(pygame.transform.rotate((PLAYER[0] if player.shotDir == 1 else PLAYER[1]), -90), (posX, posY))

    elif player.wall == 3:
        if not player.left and not player.right:
            window.blit(pygame.transform.rotate((PLAYER[0] if player.shotDir == 0 else PLAYER[1]), 180), (posX, posY))
        elif player.left:
            window.blit(pygame.transform.rotate((PLAYER_RIGHT[currFrame]), 180), (posX, posY))
        elif player.right:
            window.blit(pygame.transform.rotate((PLAYER_LEFT[currFrame]), 180), (posX, posY))
        else:
            window.blit(pygame.transform.rotate((PLAYER[0] if player.shotDir == 1 else PLAYER[1]), 180), (posX, posY))

    elif player.wall == 4:
        if not player.left and not player.right:
            window.blit(pygame.transform.rotate((PLAYER[0] if player.shotDir == 0 else PLAYER[1]), 90), (posX, posY))
        elif player.left:
            window.blit(pygame.transform.rotate((PLAYER_LEFT[currFrame]), 90), (posX, posY))
        elif player.right:
            window.blit(pygame.transform.rotate((PLAYER_RIGHT[currFrame]), 90), (posX, posY))
        else:
            window.blit(pygame.transform.rotate((PLAYER[0] if player.shotDir == 1 else PLAYER[1]), 90), (posX, posY))
    else:
        if not player.left and not player.right:
            window.blit((PLAYER[0] if player.shotDir == 0 else PLAYER[1]), (posX, posY))
        elif player.left:
            window.blit((PLAYER_LEFT[currFrame]), (posX, posY))
        elif player.right:
            window.blit((PLAYER_RIGHT[currFrame]), (posX, posY))
        else:
            window.blit((PLAYER[0] if player.shotDir == 1 else PLAYER[1]), (posX, posY))

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
