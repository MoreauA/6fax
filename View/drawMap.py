import pygame
import math
from Model.Map import *

# MAP = pygame.image.load('View/Data/Map/Map.png')

LIFE = pygame.image.load('View/Data/Map/coeur.png')
DEMILIFE = pygame.image.load('View/Data/Map/moitie_coeur.png')
DIE = pygame.image.load('View/Data/Map/coeur_mort.png')

TACOS = pygame.image.load('View/Data/Map/tacos.png')
SHOOT = pygame.image.load('View/Data/Player/salve_poivre.png')
FRITE = pygame.image.load('View/Data/Map/frite.png')

SALADE = pygame.image.load('View/Data/Monster/Salade.png')
AUBERGINE = [pygame.image.load('View/Data/Monster/Aubergine/1.png'), pygame.image.load('View/Data/Monster/Aubergine/2.png'), pygame.image.load('View/Data/Monster/Aubergine/4.png')]
MAISGUNNER = pygame.image.load('View/Data/Monster/Maïs.png')
TOMATE = pygame.image.load('View/Data/Monster/Tomate.png')

# IMPACT = [pygame.image.load('View/Data/Map/Animation/Shot/0.png'), pygame.image.load('View/Data/Map/Animation/Shot/1.png'), pygame.image.load('View/Data/Map/Animation/Shot/2.png'), pygame.image.load('View/Data/Map/Animation/Shot/3.png'), pygame.image.load('View/Data/Map/Animation/Shot/4.png')]

RESSORT_NORMAL = pygame.image.load('View/Data/Map/Ressort1.png')
RESSORT_LOAD = pygame.image.load('View/Data/Map/Ressort2.png')
RESSORT_UNLOAD = pygame.image.load('View/Data/Map/Ressort3.png')

RESSORT_TRIGGER = False

# SHOT = pygame.image.load('')

PLAYER_RIGHT = [pygame.transform.scale(pygame.image.load('View/Data/Player/Body/1.png'), (70, 80)),pygame.transform.scale(pygame.image.load('View/Data/Player/Body/2.png'), (70, 80)),pygame.transform.scale(pygame.image.load('View/Data/Player/Body/3.png'), (70, 80)), pygame.transform.scale(pygame.image.load('View/Data/Player/Body/4.png'), (70, 80)),pygame.transform.scale(pygame.image.load('View/Data/Player/Body/5.png'), (70, 80)),pygame.transform.scale(pygame.image.load('View/Data/Player/Body/6.png'), (70, 80)), pygame.transform.scale(pygame.image.load('View/Data/Player/Body/7.png'), (70, 80)),pygame.transform.scale(pygame.image.load('View/Data/Player/Body/8.png'), (70, 80)), pygame.transform.scale(pygame.image.load('View/Data/Player/Body/9.png'), (70, 80)),pygame.transform.scale(pygame.image.load('View/Data/Player/Body/10.png'), (70, 80))]
PLAYER_LEFT = [pygame.transform.scale(pygame.transform.flip(pygame.image.load('View/Data/Player/Body/1.png'), True, False), (70, 80)), pygame.transform.scale(pygame.transform.flip(pygame.image.load('View/Data/Player/Body/2.png'), True, False), (70, 80)), pygame.transform.scale(pygame.transform.flip(pygame.image.load('View/Data/Player/Body/3.png'), True, False), (70, 80)), pygame.transform.scale(pygame.transform.flip(pygame.image.load('View/Data/Player/Body/4.png'), True, False), (70, 80)), pygame.transform.scale(pygame.transform.flip(pygame.image.load('View/Data/Player/Body/5.png'), True, False), (70, 80)), pygame.transform.scale(pygame.transform.flip(pygame.image.load('View/Data/Player/Body/6.png'), True, False), (70, 80)), pygame.transform.scale(pygame.transform.flip(pygame.image.load('View/Data/Player/Body/7.png'), True, False), (70, 80)), pygame.transform.scale(pygame.transform.flip(pygame.image.load('View/Data/Player/Body/8.png'), True, False), (70, 80)), pygame.transform.scale(pygame.transform.flip(pygame.image.load('View/Data/Player/Body/9.png'), True, False), (70, 80)), pygame.transform.scale(pygame.transform.flip(pygame.image.load('View/Data/Player/Body/10.png'), True, False), (70, 80))]
PLAYER = [pygame.transform.scale(pygame.transform.flip(pygame.image.load('View/Data/Player/Body/0.png'), True, False), (70, 80)), pygame.transform.scale(pygame.image.load('View/Data/Player/Body/0.png'),(70,80))]

walkcount = 0
currFrame = 0

mapAnimation = []

def drawMap(window,x,y,width):
    # Draw arene
    pygame.draw.rect(window, (255, 0, 0), pygame.Rect(x, y, width, 20))
    pygame.draw.rect(window, (255, 0, 0), pygame.Rect(x, y, 20, width))
    pygame.draw.rect(window, (255, 0, 0), pygame.Rect(x, (y + width - 20), width, 20))
    pygame.draw.rect(window, (255, 0, 0), pygame.Rect((x + width - 20), y, 20, width))

    # window.blit(MAP, (x, 0))

def drawPlatForm(window, listPlatForm):
    for plat in listPlatForm:

        image = pygame.transform.scale(FRITE, (plat.size[0], plat.size[1]))

        if plat.size[0] < plat.size[1]:
            image = pygame.transform.rotate(FRITE, 90)
            image = pygame.transform.scale(image, (plat.size[0], plat.size[1]))

        window.blit(image, (plat.pos[0], plat.pos[1]))

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
        monster.animation += 1
        if monster.animation == 30:
            monster.animation = 0
            monster.state += 1
            if monster.state == 3:
                monster.state = 0

        image = pygame.transform.scale(AUBERGINE[monster.state], (width, heigth))

        if monster.right and (monster.wall == 2 or monster.wall == 4):
            image = pygame.transform.flip(image, True, False)

        elif monster.left and (monster.wall == 1 or monster.wall == 3):
            image = pygame.transform.flip(image, True, False)


        if monster.wall == 2:
            image = pygame.transform.rotate(image, -90)
            image = pygame.transform.scale(image, (width, heigth))
        elif monster.wall == 3:
            image = pygame.transform.rotate(image, 180)
        elif monster.wall == 4:
            image = pygame.transform.rotate(image, 90)
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
        pygame.draw.rect(window, (0, 150, 0), pygame.Rect(posX+decalage, posY-decalage, width-decalage, decalage))
        if pxVieEnleve != 0:
            pygame.draw.rect(window, (200, 0, 0), pygame.Rect(posX+decalage, posY-decalage, pxVieEnleve, decalage))
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
        pygame.draw.rect(window, (0, 150, 0), pygame.Rect(posX - (2*decalage), posY + decalage, decalage, heigth - decalage))
        if pxVieEnleve != 0:
            pygame.draw.rect(window, (200, 0, 0), pygame.Rect(posX - (2*decalage), posY + decalage, decalage, pxVieEnleve))

def drawPlayer(window,player,ratio):
    # ==================================================================================
    # Draw life
    taille = 25

    if player.life % 1 == 0 or player.life == 0:
        player.life = int(player.life)
        for i in range(0, player.life):
            image = pygame.transform.scale(LIFE, (taille, taille))
            window.blit(image, (2*i+taille*i, 258))

        for i in range(0, player.MAXLIFE - player.life):
            image = pygame.transform.scale(DIE, (taille, taille))
            window.blit(image, (2*(i+player.life) + taille*(i+player.life), 258))
    else:
        for i in range(0, int(player.life-0.5)):
            image = pygame.transform.scale(LIFE, (taille, taille))
            window.blit(image, (2 * i + taille * i, 258))

        image = pygame.transform.scale(DEMILIFE, (taille, taille))
        window.blit(image, (2*(player.life-0.5) + taille*(player.life-0.5), 258))

        for i in range(0, player.MAXLIFE - int(player.life-0.5)):
            image = pygame.transform.scale(DIE, (taille, taille))
            window.blit(image, (2 * (i + player.life - 0.5) + taille * (i + player.life - 0.5), 258))
    # ==================================================================================

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
            window.blit(pygame.transform.rotate((PLAYER[1] if player.shotDir == 0 else PLAYER[0]), -90), (posX, posY))
        elif player.left:
            window.blit(pygame.transform.rotate((PLAYER_LEFT[currFrame]), -90), (posX, posY))
        elif player.right:
            window.blit(pygame.transform.rotate((PLAYER_RIGHT[currFrame]), -90), (posX, posY))
        else:
            window.blit(pygame.transform.rotate((PLAYER[1] if player.shotDir == 1 else PLAYER[0]), -90), (posX, posY))

    elif player.wall == 3:
        if not player.left and not player.right:
            window.blit(pygame.transform.rotate((PLAYER[1] if player.shotDir == 0 else PLAYER[0]), 180), (posX, posY))
        elif player.left:
            window.blit(pygame.transform.rotate((PLAYER_RIGHT[currFrame]), 180), (posX, posY))
        elif player.right:
            window.blit(pygame.transform.rotate((PLAYER_LEFT[currFrame]), 180), (posX, posY))
        else:
            window.blit(pygame.transform.rotate((PLAYER[1] if player.shotDir == 1 else PLAYER[0]), 180), (posX, posY))

    elif player.wall == 4:
        if not player.left and not player.right:
            window.blit(pygame.transform.rotate((PLAYER[0] if player.shotDir == 0 else PLAYER[1]), 90), (posX, posY))
        elif player.left:
            window.blit(pygame.transform.rotate((PLAYER_RIGHT[currFrame]), 90), (posX, posY))
        elif player.right:
            window.blit(pygame.transform.rotate((PLAYER_LEFT[currFrame]), 90), (posX, posY))
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
        image = pygame.transform.scale(SHOOT, (shot.size[0], shot.size[1]))
        window.blit(image, (shot.pos[0], shot.pos[1]))

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

def drawBufs(window, map):

    for buf in map.bufs:

        if buf.duration + 10 >= map.timeActual() >= buf.duration:
            # le temps où il doit apparaître est dépassé
            # apparition de l'élement
            if buf.type == "tacos":
                image = pygame.transform.scale(TACOS, (buf.SIZE, buf.SIZE))

                if buf.wall == 2:
                    image = pygame.transform.rotate(TACOS, -90)
                    image = pygame.transform.scale(image, (buf.SIZE, buf.SIZE))
                elif buf.wall == 3:
                    image = pygame.transform.rotate(image, 180)
                elif buf.wall == 4:
                    image = pygame.transform.rotate(TACOS, 90)
                    image = pygame.transform.scale(image, (buf.SIZE, buf.SIZE))

            else: # c'est une vie
                image = pygame.transform.scale(LIFE, (buf.SIZE, buf.SIZE))

                if buf.wall == 2:
                    image = pygame.transform.rotate(LIFE, -90)
                    image = pygame.transform.scale(image, (buf.SIZE, buf.SIZE))
                elif buf.wall == 3:
                    image = pygame.transform.rotate(image, 180)
                elif buf.wall == 4:
                    image = pygame.transform.rotate(LIFE, 90)
                    image = pygame.transform.scale(image, (buf.SIZE, buf.SIZE))

            window.blit(image, (buf.pos[0], buf.pos[1]))




