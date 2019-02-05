def drawMap(window,x,y,width,height):
    pass

def drawMonster(window,monster,ratio):

    posX = monster.pos[0]
    posY = monster.pos[1]

    if monster.isMoving():
        posX += monster.speed[0] * ratio
        posY += monster.speed[1] * ratio

    #ICI on peut draw le monster à la position indiquer :
