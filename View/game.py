from Model.Mob import *
from View.drawMap import *
from View.endGame import *

# =========================================================================================================================================
# Boucle de jeu :

FOND_MAP = pygame.transform.scale(pygame.image.load('View/Data/Map/Fond_Map.png'), (718, 718))
CADRE_MAP = pygame.transform.scale(pygame.image.load('View/Data/Map/lecadre.png'), (758, 770))

def mapGame(window, maps, level):

    global FOND_MAP
    FOND_MAP = FOND_MAP.convert()

    global CADRE_MAP
    CADRE_MAP = CADRE_MAP.convert_alpha()

    song = pygame.mixer.Sound("View/Data/Song/welcome.wav")
    song.set_volume(0.3)
    song.play()

    gun = pygame.mixer.Sound("View/Data/Song/gun.wav")
    gun.set_volume(0.04)

    map = maps[level]

    map.start = time.time()
    map.wave = Wave(map.level, 1)
    map.score = 0

    # Environs 60 fps
    MS_PER_UPDATE = 0.010

    sizeMenu = 10
    sizeMap = pygame.display.get_surface().get_height() - sizeMenu
    posXMap = (pygame.display.get_surface().get_width() / 2) - (sizeMap / 2)
    posYMap = sizeMenu

    gravTime = time.time()

    def updateAll():
        player.precPos = [player.pos[0], player.pos[1]]
        map.update(player, map.listPlatform)
        return player.update(map.mobs(), map.listPlatform)

    def updateChrono(map):
        min = int((map.start + 180 - time.time()) / 60)
        sec = int((map.start + 180 - time.time()) % 60)

        if len(str(sec)) == 1:
            return str(min) + ':0' + str(sec)
        else:
            return str(min) + ':' + str(sec)

    def renderMapWindow(ratioRender, score, map, ressortState):
        pygame.draw.rect(window, (22, 24, 37), Rect(0, 0, 1024, 768))

        window.blit(FOND_MAP, (posXMap + 20, posYMap + 20))
        window.blit(CADRE_MAP, (posXMap, posYMap))

        drawPlatForm(window, map.listPlatform)

        for currentMob in map.mobs():
            drawMonster(window, currentMob, ratioRender)

        drawBufs(window, map)
        drawPlayer(window, player, ratioRender)
        drawRessort(window, posXMap, posYMap, sizeMap, ressortState)

        drawMap(window, posXMap, posYMap, sizeMap)

        player.movement(False)
        font = pygame.font.Font('View/Data/Font/Schoolbell-Regular.ttf', 30)
        text = font.render(updateChrono(map), 1, (255, 255, 255))
        window.blit(text, (30, 30))

        #score
        text = font.render("Score", 1, (255, 255, 255))
        window.blit(text, (930, 30))
        text = font.render(str(score), 1, ((0, 200, 0) if score>0 else (255, 0, 0)))
        window.blit(text, (920, 70))

        #vague
        text = font.render("Vague", 1, (255, 255, 255))
        window.blit(text, (930, 130))
        text = font.render(str(map.wave.num), 1, (150, 0, 0))
        window.blit(text, (920, 170))

        pygame.display.update()

    player = Player([500, 350], [70, 80], 50)

    runMap = True
    previousTime = time.time()
    lag = 0.0
    loadTime = 0.0
    ressortCharger = 0

    font = pygame.font.Font(None, 24)

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
            if not player.airTime:
                if player.wall == 2 or player.wall == 4:
                    player.right = False
                    player.left = True
                else :
                    player.left = False
                    player.right = False
        elif keys[pygame.K_s]:
            player.move([0, 1])
            player.movement(True)
            if not player.airTime:
                if player.wall == 2 or player.wall == 4:
                    player.right = True
                    player.left = False
                else:
                    player.left = False
                    player.right = False
        elif player.wall == 2 or player.wall == 4:
            player.movement(False)
            player.left = False
            player.right = False

        if keys[pygame.K_d]:
            player.move([1, 0])
            player.movement(True)
            if not player.airTime:
                if player.wall == 1 or player.wall == 3:
                    player.right = True
                    player.left = False
                else:
                    player.left = False
                    player.right = False
        elif keys[pygame.K_q] or keys[pygame.K_a]:
            player.move([-1, 0])
            player.movement(True)
            if not player.airTime:
                if player.wall == 1 or player.wall == 3:
                    player.right = False
                    player.left = True
                else:
                    player.left = False
                    player.right = False
        elif player.wall == 1 or player.wall == 3:
            player.movement(False)
            player.left = False
            player.right = False

        if keys[pygame.K_SPACE]:
            currentT = time.time()
            if currentT - gravTime >= 0.5 and not player.airTime:
                gravTime = currentT
                player.gravityShift([-player.gravitation[0], -player.gravitation[1]])
                player.right = False
                player.left = False
                player.airTime = True

        for event in pygame.event.get():
            if event.type == QUIT:  # If you click on the window's cross
                runMap = False

        mouseBoutton = pygame.mouse.get_pressed()
        if mouseBoutton[0]:
            gun.play()
            player.shoot(pygame.mouse.get_pos())

        while lag >= MS_PER_UPDATE:
            actRessort = updateAll()
            if actRessort != 0:
                if time.time() - loadTime > 0.1:
                    loadTime = time.time()
                    ressortCharger = actRessort
            lag -= MS_PER_UPDATE

        if time.time() - loadTime > 0.1:
            ressortCharger = 0

        score = map.getScore()
        renderMapWindow(lag/MS_PER_UPDATE, score, map, ressortCharger)

        # Take consideration of the event :
        pygame.event.pump()

    if not map.running():
        finalScore = map.getScore()

        if finalScore <= 0:
            end = pygame.mixer.Sound("View/Data/Song/loose.wav")
        elif finalScore >= 100:
            end = pygame.mixer.Sound("View/Data/Song/dislock.wav")
            end.set_volume(0.4)

        if finalScore <= 0 or finalScore >= 100:
            song.stop()
            end.play()

        inputView(window, finalScore, maps[level + 1])
        if finalScore >= 100:
            maps[level+1].dislock = True
            updateMapState(level+2, 1)

        if finalScore <= 0 or finalScore >= 100:
            end.stop()

        end.stop()

    song.stop()

# Fin de boucle de jeu

# =========================================================================================================================================
