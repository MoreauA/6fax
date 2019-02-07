import time
from Model.Wave import Wave
from Model.Element import Element

class Map:

    def __init__(self, level, dislock):
        self.level = level
        self.dislock = dislock
        self.score = 0

        self.start = time.time()
        self.wave = Wave(level, 1)

        self.elements = []
        self.createElement()

    def running(self):
        return self.start+180 - time.time() > 0

    def waveFinished(self):
        return self.wave.finished()

    def createElement(self):
        nbElement = 0

        if self.level <= 2:
            nbElement = 5
        elif self.level <= 4:
            nbElement = 4
        elif self.level <= 8:
            nbElement = 3

        for i in range(nbElement):
            self.elements.append(Element("tacos"))


    def updateElements(self):
        elementsTmp = self.elements

        for i in range(1, len(self.elements)):
            element = self.elements[i-1]

            if element.timeAppared is none and element.timePop < self.timeActual():
                # l'élement n'est pas apparue et le temps où il doit apparaître est dépassé
                # apparition de l'élement
                element.timeAppared = self.timeActual()
            elif element.timeAppared is not none and element.timeAppared+5 < self.timeActual():
                # l'élement est apparu depuis plus de 5 secondes
                # disparition de l'élement
                elementsTmp.remove(element)

        self.elements = elementsTmp

    def timeActual(self):
        return time.time()-self.start

    def mobs(self):
        return self.wave.getMonsters()

    def update(self, player):
        for currentMonster in self.wave.getMonsters():
            if currentMonster.value == 10:
                if currentMonster.update(player):
                    self.score -= 10
            else:
                currentMonster.update()
        if self.wave.finished():
            self.score += self.wave.score
            num = self.wave.num + 1
            self.wave = Wave(self.level, num)
            self.wave.touchMonster = time.time()
        self.wave.updateMonsters(player)

    def getScore(self):
        return self.wave.score + self.score

    # def initPlatForm(self):
    #     platForm = []
    #     platForm.append(Platform((350, 90), (90, 30)))
    #     platForm.append(Platform((100, 270), (90, 30)))
    #     platForm.append(Platform((300, 450), (90, 30)))
    #     platForm.append(Platform((390, 400), (30, 90)))
    #     return platForm


