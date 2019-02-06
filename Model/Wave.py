import time
import random
from Model.Mob import *
# from Model.Mob import MaisGunner
from Model.Mob import Tomate
from Model.Mob import Aubergine


class Wave:

    def __init__(self, level, numWave):
        self.monsters = []
        self.num = numWave
        self.score = 0
        self.touchMonster = time.time()

        nbMonster = 3*level+2*numWave
        for i in range(nbMonster):
            num = random.randint(1, 4)
            if num == 1:
                wall = random.randint(1, 4)
                self.monsters.append(Tomate(wall))
            elif num == 2:
                 self.monsters.append(Salade())
            elif num == 3:
                wall = random.randint(1, 4)
                self.monsters.append(Aubergine(wall))
            else:
                wall = random.randint(1, 4)
                self.monsters.append(MaisGunner(wall))

    def finished(self):
        return len(self.monsters) == 0

    def updateMonsters(self, player):
        monstersTmp = []

        for monster in self.monsters:
            xP = player.pos[0]
            yP = player.pos[1]

            xM = monster.pos[0]
            yM = monster.pos[1]

            if time.time() - self.touchMonster > 1:

                if (xM + monster.size[0]) >= xP >= xM and (yM + monster.size[1]) >= yP >= yM:
                    self.score -= 20
                    self.touchMonster = time.time()
                elif (xM + monster.size[0]) >= (xP + player.size[0]) >= xM and (yM + monster.size[1]) >= (yP + player.size[1]) >= yM:
                    self.score -= 20
                    self.touchMonster = time.time()

            if monster.alive:
                # le monstre est en vie
                # ajout du monstres à la liste
                monstersTmp.append(monster)
            else:
                self.score += monster.value
        self.monsters = monstersTmp

    def getMonsters(self):
        return self.monsters


