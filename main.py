from pygame import *
from View.game import *
from View.drawMap import *
from View.Button import button
import time

pygame.init()
FOND = pygame.image.load('View/Data/option/fond.png')
NBLEVEL = 10
maps = []

# =========================================================================================================================================
# Window :
window = pygame.display.set_mode((1024, 700))
pygame.display.set_caption("Tacos Mania")
window.fill((255, 255, 255))

# ===================================
# Mise en place de la musique
song = pygame.mixer.Sound("View/Data/Song/RainingTacos.wav")
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
# Score View
def scoreView():
    runScore = True
    levelSelect = 1

    back = button((59, 250, 165), 0, 0, 1024, 768)  # Background of the Scoreview
    back.addImage("Option/fond.png", 0, 0, 1024, 768)
    back.draw(window)
    tab = button((10, 10, 10), posXButton-350, posYButton-190, 450, 700)
    arenaNameDisplay = button((59, 250, 165), 150, -100, 310, 100)

    quit = button((200, 0, 0), posXButton + 350, posYButton + 400, 250, 80)

    arenaScore = []
    for map in maps:
        i = map.level
        if i < 6:
            ba = button((0, 0, 200), (posXButton + 260), (posYButton-200) + (i * 85), 160, 70)
            arenaScore.append(ba)
        else:
            ba = button((0, 0, 200), (posXButton + 440), (posYButton - 200) + ((i-5)* 85), 160, 70)
            arenaScore.append(ba)

    playerTab = []
    scoreTab = []
    for k in range(0,10):
        playerName = button((10,50,100), posXButton - 340, posYButton - 180+(k * 70), 210, 50)
        playerTab.append(playerName)
        playerScore = button((10, 50, 100), posXButton - 120, posYButton - 180 + (k * 70), 210, 50)
        scoreTab.append(playerScore)

    def reDrawScoreView(levelSelect):
        i = 1
        back.draw(window)
        tab.draw(window)
        for are in arenaScore:
            arenaNameScore = "Arène " + str(i)
            are.addImage("Buttons/notPress.png", 0, 0, 160, 70)
            are.addText(arenaNameScore, 35, 15, 30)
            are.draw(window)
            i += 1
        res = getScoreSorted(levelSelect)
        i = 0
        for play in playerTab:
            play.addText(str(i+1) + " : " + res[i][0], 5, 10, 30)
            play.draw(window)
            i += 1
        i = 0
        for playScore in scoreTab:
            playScore.addText(str(res[i][1]), 5, 10, 30)
            playScore.draw(window)
            i += 1

        quit.addText('Retour', 60, 10, 50)
        quit.addImage("Buttons/notPress.png", 0, 0, 250, 80)
        quit.draw(window)

        arenaNameDisplay.addText("Arène " + str(levelSelect), 20, 100, 55)
        arenaNameDisplay.draw(window)
        pygame.display.flip()

        posi = pygame.mouse.get_pos()
        for aren in arenaScore:
            if aren.isOver(posi):
                aren.addImage("Buttons/press.png", 0, 0, 160, 70)
                aren.draw(window)
                pygame.display.flip()
        if quit.isOver(posi):
            quit.addImage("Buttons/press.png", 0, 0, 250, 80)
            quit.draw(window)
            pygame.display.flip()
        # Take consideration of the event :
        pygame.event.pump()

    reDrawScoreView(levelSelect)

    while runScore:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            runScore = False

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if quit.isOver(pos):
                    runScore = False
                for are in arenaScore:
                    if are.isOver(pos):
                        window.fill((255, 255, 255))
                        levelSelect = int(are.text[6:len(are.text)])
                        reDrawScoreView(levelSelect)
        reDrawScoreView(levelSelect)



        # Take consideration of the event :
        pygame.event.pump()

#End Score View
# =========================================================================================================================================

# =========================================================================================================================================
# Welcome View
widthButton = 250
posXButton = (pygame.display.get_surface().get_width() / 2) - ((1/2) * widthButton)
posYButton = (pygame.display.get_surface().get_height() / 3)

# Buttons on the top
start = button((0, 200, 0), posXButton, posYButton - 200, 300, 80) # To delete one day

# Buttons on the middle
arena = []
widthButton = 170
heightButton = 190
for map in maps:
    i = map.level
    if i < 6:
        b = button((0, 0, 200), (posXButton - 360) + (i-1)*200, posYButton-80, widthButton, heightButton)
        arena.append(b)
    else:
        b = button((0, 0, 200), (posXButton - 360) + (i-6)*200, posYButton + 150, widthButton, heightButton)
        arena.append(b)

# Buttons on the bottom
widthButton = 250
credit = button((0, 0, 200), posXButton - 350, posYButton + 400, widthButton, 80)
score = button((0, 0, 200), posXButton, posYButton + 400, widthButton, 80)
quit = button((200, 0, 0), posXButton + 350, posYButton + 400, widthButton, 80)

# Button help
help = button((0, 0, 200), 950, 10, 50, 50)

# Affichage de la fenêtre
def redrawWindow():
    window.fill((255, 255, 255))
    image = pygame.transform.scale(FOND, (1024, 768))
    window.blit(image, (0, 0))
    start.draw(window)
    start.addText("Tacos Mania", 10, 10, 50)

    i = 0
    for a in arena:
        arenaName = "Arène " + str(i+1)
        a.draw(window)
        a.addText(arenaName, 40, 130, 30)

        if i < 6:
            if not maps[i].dislock:
                a.addImage('Buttons/arenaLock.png', 0, 0, 170, 190)
            else:
                a.addImage('Buttons/arenaNotPress.png', 0, 0, 170, 190)
        else:
            if not maps[i].dislock:
                a.addImage('Buttons/arenaLock.png', 0, 0, 170, 190)
            else:
                a.addImage('Buttons/arenaNotPress.png', 0, 0, 170, 190)
        i += 1

    credit.draw(window)
    credit.addImage("Buttons/notPress.png", 0, 0, 250,80)
    credit.addText('Credit', 65, 10, 45)
    score.draw(window)
    score.addImage("Buttons/notPress.png", 0, 0, 250, 80)
    score.addText('Score', 65, 10, 45)
    quit.draw(window)
    quit.addImage("Buttons/notPress.png", 0, 0, 250, 80)
    quit.addText('Quitter', 55, 10, 45)
    help.draw(window)
    help.addImage('help.jpg', 0, 0, help.width, help.height)
# =========================================================================================================================================
    #Buttons over
    pos = pygame.mouse.get_pos()
    if score.isOver(pos):
        score.addImage("Buttons/press.png", 0, 0, 250, 80)
    elif credit.isOver(pos):
        credit.addImage("Buttons/press.png", 0, 0, 250, 80)
    elif quit.isOver(pos):
        quit.addImage("Buttons/press.png", 0, 0, 250, 80)

def viewHelp():
    image = pygame.image.load('View/Data/Option/Comment_jouer.png')
    image = pygame.transform.scale(image, (1024, 768))
    window.blit(image, (0, 0))
    pygame.display.update()

    runHelp = True
    while runHelp:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):  # If you click on the window's cross
                runHelp = False

def creditView():
    image = pygame.image.load('View/Data/Option/Credits.png')
    image = pygame.transform.scale(image, (1024, 768))
    window.blit(image, (0, 0))
    pygame.display.update()

    runHelp = True
    while runHelp:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):  # If you click on the window's cross
                runHelp = False

runWelcome = True

while runWelcome:
    redrawWindow()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT: # If you click on the window's cross
            quit.addImage("Buttons/press.png", 0, 0, 250, 80)
            runWelcome = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if score.isOver(pos):
                scoreView()
            elif credit.isOver(pos):
                creditView()
            elif quit.isOver(pos):
                runWelcome = False
            elif help.isOver(pos):
                viewHelp()
            else:
                for a in arena:
                    if a.isOver(pos):
                        window.fill((255, 255, 255))
                        level = int(a.text[6:len(a.text)])
                        if maps[level-1].dislock:
                            pygame.mixer.pause()
                            mapGame(window, maps[level-1], a)
                            finalScore = maps[level-1].getScore()

# End welcome view
# =========================================================================================================================================


song.stop()
pygame.quit()
