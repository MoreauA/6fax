import time
import random
from Model.Wave import Wave
from Model.Mob import Buf

class Map:

    def __init__(self, level, dislock):
        self.level = level
        self.dislock = dislock
        self.score = 0

        self.start = time.time()
        self.wave = Wave(level, 1)

        self.bufs = []
        self.createBuf()

    def running(self):
        return self.start+180 - time.time() > 0

    def waveFinished(self):
        return self.wave.finished()

    def createBuf(self):
        nbBuf = 0

        if self.level <= 2:
            nbBuf = 5
        elif self.level <= 4:
            nbBuf = 4
        elif self.level <= 8:
            nbBuf = 3

        for i in range(nbBuf):
            apparition = random.randint(1, 180)
            self.bufs.append(Buf("tacos", 50, apparition))

    def updateBufs(self):
        bufsTmp = []

        for buf in self.bufs:
            if self.timeActual()+5 > buf.duration:
                bufsTmp.append(buf)

        self.bufs = bufsTmp

    def timeActual(self):
        return time.time()-self.start

    def mobs(self):
        return self.wave.getMonsters()

    def update(self, player):
        for currentMonster in self.wave.getMonsters():
            if currentMonster.value == 10:
                if currentMonster.update(player):
                    player.life -= 1
            else:
                currentMonster.update()

        if self.wave.finished():
            self.score += self.wave.score
            self.wave.score = 0
            num = self.wave.num + 1

            if time.time() - player.die > 1:
                num -= 1
            self.wave = Wave(self.level, num)

        butsTpm =[]
        for buf in self.bufs:
            xP = player.pos[0]
            yP = player.pos[1]

            xM = buf.pos[0]
            yM = buf.pos[1]

            if (xM + buf.SIZE) >= xP >= xM and (yM + buf.SIZE) >= yP >= yM:
                self.score += 50
            elif (xM + buf.SIZE) >= (xP + player.size[0]) >= xM and (yM + buf.SIZE) >= (yP + player.size[1]) >= yM:
                self.score += 50
            else:
                butsTpm.append(buf)
        self.bufs = butsTpm

        self.wave.updateMonsters(player)
        self.updateBufs()

    def getScore(self):
        return self.wave.score + self.score

    # def initPlatForm(self):
    #     platForm = []
    #     platForm.append(Platform((350, 90), (90, 30)))
    #     platForm.append(Platform((100, 270), (90, 30)))
    #     platForm.append(Platform((300, 450), (90, 30)))
    #     platForm.append(Platform((390, 400), (30, 90)))
    #     return platForm


