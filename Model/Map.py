import time
from Model import Wave
from Model import Element

class Map:

    def __init__(self, level, dislock):
        self.level = level
        self.dislock = dislock
        # self.tableauScore = open("../map-"+level+".txt", "r")
        self.score = 0

        self.start = time.time()
        self.wave = Wave(level, 1)

        self.elements = []
        self.createElement()

    def running(self):
        return 180 - self.start > 0

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

        for i in range(1, nbElement):
            self.elements[i-1] = Element()


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

    def update(self):
        for currentMonster in self.wave.getMonsters():
            currentMonster.update()