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
window = pygame.display.set_mode((700, 500))
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

start = button((0, 200, 0), posXButton, posYButton, widthButton, 80, '', 'Start')
score = button((0, 0, 200), posXButton, posYButton + 120, widthButton, 80, '', 'Score')
quit = button((200, 0, 0), posXButton, posYButton + 240, widthButton, 80, '', 'Quitter')

def redrawWindow():
    window.fill((255, 255, 255))
    start.draw(window)
    score.draw(window)
    quit.draw(window)
    #window.blit(imgAubergine, (10, 20))

while runWelcome:
    redrawWindow()
    pygame.display.update()
    #loop to quit
    for event in pygame.event.get():
        if event.type == QUIT:
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