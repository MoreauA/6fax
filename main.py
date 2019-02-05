from pygame import *
from View.game import *
from View.drawMap import *
from View.Button import button

pygame.init()
NBLEVEL = 10
maps = []

# =========================================================================================================================================
# Window :
window = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Tacos Mania")
window.fill((255, 255, 255))
runWelcome = True

# Création des maps
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
                       mapGame(window, int(b.text))
                       runChooseMap = False

# =========================================================================================================================================
# Welcome View
widthButton = 250
posXButton = (pygame.display.get_surface().get_width() / 2) - ((1/2) * widthButton)
posYButton = (pygame.display.get_surface().get_height() / 3)

# Buttons on the top
start = button((0, 200, 0), posXButton, posYButton - 200, widthButton, 80, '', 'Tacos Mania') # To delete one day

# Buttons on the middle
arena = []
widthButton = 150
for i in range(0, 10):
    arenaName = "Arène " + str(i+1)
    if i < 5:
        arena.append(button((0, 0, 200), (posXButton - 350) + i*200, posYButton, widthButton, 80, True, arenaName))
    else:
        arena.append(button((0, 0, 200), (posXButton - 350) + (i-5)*200, posYButton + 200, widthButton, 80, True, arenaName))

# Buttons on the bottom
widthButton = 250
boutique = button((0, 0, 200), posXButton - 350, posYButton + 400, widthButton, 80, False, 'Boutique')
score = button((0, 0, 200), posXButton, posYButton + 400, widthButton, 80, False, 'Score')
quit = button((200, 0, 0), posXButton + 350, posYButton + 400, widthButton, 80, False, 'Quitter')

def redrawWindow():
    window.fill((255, 255, 255))
    start.draw(window)

    for val in range(0, 10):
        arena[val].draw(window)
        arena[val].addImmage(window, 'cadenas.png', 0, 0, 50, 50)
    arena[1].removeImage()
    boutique.draw(window)
    score.draw(window)
    quit.draw(window)
    # window.blit(imgAubergine, (10, 20))

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
                mapGame(window, 1)
                # chooseMaps()
                runWelcome = False
            elif score.isOver(pos):
                print("Success 2")
            elif quit.isOver(pos):
                runWelcome = False

# End welcome view
# =========================================================================================================================================

pygame.quit()
