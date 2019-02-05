# import pygame
from pygame.locals import *
import pygame.gfxdraw
from Model.Map import Map
import time
from View.Button import button
from View.drawMap import *

from Model.Mob import *


NBLEVEL = 10
maps = []

pygame.init()

# welcome view
window = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Tacos Mania")
window.fill((255, 255, 255))
runWelcome = True

#imgAubergine = pygame.image.load('aubergine.jpg')

#Création des maps
def chooseMaps():
    x = 10
    y = 10

    buttons = []

    for i in range(NBLEVEL):
        map = Map(i+1, False)
        maps.append(map)

    for map in maps:
        if map.dislock:
            accueil = button((255, 255, 255), x, y, 50, 50, 'cadenaOuvert.jpg', str(map.level))
            accueil.draw(window)
        else:
            accueil = button((255, 255, 255), x, y, 50, 50, 'cadenas.png', str(map.level))
            accueil.draw(window)

        buttons.append(accueil)
        x += 50

        if x > 400:
            x = 10
            y += 50

    pygame.display.flip()
    runChooseMap = True

    while runChooseMap:
        for event in pygame.event.get():
            if event.type == QUIT:
                runChooseMap = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                for b in buttons:
                    if b.isOver(pos):
                       window.fill((255, 255, 255))
                       mapGame(int(b.text))
                       runChooseMap = False


#=========================================================================================================================================
#Boucle de jeu :
def mapGame(idMap):
    #Environs 60 fps
    MS_PER_UPDATE = 10

    sizeMenu = 10
    sizeMap = pygame.display.get_surface().get_height() - sizeMenu
    posXMap = (pygame.display.get_surface().get_width() / 2) - (sizeMap / 2)
    posYMap = sizeMenu

    #20 est la valeur de l'épaisseur des murs :
    setCollider((posXMap+20), (posXMap+sizeMap-20), (posYMap+20), (posYMap+sizeMap-20))

    gravTime = time.time()

    def updateAll():
        currentMap.update()
        print("Update !")
        player.update()

    def renderMapWindow(ratioRender):
        window.fill((255, 255, 255))
        drawMap(window, posXMap, posYMap, sizeMap)
        for currentMob in currentMap.mobs():
            drawMonster(window, currentMob, ratioRender)
        # pygame.display.flip()
        drawPlayer(window, player, ratioRender)
        player.movement(False)
        pygame.display.update()

    player = Player([500, 350], 100, [40,40], 50)

    runMap = True
    currentMap = Map(idMap, 10) #What IS dislock ?
    previousTime = time.time()
    lag = 0.0

    while runMap:
        #Permet une gestion précise de la boucle de jeu principale :
        currentTime = time.time()
        elapsed = currentTime - previousTime
        previousTime = currentTime
        lag += elapsed

        #Gestion input:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            runMap = False

        if keys[pygame.K_z]:
            player.move([0, -1])
            player.movement(True)

        if keys[pygame.K_q]:
            player.move([-1, 0])
            player.movement(True)

        if keys[pygame.K_d]:
            player.move([1, 0])
            player.movement(True)

        if keys[pygame.K_s]:
            player.move([0, 1])
            player.movement(True)

        if keys[pygame.K_SPACE]:
            currentT = time.time()
            if currentT - gravTime >= 0.5:
                gravTime = currentT
                player.gravityShift([player.gravitation[0], -player.gravitation[1]])


        updateAll()
        while lag >= MS_PER_UPDATE:
            updateAll()
            lag -= MS_PER_UPDATE

        renderMapWindow(lag/MS_PER_UPDATE)
        #Take consideration of the event :
        pygame.event.pump()
#Fin de boucle de jeu
#=========================================================================================================================================

#=========================================================================================================================================
# Welcome View
widthButton = 250
posXButton = (pygame.display.get_surface().get_width() / 2) - ((1/2) * widthButton)
posYButton = (pygame.display.get_surface().get_height() / 3)

# Buttons on the top
start = button((0, 200, 0), posXButton, posYButton - 200, widthButton, 80, '', 'Tacos Mania') # To delete one day

#Buttons on the middle
arena = []
widthButton = 150
for i in range(0,10):
    arenaName = "Arène " + str(i+1)
    if i < 5:
        arena.append(button((0, 0, 200), (posXButton -350) + i*200, posYButton, widthButton, 80,'', arenaName))
    else:
        arena.append(button((0, 0, 200), (posXButton -350) + (i-5)*200, posYButton + 200, widthButton, 80,'', arenaName))

#Buttons on the bottom
widthButton = 250
boutique = button((0, 0, 200), posXButton -350 , posYButton + 400, widthButton, 80,'', 'Boutique')
score = button((0, 0, 200), posXButton, posYButton + 400, widthButton, 80,'', 'Score')
quit = button((200, 0, 0), posXButton +350, posYButton + 400, widthButton, 80,'', 'Quitter')

def redrawWindow():
    window.fill((255, 255, 255))
    start.draw(window)

    for val in range(0,10):
        arena[val].draw(window)

    boutique.draw(window)
    score.draw(window)
    quit.draw(window)
    #window.blit(imgAubergine, (10, 20))

while runWelcome:
    redrawWindow()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT: #If you click on the window's cross
            runWelcome = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if start.isOver(pos):
                window.fill((255, 255, 255))
                mapGame(1)
                # chooseMaps()
                runWelcome = False
            elif score.isOver(pos):
                print("Success 2")
            elif quit.isOver(pos):
                runWelcome = False

# End welcome view
# =========================================================================================================================================

pygame.quit()