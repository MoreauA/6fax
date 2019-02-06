import random
from Model.Mob import Salade
from Model.Mob import MaisGunner
from Model.Mob import Tomate
from Model.Mob import Aubergine


class Wave:

    def __init__(self, level, numWave):
        self.monsters = []
        self.num = numWave
        self.score = 0
        nbMonster = 3*level+2*numWave
        for i in range(nbMonster):
            num = random.randint(1, 1)
            if num == 1:
                wall = random.randint(1, 4)
                self.monsters.append(Tomate(wall))
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
        monstersTmp = []

        for monster in self.monsters:

            if monster.alive:
                # le monstre est en vie
                # ajout du monstres à la liste
                monstersTmp.append(monster)
            else:
                self.score += monster.value
        self.monsters = monstersTmp

    def getMonsters(self):
        return self.monsters


