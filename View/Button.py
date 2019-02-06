import pygame

class button():
    def __init__(self, color, x, y, width, height):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = ''
        self.image = ''


    def draw(self, win, outline=None):
    # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.image != '':
            win.blit(self.image, (self.x + self.posXimg, self.y + self.posYimg))

        if self.text != '':
            font = pygame.font.SysFont('comicsans', self.size)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (self.x + self.posXText, self.y + self.posYText))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

    def addText(self, text, posX, posY, size):
        self.text = text
        self.size = size
        self.posXText = posX
        self.posYText = posY

    def removeText(self):
        self.text = ''

    def addImage(self, img, posX, posY, width, height):
       self.image = pygame.image.load('View/Data/' + img)
       self.image = pygame.transform.scale(self.image, (width, height))
       self.posXimg = posX
       self.posYimg = posY


    def removeImage(self):
        self.image = ''


