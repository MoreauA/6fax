from pygame import *
from View.game import *
from View.drawMap import *
from View.Button import button

pygame.init()
NBLEVEL = 10
maps = []

# =========================================================================================================================================
# Window :
window = pygame.display.set_mode((1024, 500))
pygame.display.set_caption("Tacos Mania")
window.fill((255, 255, 255))

# ===================================
# Mise en place de la musique
song = pygame.mixer.Sound("View/Data/RainingTacos.wav")
song.play(loops=4)
song.set_volume(0.4)

# ===================================
# Taille des bouttons/arène
sizeMenu = 10
sizeMap = pygame.display.get_surface().get_height() - sizeMenu
posXMap = (pygame.display.get_surface().get_width() / 2) - (sizeMap / 2)
posYMap = sizeMenu

# 20 est la valeur de l'épaisseur des murs :
setCollider((posXMap+20), (posXMap+sizeMap-20), (posYMap+20), (posYMap+sizeMap-20))

# ===================================
# Création des maps
# La 1ere map est déverrouillée
map = Map(1, True)
maps.append(map)

for i in range(1, NBLEVEL):
    map = Map(i+1, False)
    maps.append(map)
# ==================================

# =========================================================================================================================================
# Welcome View
widthButton = 250
posXButton = (pygame.display.get_surface().get_width() / 2) - ((1/2) * widthButton)
posYButton = (pygame.display.get_surface().get_height() / 3)

# Buttons on the top
start = button((0, 200, 0), posXButton, posYButton - 200, 300, 80) # To delete one day

# Buttons on the middle
arena = []
widthButton = 150
for map in maps:
    i = map.level
    if i < 6:
        b = button((0, 0, 200), (posXButton - 350) + (i-1)*200, posYButton, widthButton, 140)
        arena.append(b)
    else:
        b = button((0, 0, 200), (posXButton - 350) + (i-6)*200, posYButton + 200, widthButton, 140)
        arena.append(b)

# Buttons on the bottom
widthButton = 250
boutique = button((0, 0, 200), posXButton - 350, posYButton + 400, widthButton, 80)
score = button((0, 0, 200), posXButton, posYButton + 400, widthButton, 80)
quit = button((200, 0, 0), posXButton + 350, posYButton + 400, widthButton, 80)
# =========================================================================================================================================
# Affichage de la fenêtre
def redrawWindow():
    window.fill((255, 255, 255))
    start.draw(window)
    start.addText("Tacos Mania", 10, 10, 60)

    i = 0
    for a in arena:
        arenaName = "Arène " + str(i+1)
        a.draw(window)
        a.addText(arenaName, 10, 100, 40)

        if i < 6:
            if not maps[i].dislock:
                a.addImage('cadenas.png', 10, 10, 20, 20)
        else:
            if not maps[i].dislock:
                a.addImage('cadenas.png', 10, 10, 20, 20)

        i += 1

    boutique.draw(window)
    boutique.addText('Boutique', 20, 20, 60)
    score.draw(window)
    score.addText('Score', 20, 20, 60)
    quit.draw(window)
    quit.addText('Quitter', 20, 20, 60)
# =========================================================================================================================================

runWelcome = True

while runWelcome:
    redrawWindow()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT: # If you click on the window's cross
            runWelcome = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if start.isOver(pos):
                window.fill((255, 255, 255))
                mapGame(window, maps[0])
                runWelcome = False
            elif score.isOver(pos):
                print("Success 2")
            elif quit.isOver(pos):
                runWelcome = False
            else:
                for a in arena:
                    if a.isOver(pos):
                        window.fill((255, 255, 255))
                        level = int(a.text[6:len(a.text)])
                        if maps[level-1].dislock:
                            pygame.mixer.pause()
                            mapGame(window, maps[level-1])
                            pygame.mixer.unpause()


# End welcome view
# =========================================================================================================================================
song.stop()
pygame.quit()
