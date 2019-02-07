import time
from Model.Mob import *
from Model.Map import Map
from View.drawMap import *
from Model.Score import *
from View.endGame import *

# =========================================================================================================================================
# Boucle de jeu :
def mapGame(window, map):
    song = pygame.mixer.Sound("View/Data/Song/welcome.wav")
    song.play()

    map.start = time.time()

    # Environs 60 fps
    MS_PER_UPDATE = 0.010

    sizeMenu = 10
    sizeMap = pygame.display.get_surface().get_height() - sizeMenu
    posXMap = (pygame.display.get_surface().get_width() / 2) - (sizeMap / 2)
    posYMap = sizeMenu

    gravTime = time.time()


    def updateAll():
        map.update(player)
        return player.update(map.mobs())

    def updateChrono(map):
        min = int((map.start + 180 - time.time()) / 60)
        sec = int((map.start + 180 - time.time()) % 60)

        if len(str(sec)) == 1:
            return str(min) + ':0' + str(sec)
        else:
            return str(min) + ':' + str(sec)

    def renderMapWindow(ratioRender, score, map, ressortState):
        window.fill((255, 255, 255))
        drawMap(window, posXMap, posYMap, sizeMap)
        for currentMob in map.mobs():
            drawMonster(window, currentMob, ratioRender)
        # pygame.display.flip()
        drawPlayer(window, player, ratioRender)
        drawRessort(window, posXMap, posYMap, sizeMap, ressortState)

        player.movement(False)
        text = font.render(updateChrono(map), 1, (0, 0, 0))
        window.blit(text, (30, 30))

        #score
        text = font.render("Score :", 1, (0, 0, 0))
        window.blit(text, (920, 30))
        text = font.render(str(score), 1, (0, 0, 0))
        window.blit(text, (990, 30))

        #top 5
        text = font.render("Top 5 :", 1, (0, 0, 0))
        window.blit(text, (920, 100))
        data = getScoreSorted()
        for j in range(0,5):
            text = font.render(str(j+1)+' : ', 1, (0,0,0))
            window.blit(text, (895, 150 + (j * 50)))
            text = font.render(data[j][0], 1, (0, 0, 0))
            window.blit(text, (915, 150 + (j * 50)))
            text = font.render(str(data[j][1]), 1, (0, 0, 0))
            window.blit(text, (925, 170 + (j * 50)))

        pygame.display.update()


    player = Player([500, 350], 100, [70, 80], 50)

    runMap = True
    #currentMap = Map(idMap, 10) #What IS dislock ?
    previousTime = time.time()
    lag = 0.0
    actRessort = 0
    loadTime = 0.0
    ressortCharger = 0

    font = pygame.font.Font(None, 24)
    # text = font.render(updateChrono(map), 1, (0, 0, 0))

    while runMap and map.running():

        # Permet une gestion précise de la boucle de jeu principale :
        currentTime = time.time()
        elapsed = currentTime - previousTime
        previousTime = currentTime
        lag += elapsed

        #Gestion input:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            runMap = False

        if keys[pygame.K_z] or keys[pygame.K_w]:
            player.move([0, -1])
            player.movement(True)
            player.left = False
            player.right = False

        if keys[pygame.K_d]:
            player.move([1, 0])
            player.movement(True)
            if not player.airTime:
                player.left = False
                player.right = True
        elif keys[pygame.K_q] or keys[pygame.K_a]:
            player.move([-1, 0])
            player.movement(True)
            if not player.airTime:
                player.left = True
                player.right = False
        else:
            player.movement(False)
            player.left = False
            player.right = False

        if keys[pygame.K_s]:
            player.move([0, 1])
            player.movement(True)
            player.left = False
            player.right = False

        if keys[pygame.K_SPACE]:
            currentT = time.time()
            if currentT - gravTime >= 0.5:
                gravTime = currentT
                player.gravityShift([-player.gravitation[0], -player.gravitation[1]])
                player.right = False
                player.left = False
                player.airTime = True

        mouseBoutton = pygame.mouse.get_pressed()
        if mouseBoutton[0]:
            player.shoot(pygame.mouse.get_pos())

        while lag >= MS_PER_UPDATE:
            actRessort = updateAll()
            if actRessort != 0:
                if time.time() - loadTime > 0.1:
                    loadTime = time.time()
                    ressortCharger = actRessort
            # text = font.render(updateChrono(map), 1, (0, 0, 0))
            lag -= MS_PER_UPDATE

        if time.time() - loadTime > 0.1:
            ressortCharger = 0

        score = map.getScore()
        renderMapWindow(lag/MS_PER_UPDATE, score, map, ressortCharger)

        # Take consideration of the event :
        pygame.event.pump()


        # pygame.display.flip()

    if not map.running():
        finalScore = map.getScore()
        inputView(window, finalScore)
        pygame.mixer.unpause()

    song.stop()

# Fin de boucle de jeu

# =========================================================================================================================================
