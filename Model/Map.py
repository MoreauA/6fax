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
            elif currentMonster.value == 16:
                currentMonster.update(player)
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

            if ((xM + buf.SIZE) >= xP >= xM and (yM + buf.SIZE) >= yP >= yM) or ((xM + buf.SIZE) >= (xP + player.size[0]) >= xM and (yM + buf.SIZE) >= (yP + player.size[1]) >= yM):
                if buf.type == "tacos":
                    self.score += 50
                else:
                    if player.life <= player.MAXLIFE - 1:
                        player.life += 1
                    else:
                        player.life = player.MAXLIFE
            else:
                butsTpm.append(buf)
        self.bufs = butsTpm

        self.wave.updateMonsters(self, player)
        self.updateBufs()

    def getScore(self):
        return self.wave.score + self.score



