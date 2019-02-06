import time
from Model.Mob import *
from Model.Map import Map
from View.drawMap import *

# =========================================================================================================================================
# Boucle de jeu :
def mapGame(window, map):
    # ===================================
    # Mise en place de la musique
    song = pygame.mixer.Sound("View/Data/Song/welcome.wav")
    song.play()
    # ===================================
    # Mise en place des timers
    map.start = time.time()
    map.wave.touchMonster = time.time()
    gravTime = time.time()
    # ===================================
    # Environs 60 fps
    MS_PER_UPDATE = 0.010

    # ===================================
    # Taille des bouttons/arène
    sizeMenu = 10
    sizeMap = pygame.display.get_surface().get_height() - sizeMenu
    posXMap = (pygame.display.get_surface().get_width() / 2) - (sizeMap / 2)
    posYMap = sizeMenu
    # ===================================

    def updateAll():
        map.update(player)
        player.update(map.mobs())

    def updateChrono(map):
        min = int((map.start + 180 - time.time()) / 60)
        sec = int((map.start + 180 - time.time()) % 60)

        # Pour afficher 2:05 et non 2:5
        if len(str(sec)) == 1:
            second = '0'+str(sec)
        else:
            second = str(sec)
        
        return str(min) + ':' + second

    def renderMapWindow(ratioRender, score, map):
        window.fill((255, 255, 255))
        drawMap(window, posXMap, posYMap, sizeMap)
        for currentMob in map.mobs():
            drawMonster(window, currentMob, ratioRender)
        drawPlayer(window, player, ratioRender)
        drawRessort(window, posXMap, posYMap, sizeMap)

        player.movement(False)
        text = font.render(updateChrono(map), 1, (0, 0, 0))
        window.blit(text, (30, 30))

        text = font.render(str(score), 1, (0, 0, 0))
        window.blit(text, (1000, 30))
        pygame.display.update()

    player = Player([500, 350], 100, [40, 60], 50)

    runMap = True
    previousTime = time.time()
    lag = 0.0

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
                player.gravityShift([-player.gravitation[0], -player.gravitation[1]])

        mouseBoutton = pygame.mouse.get_pressed()
        if mouseBoutton[0]:
            player.shoot(pygame.mouse.get_pos())

        while lag >= MS_PER_UPDATE:
            updateAll()
            lag -= MS_PER_UPDATE

        score = map.getScore()
        renderMapWindow(lag/MS_PER_UPDATE, score, map)

        # Take consideration of the event :
        pygame.event.pump()

    song.stop()

# Fin de boucle de jeu
# =========================================================================================================================================
