# import pygame
from pygame.locals import *
import pygame.gfxdraw
from Model.Map import Map
import time
from View.Button import button
from View.drawMap import drawMap
from View.drawMap import drawMonster


NBLEVEL = 10
maps = []

pygame.init()

# welcome view
window = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Tacos Mania")
window.fill((255, 255, 255))
runWelcome = True

imgAubergine = pygame.image.load('aubergine.jpg')

#Création des maps
def chooseMaps():
    cadenas = pygame.image.load('cadenas.png')
    cadenasOuvert = pygame.image.load('cadenaOuvert.jpg')
    x = 10
    y = 10

    for i in range(NBLEVEL):
        map = Map(i, False)
        maps.append(map)

    for map in maps:
        if map.dislock:
            window.blit(cadenasOuvert, (x, y))
        else:
            window.blit(cadenas, (x, y))

        x += 50

        if x > 400:
            x = 10
            y += 50

    runChooseMap = True

    while runChooseMap:
        for event in pygame.event.get():
            if event.type == QUIT:
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

    def inputHandler(keys):
        if keys[pygame.K_a]:
            pygame.draw.rect(window, (0, 200, 0), pygame.Rect(10, 10, 50, 20))
            return False
        return True

    def update():
        currentMap.update()

    def renderMapWindow(ratioRender):
        window.fill((255, 255, 255))
        drawMap(window, posXMap, posYMap, sizeMap)
        for currentMob in currentMap.mobs():
            drawMonster(window, currentMob, ratioRender)
        # pygame.display.flip()
        pygame.display.update()

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
        keyPressed = pygame.key.get_pressed()
        if keyPressed[pygame.K_ESCAPE]:
            runMap = False
        inputHandler(keyPressed)

        while lag >= MS_PER_UPDATE:
            update()
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
start = button((0, 200, 0), posXButton, posYButton - 200, widthButton, 80, 'Tacos Mania') # To delete one day

#Buttons on the middle
arena = []
widthButton = 150
for i in range(0,10):
    arenaName = "Arène " + str(i+1)
    if i < 5:
        arena.append(button((0, 0, 200), (posXButton -350) + i*200, posYButton, widthButton, 80, arenaName))
    else:
        arena.append(button((0, 0, 200), (posXButton -350) + (i-5)*200, posYButton + 200, widthButton, 80, arenaName))

#Buttons on the bottom
widthButton = 250
boutique = button((0, 0, 200), posXButton -350 , posYButton + 400, widthButton, 80, 'Boutique')
score = button((0, 0, 200), posXButton, posYButton + 400, widthButton, 80, 'Score')
quit = button((200, 0, 0), posXButton +350, posYButton + 400, widthButton, 80, 'Quitter')

def redrawWindow():
    window.fill((255, 255, 255))
    start.draw(window)

    for val in range(0,10):
        arena[val].draw(window)

    boutique.draw(window)
    score.draw(window)
    quit.draw(window)
    window.blit(imgAubergine, (10, 20))

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
                chooseMaps()
                runWelcome = False
            elif score.isOver(pos):
                print("Success 2")
            elif quit.isOver(pos):
                runWelcome = False

# End welcome view
# =========================================================================================================================================

pygame.quit()