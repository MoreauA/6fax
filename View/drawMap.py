import pygame

def drawMap(window,x,y,width):
    pygame.draw.rect(window, (255, 0, 0), pygame.Rect(x, y, width, 20))
    pygame.draw.rect(window, (255, 0, 0), pygame.Rect(x, y, 20, width))
    pygame.draw.rect(window, (255, 0, 0), pygame.Rect(x, (y + width - 20), width, 20))
    pygame.draw.rect(window, (255, 0, 0), pygame.Rect((x + width - 20), y, 20, width))
    pass

def drawMonster(window,monster,ratio):

    posX = monster.pos[0]
    posY = monster.pos[1]
    width = monster.size[0]

    if monster.isMoving():
        posX += monster.speed[0] * ratio
        posY += monster.speed[1] * ratio

    #ICI on peut draw le monster à la position indiquer :
    pygame.draw.rect(window, (0, 0, 150), pygame.Rect(posX, posY, width, width))

def drawPlayer(window,player,ratio):

    for shot in player.shots:
        shotX = int(shot.pos[0] + (shot.speed[0]*ratio))
        shotY = int(shot.pos[1] + (shot.speed[1]*ratio))
        pygame.draw.circle(window, (0, 0, 0), (shotX, shotY), shot.size[0])

    posX = player.pos[0]
    posY = player.pos[1]
    width = player.size[0]

    if player.isMoving():
        posX += player.speed[0] * ratio
        posY += player.speed[1] * ratio

    pygame.draw.rect(window, (0, 150, 0), pygame.Rect(posX, posY, width, width))

def drawRessort(window, x, y, size):
    image = pygame.image.load('View/Data/ressort.png')
    image = pygame.transform.scale(image, (20, 20))
    image = pygame.transform.rotate(image, 45)

    # -50 pour taille des cube de l'arène (20)
    #           - taille image (20)
    #           - moitié taille image (10)
    window.blit(image, (x + size - 50, y + 20))
    window.blit(image, (x + 20, y + size - 50))

    image = pygame.transform.rotate(image, 90)
    window.blit(image, (x + 20, y + 20))
    window.blit(image, (x + size - 50, y + size - 50))

