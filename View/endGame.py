import time
from View.Button import *
from Model.Score import *

# =========================================================================================================================================
# Input view
def inputView(window, finalScore, level):
    widthButton = 250
    posXButton = (pygame.display.get_surface().get_width() / 2) - ((1 / 2) * widthButton)
    posYButton = (pygame.display.get_surface().get_height() / 3)

    runInput = 1
    back = button((59, 250, 165), posXButton - 120, posYButton - 160, 500, 500)  # Background of the inputview
    print(str(finalScore))
    back.addText("Votre Score : " + str(finalScore), 20, 120, 60)
    back.draw(window)
    title= button((59, 250, 165), posXButton-100, posYButton - 160, 200, 100)
    title.addText("PARTIE TERMINEE", 0,30,60)
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
                addScore(level,lastText, finalScore)
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
