import random
from Model.Mob import Salade
from Model.Mob import MaisGunner
from Model.Mob import Tomate
from Model.Mob import Aubergine


class Wave:

    def __init__(self, level, numWave):
        self.monsters = []

        nbMonster = 3*level+2*numWave
        for i in range(nbMonster):
            num = random.randint(1, 1)
            if num == 1:
                wall = random.randint(1, 4)
                cote = random.randint(1, 2)
                self.monsters.append(Tomate(wall, cote))
            # elif num == 2:
            #     self.monsters[i-1] = MaisGunner()
            # elif num == 3:
            #     self.monsters[i-1] = Aubergine()
            # else:
            #     self.monsters[i-1] = Salade()

    # def __get_nbMonster__(self):
    #     return self.nbMonster
    #
    # def __set_name__(self, nbMonster):
    #     if nbMonster > 0 :
    #         self.nbMonster = nbMonster

    def finished(self):
        return len(self.monsters) == 0

    def updateMonsters(self):
        monstersTmp = self.monsters

        for i in range(0, len(self.monsters)):
            monster = self.monsters[i]

            if not monster.alive:
                # le monstre est mort
                # disparition du monstre
                monstersTmp.remove(monster)

        self.monsters = monstersTmp

    def getMonsters(self):
        return self.monsters