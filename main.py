from pygame import *
from View.game import *
from View.drawMap import *
from View.Button import button
import time

pygame.init()
NBLEVEL = 10
maps = []


# =========================================================================================================================================
# Window :
window = pygame.display.set_mode((1024, 768))
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
# Input view

def inputView(finalScore):
    runInput = 1
    back = button((59, 250, 165), posXButton - 120, posYButton - 160, 500, 500)  # Background of the inputview
    print(str(finalScore))
    back.addText("Votre Score : " + str(finalScore), 20, 120, 60)
    back.draw(window)
    title= button((59, 250, 165), posXButton - 120, posYButton - 160, 500, 100)
    title.addText("PARTIE TERMINEE", 100,30,60)
    title.draw(window)

    nameRequest = button((59, 250, 165), posXButton - 120, posYButton +100, 500, 30)
    nameRequest.addText("Saisir pseudo : ", 20, 0, 60)
    nameRequest.draw(window)

    text = button((255, 255, 255), posXButton - 100, posYButton + 150, 460, 50)

    #Bouton pour validé le pseudo
    # enter = button((100,26,100), posXButton + 20, posYButton + 250, 200, 80)
    # enter.addText("Valider", 40, 20, 50)
    # enter.draw(window)

    pygame.display.flip()
    lastText = '|'
    keyPressed = time.time()
    textX = 30
    textY = 5
    textSize = 50
    text.addText(lastText, textX, textY, textSize)
    text.draw(window)
    pygame.display.flip()



    while runInput:
        keys = pygame.key.get_pressed()
        if time.time() - keyPressed > 0.09:  #change the writing speed
            keyPressed = time.time()
            if keys[pygame.K_ESCAPE]:
                runInput = False
            if keys[pygame.K_BACKSPACE] and lastText != '':
                lastText = lastText[:-2]
                lastText = lastText + '|'
                text.addText(lastText, textX, textY, textSize)
                text.draw(window)
                pygame.display.flip()
            elif keys[pygame.K_RETURN] and lastText != '|':
                level = int(a.text[6:len(a.text)])
                addScore(level, lastText, finalScore)
                runInput = False
            if len(lastText) < 9:
                if keys[pygame.K_a]:
                    lastText = lastText[:-1]
                    lastText = lastText + 'A|'
                    text.addText(lastText, textX, textY, textSize)
                    text.draw(window)
                    pygame.display.flip()
                elif keys[pygame.K_b]:
                    lastText = lastText[:-1]
                    lastText = lastText + 'B|'
                    text.addText(lastText, textX, textY, textSize)
                    text.draw(window)
                    pygame.display.flip()
                elif keys[pygame.K_c]:
                    lastText = lastText[:-1]
                    lastText = lastText + 'C|'
                    text.addText(lastText, textX, textY, textSize)
                    text.draw(window)
                    pygame.display.flip()
                elif keys[pygame.K_d]:
                    lastText = lastText[:-1]
                    lastText = lastText + 'D|'
                    text.addText(lastText, textX, textY, textSize)
                    text.draw(window)
                    pygame.display.flip()
                elif keys[pygame.K_e]:
                    lastText = lastText[:-1]
                    lastText = lastText + 'E|'
                    text.addText(lastText, textX, textY, textSize)
                    text.draw(window)
                    pygame.display.flip()
                elif keys[pygame.K_f]:
                    lastText = lastText[:-1]
                    lastText = lastText + 'F|'
                    text.addText(lastText, textX, textY, textSize)
                    text.draw(window)
                    pygame.display.flip()
                elif keys[pygame.K_g]:
                    lastText = lastText[:-1]
                    lastText = lastText + 'G|'
                    text.addText(lastText, textX, textY, textSize)
                    text.draw(window)
                    pygame.display.flip()
                elif keys[pygame.K_h]:
                    lastText = lastText[:-1]
                    lastText = lastText + 'H|'
                    text.addText(lastText, textX, textY, textSize)
                    text.draw(window)
                    pygame.display.flip()
                elif keys[pygame.K_i]:
                    lastText = lastText[:-1]
                    lastText = lastText + 'I|'
                    text.addText(lastText, textX, textY, textSize)
                    text.draw(window)
                    pygame.display.flip()
                elif keys[pygame.K_j]:
                    lastText = lastText[:-1]
                    lastText = lastText + 'J|'
                    text.addText(lastText, textX, textY, textSize)
                    text.draw(window)
                    pygame.display.flip()
                elif keys[pygame.K_k]:
                    lastText = lastText[:-1]
                    lastText = lastText + 'K|'
                    text.addText(lastText, textX, textY, textSize)
                    text.draw(window)
                    pygame.display.flip()
                elif keys[pygame.K_l]:
                    lastText = lastText[:-1]
                    lastText = lastText + 'L|'
                    text.addText(lastText, textX, textY, textSize)
                    text.draw(window)
                    pygame.display.flip()
                elif keys[pygame.K_m]:
                    lastText = lastText[:-1]
                    lastText = lastText + 'M|'
                    text.addText(lastText, textX, textY, textSize)
                    text.draw(window)
                    pygame.display.flip()
                elif keys[pygame.K_n]:
                    lastText = lastText[:-1]
                    lastText = lastText + 'N|'
                    text.addText(lastText, textX, textY, textSize)
                    text.draw(window)
                    pygame.display.flip()
                elif keys[pygame.K_o]:
                    lastText = lastText[:-1]
                    lastText = lastText + 'O|'
                    text.addText(lastText, textX, textY, textSize)
                    text.draw(window)
                    pygame.display.flip()
                elif keys[pygame.K_p]:
                    lastText = lastText[:-1]
                    lastText = lastText + 'P|'
                    text.addText(lastText, textX, textY, textSize)
                    text.draw(window)
                    pygame.display.flip()
                elif keys[pygame.K_q]:
                    lastText = lastText[:-1]
                    lastText = lastText + 'Q|'
                    text.addText(lastText, textX, textY, textSize)
                    text.draw(window)
                    pygame.display.flip()
                elif keys[pygame.K_r]:
                    lastText = lastText[:-1]
                    lastText = lastText + 'R|'
                    text.addText(lastText, textX, textY, textSize)
                    text.draw(window)
                    pygame.display.flip()
                elif keys[pygame.K_s]:
                    lastText = lastText[:-1]
                    lastText = lastText + 'S|'
                    text.addText(lastText, textX, textY, textSize)
                    text.draw(window)
                    pygame.display.flip()
                elif keys[pygame.K_t]:
                    lastText = lastText[:-1]
                    lastText = lastText + 'T|'
                    text.addText(lastText, textX, textY, textSize)
                    text.draw(window)
                    pygame.display.flip()
                elif keys[pygame.K_u]:
                    lastText = lastText[:-1]
                    lastText = lastText + 'U|'
                    text.addText(lastText, textX, textY, textSize)
                    text.draw(window)
                    pygame.display.flip()
                elif keys[pygame.K_v]:
                    lastText = lastText[:-1]
                    lastText = lastText + 'V|'
                    text.addText(lastText, textX, textY, textSize)
                    text.draw(window)
                    pygame.display.flip()
                elif keys[pygame.K_w]:
                    lastText = lastText[:-1]
                    lastText = lastText + 'W|'
                    text.addText(lastText, textX, textY, textSize)
                    text.draw(window)
                    pygame.display.flip()
                elif keys[pygame.K_x]:
                    lastText = lastText[:-1]
                    lastText = lastText + 'X|'
                    text.addText(lastText, textX, textY, textSize)
                    text.draw(window)
                    pygame.display.flip()
                elif keys[pygame.K_y]:
                    lastText = lastText[:-1]
                    lastText = lastText + 'Y|'
                    text.addText(lastText, textX, textY, textSize)
                    text.draw(window)
                    pygame.display.flip()
                elif keys[pygame.K_z]:
                    lastText = lastText[:-1]
                    lastText = lastText + 'Z|'
                    text.addText(lastText, textX, textY, textSize)
                    text.draw(window)
                    pygame.display.flip()



            # Take consideration of the event :
            pygame.event.pump()
# End Input View
# =========================================================================================================================================

# =========================================================================================================================================
# Score View
def scoreView():
    runScore = True
    levelSelect = 1
    back = button((59, 250, 165), 0, 0, 1024, 768)  # Background of the Scoreview
    arenaNameDisplay = button((59, 250, 165), 0, 0, 300, 100)  # Background of the Scoreview

    quit = button((200, 0, 0), posXButton + 350, posYButton + 400, widthButton, 80)

    arenaScore = []
    for map in maps:
        i = map.level
        if i < 6:
            ba = button((0, 0, 200), (posXButton - 360), (posYButton-200) + (i * 85), 160, 70)
            arenaScore.append(ba)
        else:
            ba = button((0, 0, 200), (posXButton - 170), (posYButton - 200) + ((i-5)* 85), 160, 70)
            arenaScore.append(ba)


    def reDrawScoreView(levelSelect):
        i = 1
        back.draw(window)
        for are in arenaScore:
            arenaNameScore = "Arène " + str(i)
            are.addText(arenaNameScore, 20, 20, 40)
            are.draw(window)
            i += 1
        quit.addText('Retour', 60, 20, 60)
        quit.draw(window)
        arenaNameDisplay.addText("Arène " + str(levelSelect), 20, 120, 60)
        arenaNameDisplay.draw(window)
        pygame.display.flip()

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
                        print(are.text)
                        print(levelSelect)
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

# Affichage de la fenêtre
def redrawWindow():
    window.fill((255, 255, 255))
    start.draw(window)
    start.addText("Tacos Mania", 10, 10, 60)

    i = 0
    for a in arena:
        arenaName = "Arène " + str(i+1)
        a.draw(window)
        a.addText(arenaName, 30, 150, 40)

        if i < 6:
            if not maps[i].dislock:
                a.addImage('cadenas.png', 10, 10, 50, 50)
        else:
            if not maps[i].dislock:
                a.addImage('cadenas.png', 10, 10, 50, 50)

        i += 1

    credit.draw(window)
    credit.addText('Credit', 60, 20, 60)
    score.draw(window)
    score.addText('Score', 60, 20, 60)
    quit.draw(window)
    quit.addText('Quitter', 50, 20, 60)
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
            if score.isOver(pos):
                scoreView()
            elif quit.isOver(pos):
                runWelcome = False
            else:
                for a in arena:
                    if a.isOver(pos):
                        window.fill((255, 255, 255))
                        level = int(a.text[6:len(a.text)])
                        if maps[level-1].dislock:
                            pygame.mixer.pause()
                            mapGame(window, maps[level-1], a)
                            finalScore = maps[level-1].getScore()
                            inputView(finalScore)
                            pygame.mixer.unpause()


# End welcome view
# =========================================================================================================================================


song.stop()
pygame.quit()
