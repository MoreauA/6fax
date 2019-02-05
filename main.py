# import pygame
from pygame.locals import *
import pygame.gfxdraw
from Model.Map import Map
import time
from View.Button import button
from View.drawMap import drawMap
from View.drawMap import drawMonster

pygame.init()

# welcome view
window = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
window.fill((255,255,255))
runWelcome = True
runMap = False

# button = pygame.Rect((100, 100), (100, 100))
# rect_surf = pygame.Surface(clickable_area.size)
# button.fill((0,0,255))
# b = window.blit(button, (300, 200))

# window.blit(rect_surf, clickable_area)
widthButton = 250
posXButton = (pygame.display.get_surface().get_width() / 2) - ((1/2) * widthButton)
posYButton =  (pygame.display.get_surface().get_height() / 3)
# gapYButton = ((pygame.display.get_surface().get_width() / 3) / 2)
print(posXButton)

start = button((0, 200, 0), posXButton, posYButton, widthButton, 80, 'Start')
score = button((0, 0, 200), posXButton, posYButton + 120, widthButton, 80, 'Score')
quit = button((200, 0, 0), posXButton, posYButton + 240, widthButton, 80, 'Quitter')

def redrawWindow():
    window.fill((255,255,255))
    start.draw(window)
    score.draw(window)
    quit.draw(window)

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
                runMap = True
            elif score.isOver(pos):
                print("Success 2")
            elif quit.isOver(pos):
                runWelcome = False
                runMap = False


    # pos = pygame.mouse.get_pos()
    # if clickable_area.collidepoint(pos):
    #     print("success")

    # window.blit(button, (300, 200))

def mapGame(idMap):
    #Environs 60 fps
    MS_PER_UPDATE = 10

    def update():
        currentMap.update()

    def renderMapWindow(ratioRender):
        drawMap(window,100,100,500,500)
        for currentMob in currentMap.mobs():
            drawMonster(window, currentMob, ratioRender)


    runMap = True
    currentMap = Map(idMap,10) #What IS dislock ?
    previousTime = time.time()
    lag = 0.0

    while runMap:
        #Permet une gestion précise de la boucle de jeu principale :
        currentTime = time.time()
        elapsed = currentTime - previousTime
        previousTime = currentTime
        lag += elapsed

        #Gestion input:
        while lag >= MS_PER_UPDATE:
            update()
            lag -= MS_PER_UPDATE

        renderMapWindow(lag/MS_PER_UPDATE)
