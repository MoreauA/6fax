import time
import random
import pygame
from Model.Wave import Wave
from Model.Mob import Buf

pygame.init()
WINBUF = pygame.mixer.Sound("View/Data/Song/winBuf.wav")
WINBUF.set_volume(0.3)

class Map:

    def __init__(self, level, dislock):
        self.level = level
        self.dislock = dislock
        self.score = 0

        self.start = time.time()
        self.wave = Wave(level, 1)

        self.bufs = []
        self.createBuf()

        self.listPlatform = self.initPlatform()

    def running(self):
        return self.start+180 - time.time() > 0

    def waveFinished(self):
        return self.wave.finished()

    def createBuf(self):
        nbBuf = 0

        if self.level <= 2:
            nbBuf = 14
        elif self.level <= 4:
            nbBuf = 9
        elif self.level <= 8:
            nbBuf = 6

        for i in range(nbBuf):
            apparition = random.randint(1, 180)
            self.bufs.append(Buf("tacos", 50, apparition))

    def updateBufs(self):
        bufsTmp = []

        for buf in self.bufs:
            if self.timeActual() + 10 > buf.duration:
                bufsTmp.append(buf)

        self.bufs = bufsTmp

    def timeActual(self):
        return time.time()-self.start

    def mobs(self):
        return self.wave.getMonsters()

    def update(self, player, listPlatform):
        for currentMonster in self.wave.getMonsters():
            if currentMonster.value == 10:
                if currentMonster.update(player, listPlatform):
                    player.life -= 1
            elif currentMonster.value == 16:
                currentMonster.update(player)
            else:
                currentMonster.update()

        if self.wave.finished():
            self.score += self.wave.score
            self.wave.score = 0

            if time.time() - player.die > 1:
                if not player.dead:
                    num = self.wave.num + 1
                else:
                    num = self.wave.num
                    player.dead = False

                self.wave = Wave(self.level, num)

        butsTpm =[]
        for buf in self.bufs:

            if buf.collide(player):
                WINBUF.play()
                if buf.type == "tacos":
                    self.score += buf.value
                else:
                    if player.life <= player.MAXLIFE - buf.value:
                        player.life += buf.value
                    else:
                        player.life = player.MAXLIFE
            else:
                buf.update()
                butsTpm.append(buf)
        self.bufs = butsTpm

        self.wave.updateMonsters(self, player)
        self.updateBufs()

    def getScore(self):
        return self.wave.score + self.score

    def initPlatform(self): #Ajout platform des level :
        platForm = []
        if self.level == 1:
            platForm.append(Platform((450, 300), [90, 30])) #Position puis taille (taille standart de 90 * 30)
            platForm.append(Platform((350, 200), [30, 90]))
        elif self.level == 2:
            platForm.append(Platform((450, 300), [90, 30]))

        return platForm


class Platform:
    def __init__(self, initPos, initSize):
        self.pos = initPos
        self.size = initSize

    def inside(self, position, coor):
        if self.pos[coor] < position and position < (self.pos[coor] + self.size[coor]):
            return True
        return False

    def collide(self, projectil):
        if self.inside(projectil.pos[0], 0) and self.inside(projectil.pos[1], 1):
            return True
        return False
