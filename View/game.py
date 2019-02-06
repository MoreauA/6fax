import time
from Model.Mob import *
from Model.Map import Map
from View.drawMap import *

def updateChrono(map):
    min = int((map.start + 180 - time.time()) / 60)
    sec = int((map.start + 180 - time.time()) % 60)

    return str(min) + ':' + str(sec)

   # text = font.render(str(min) + ':' + str(sec), 1, (0, 0, 0))
    #window.blit(text, (20, 20))
   # pygame.display.flip()

# =========================================================================================================================================
# Boucle de jeu :
def mapGame(window, map):
    son = pygame.mixer.Sound("View/Data/welcome.wav")
    son.play()

    map.start = time.time()

    # Environs 60 fps
    MS_PER_UPDATE = 10

    sizeMenu = 10
    sizeMap = pygame.display.get_surface().get_height() - sizeMenu
    posXMap = (pygame.display.get_surface().get_width() / 2) - (sizeMap / 2)
    posYMap = sizeMenu

    gravTime = time.time()

    def updateAll():
        map.update()
        player.update()

    def renderMapWindow(ratioRender):
        window.fill((255, 255, 255))
        drawMap(window, posXMap, posYMap, sizeMap)
        for currentMob in map.mobs():
            drawMonster(window, currentMob, ratioRender)
        # pygame.display.flip()
        drawPlayer(window, player, ratioRender)
        player.movement(False)
        pygame.display.update()

    player = Player([500, 350], 100, [40,40], 50)

    runMap = True
    #currentMap = Map(idMap, 10) #What IS dislock ?
    previousTime = time.time()
    lag = 0.0

    chrono = int(time.time())
    texte = updateChrono(map)
    font = pygame.font.Font(None, 24)
    text = font.render(texte, 1, (0, 0, 0))

    while runMap and map.running():

        if int(time.time()) - chrono > 0.5:
            texte = updateChrono(map)
            font = pygame.font.Font(None, 24)
            text = font.render(texte, 1, (0, 0, 0))
            chrono = int(time.time())

        # Permet une gestion précise de la boucle de jeu principale :
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

        mouseBoutton = pygame.mouse.get_pressed()
        if mouseBoutton[0]:
            player.shoot(pygame.mouse.get_pos())

        updateAll()
        while lag >= MS_PER_UPDATE:
            updateAll()
            lag -= MS_PER_UPDATE

        renderMapWindow(lag/MS_PER_UPDATE)
        # Take consideration of the event :
        pygame.event.pump()
        window.blit(text, (20, 20))
        pygame.display.flip()


# Fin de boucle de jeu
# =========================================================================================================================================
