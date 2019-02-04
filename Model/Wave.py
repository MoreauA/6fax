import random
from Model import Salade
from Model import MaisGunner
from Model import Tomate
from Model import Aubergine


class Wave:

    def __init__(self, level, numWave):
        self.monsters = []

        nbMonster = 3*level+2*numWave
        for i in range(1, nbMonster):
            num = random.randint(1, 4)
            if num == 1:
                self.monsters[i-1] = Tomate()
            elif num == 2:
                self.monsters[i-1] = MaisGunner()
            elif num == 3:
                self.monsters[i-1] = Aubergine()
            else:
                self.monsters[i-1] = Salade()

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

        for i in range(1, len(self.monsters)):
            monster = self.monsters[i-1]

            if not monster.alive:
                # le monstre est mort
                # disparition du monstre
                monstersTmp.remove(monster)

        self.monsters = monstersTmp
