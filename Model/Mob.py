import abc
import random
import math
import time
import pygame
from pygame.locals import *

MAXPOSXWALL = 0
MINPOSXWALL = 0
MAXPOSYWALL = 0
MINPOSYWALL = 0

def setCollider(minX, maxX, minY, maxY):
        global MAXPOSXWALL
        MAXPOSXWALL = maxX

        global MINPOSXWALL
        MINPOSXWALL = minX

        global MAXPOSYWALL
        MAXPOSYWALL = maxY

        global MINPOSYWALL
        MINPOSYWALL = minY

class Mob(pygame.sprite.Sprite):

    def __init__(self, initPos, initLife, initSize, initForce, initSpeed):
        self.pos = initPos
        self.life = initLife
        self.size = initSize
        self.force = initForce
        self.speed = initSpeed
        self.alive = True
        self.moving = True

    def take_damage(self, damage):
        self.life -= damage
        if self.life < 0:
            self.alive = False

    def deal_damage(self, target):
        target.take_damage(self.force)

    def isMoving(self):
        return self.moving

    def movement(self, movement):
        self.moving = movement

# Les différents monstres du jeu :
class Monster(Mob):
    def __init__(self, initValue, initLife, initSize, initForce, initSpeed, wall):
       self.wall = wall
       self.value = initValue
       Mob.__init__(self, self.initPos(initSize), initLife, self.initSz(initSize), initForce, self.initSpeed(initSpeed))

    @abc.abstractmethod
    def move(self):
        """Fait bouger les monstres"""
        return

    @abc.abstractmethod
    def attack(self):
        """Fait attacker les monstres"""
        return

    def update(self,):
        self.move()
        self.attack()

    def drop(self):
        return self.value

    def initSpeed(self, speed):
        if self.wall == 1 or self.wall == 3:
            return [speed, 0]
        else:
            return [0, speed]

    def initPos(self, size):
        if self.wall == 1:
            x = random.randint(MINPOSXWALL, MAXPOSXWALL-size[0])
            return [x, MAXPOSYWALL-size[1]]
        elif self.wall == 2:
            y = random.randint(MINPOSYWALL, MAXPOSYWALL-size[0])
            return [MINPOSXWALL, y]
        elif self.wall == 3:
            x = random.randint(MINPOSXWALL, MAXPOSXWALL-size[0])
            return [x, MINPOSYWALL]
        elif self.wall == 4:
            y = random.randint(MINPOSYWALL, MAXPOSYWALL-size[0])
            return [MAXPOSXWALL-size[1], y]
        else: #Le monstre vole (salade) donc wall == 0
            x = random.randint(MINPOSXWALL, MAXPOSXWALL-size[0])
            y = random.randint(MINPOSYWALL, MAXPOSYWALL - size[1])
            return [x, y]

    def initSz(self, size):
        if self.wall == 1 or self.wall == 3 or self.wall == 0:
            return size
        else:
            return [size[1], size[0]]

# Monstre inoffensif :
class Salade(Monster):
    VALUE = 4
    MAXLIFE = 25
    SPEED = 0.4

    def __init__(self):
        Monster.__init__(self, self.VALUE, self.MAXLIFE, [80, 60], 0, self.SPEED, 0)

    def move(self):
        self.pos[1] += self.speed[1]

        if self.pos[1] + self.size[1] > MAXPOSYWALL:
            self.pos[1] = MAXPOSYWALL - self.size[1]
            self.speed[1] = -self.speed[1]
        elif self.pos[1] < MINPOSYWALL:
            self.pos[1] = MINPOSYWALL
            self.speed[1] = -self.speed[1]

class Tomate(Monster):
    VALUE = 2
    MAXLIFE = 50
    SPEED = 0.4

    def __init__(self, wall):
        Monster.__init__(self, self.VALUE, self.MAXLIFE, [25, 25], 0, self.SPEED, wall)

    def move(self):
        # Le déplacement sur le sol ou le plafond :
        if self.wall == 1 or self.wall == 3:
            self.pos[0] += self.speed[0]
            if self.pos[0] + self.size[0] > MAXPOSXWALL:
                self.pos[0] = MAXPOSXWALL - self.size[0]
                self.speed[0] = -self.speed[0]
            elif self.pos[0] < MINPOSXWALL:
                self.pos[0] = MINPOSXWALL
                self.speed[0] = -self.speed[0]

        # Le déplacement sur les murs de gauche et de droite
        elif self.wall == 2 or self.wall == 4:
            self.pos[1] += self.speed[1]
            if self.pos[1] + self.size[1] > MAXPOSYWALL:
                self.pos[1] = MAXPOSYWALL - self.size[1]
                self.speed[1] = -self.speed[1]
            elif self.pos[1] < MINPOSYWALL:
                self.pos[1] = MINPOSYWALL
                self.speed[1] = -self.speed[1]

    def attack(self):
        pass

# Monstre agrésif :
class Aubergine(Monster):
    VALUE = 16
    MAXLIFE = 200
    SPEED = 0.3

    def __init__(self, wall):
        Monster.__init__(self, self.VALUE, self.MAXLIFE, [70, 100], 0, self.SPEED, wall)
        self.state = 0
        self.animation = 0
        self.left = False
        self.right = False

    def update(self, player):
        self.move(player)

    def move(self, player):
        # Le déplacement sur le sol ou le plafond :
        if self.wall == 1 or self.wall == 3:

            if player.pos[0] > self.pos[0]:
                self.pos[0] += self.SPEED
                self.left = (self.wall == 3)
                self.right = (self.wall == 1)

            elif player.pos[0] < self.pos[0]:
                self.pos[0] -= self.SPEED
                self.left = (self.wall == 1)
                self.right = (self.wall == 3)

            if self.pos[0] + self.size[0] > MAXPOSXWALL:
                self.pos[0] = MAXPOSXWALL - self.size[0]
                self.speed[0] = -self.speed[0]
            elif self.pos[0] < MINPOSXWALL:
                self.pos[0] = MINPOSXWALL
                self.speed[0] = -self.speed[0]

        # Le déplacement sur les murs de gauche et de droite
        elif self.wall == 2 or self.wall == 4:

            if player.pos[1] > self.pos[1]:
                self.pos[1] += self.SPEED
                self.left = (self.wall == 2)
                self.right = (self.wall == 4)

            elif player.pos[1] < self.pos[1]:
                self.pos[1] -= self.SPEED
                self.left = (self.wall == 4)
                self.right = (self.wall == 2)

            if self.pos[1] + self.size[1] > MAXPOSYWALL:
                self.pos[1] = MAXPOSYWALL - self.size[1]
                self.speed[1] = -self.speed[1]
            elif self.pos[1] < MINPOSYWALL:
                self.pos[1] = MINPOSYWALL
                self.speed[1] = -self.speed[1]


class MaisGunner(Monster):
    VALUE = 10
    MAXLIFE = 60
    SPEED = 1
    RELOAD = 2.0

    def __init__(self, wall):
        Monster.__init__(self, self.VALUE, self.MAXLIFE, [50, 120], 0, self.SPEED, wall)
        self.precShoot = time.time()
        self.shots = []
        self.efficiency = (random.randint(1, 15)/10)

    def move(self):
        # Le déplacement sur le sol ou le plafond :
        if self.wall == 1 or self.wall == 3:
            self.pos[0] += self.speed[0]
            if self.pos[0] + self.size[0] > MAXPOSXWALL:
                self.pos[0] = MAXPOSXWALL - self.size[0]
                self.speed[0] = -self.speed[0]
            elif self.pos[0] < MINPOSXWALL:
                self.pos[0] = MINPOSXWALL
                self.speed[0] = -self.speed[0]

        # Le déplacement sur les murs de gauche et de droite
        elif self.wall == 2 or self.wall == 4:
            self.pos[1] += self.speed[1]
            if self.pos[1] + self.size[1] > MAXPOSYWALL:
                self.pos[1] = MAXPOSYWALL - self.size[1]
                self.speed[1] = -self.speed[1]
            elif self.pos[1] < MINPOSYWALL:
                self.pos[1] = MINPOSYWALL
                self.speed[1] = -self.speed[1]

    def update(self, player):
        self.move()
        self.attack(player)
        touch = False

        newCorn = []
        for corn in self.shots:
            if corn.update(player):
                touch = True
            if corn.est():
                newCorn.append(corn)
        self.shots = newCorn
        return touch

    def attack(self, player):
        if time.time() - self.precShoot > self.RELOAD - self.efficiency:
            self.precShoot = time.time()
            self.shoot((player.pos[0], player.pos[1]))

    def shoot(self, posShoot):
        if True:
            self.precShoot = time.time()
            centerX = self.pos[0] + (self.size[0] / 2)
            centerY = self.pos[1] + (self.size[1] / 2)
            sX = centerX
            sY = centerY

            velX = abs(sX-posShoot[0])
            velY = abs(sY-posShoot[1])
            speedForce = 3 #Vitesse d'une balle de corn

            if velX > velY :
                ratio = velY/velX
                if velX == 0:
                    Y = speedForce
                else:
                    Y = (ratio * speedForce)
                if velY == 0:
                    X = speedForce
                else:
                    X = Y * (velX/velY)
            else:
                ratio = velX/velY
                if velY == 0:
                    X = speedForce
                else:
                    X = (ratio * speedForce)
                if velX == 0:
                    Y = speedForce
                else:
                    Y = X * (velY/velX)

            direction = []

            if posShoot[0] > (self.pos[0]+self.size[0]/2) :
                if posShoot[1] > (self.pos[1]+self.size[1]/2) :
                    direction.append(X)
                    direction.append(Y)
                else:
                    direction.append(X)
                    direction.append(-Y)
            else:
                if posShoot[1] > (self.pos[1]+self.size[1]/2):
                    direction.append(-X)
                    direction.append(Y)
                else :
                    direction.append(-X)
                    direction.append(-Y)
            self.shots.append(Corn(sX, sY, direction))

class Player(Mob):
    MAXLIFE = 5
    def __init__(self, initPos, initSize, initForce):
        Mob.__init__(self, initPos, self.MAXLIFE, initSize, initForce, [0.85, 0.85])
        self.gravitation = [0, 5]
        self.shots = []
        self.push = [0, 0]
        self.wall = 1
        self.precShoot = time.time()
        self.gunPicLeft = pygame.image.load('View/Data/Player/gun_64.png')
        self.gunPicLeft = pygame.transform.scale(self.gunPicLeft, (30, 30))
        self.gunPicRight = pygame.transform.flip(self.gunPicLeft, True, False)
        self.shotDir = 1
        self.die = time.time()

        self.left = True
        self.right = False
        self.airTime = True

    def reSpawn(self):
        self.die = time.time()
        self.pos = [500, 350]
        if self.wall == 2 or self.wall == 4:
            self.size = [self.size[1], self.size[0]]
        self.gravitation = [0, 5]
        self.wall = 1
        self.life = self.MAXLIFE

    def shoot(self, posShoot):
        if time.time() - self.precShoot > 0.2:
            self.precShoot = time.time()
            centerX = self.pos[0] + (self.size[0] / 2)
            centerY = self.pos[1] + (self.size[1] / 2)
            if self.shotDir == 1:
                cX = centerX
                cY = centerY - 15
                sX = cX + 15
                sY = cY + 15
            else:
                cX = centerX - 30
                cY = centerY - 15
                sX = cX + 15
                sY = cY + 15

            velX = abs(sX-posShoot[0])
            velY = abs(sY-posShoot[1])
            speedForce = 5 #Vitesse d'une balle

            if velX > velY:
                ratio = velY/velX
                if velX == 0:
                    Y = speedForce
                else:
                    Y = (ratio * speedForce)
                if velY == 0:
                    X = speedForce
                else:
                    X = Y * (velX/velY)
            else:
                ratio = velX/velY
                if velY == 0:
                    X = speedForce
                else:
                    X = (ratio * speedForce)
                if velX == 0:
                    Y = speedForce
                else:
                    Y = X * (velY/velX)

            direction = []

            if posShoot[0] > (self.pos[0]+self.size[0]/2) :
                if posShoot[1] > (self.pos[1]+self.size[1]/2) :
                    direction.append(X)
                    direction.append(Y)
                else:
                    direction.append(X)
                    direction.append(-Y)
            else:
                if posShoot[1] > (self.pos[1]+self.size[1]/2):
                    direction.append(-X)
                    direction.append(Y)
                else:
                    direction.append(-X)
                    direction.append(-Y)
            self.shots.append(MeetBall(sX, sY, direction))

    def gravityShift(self, newGrav):
        self.gravitation = newGrav
        if self.wall <= 2:
            self.wall += 2
        else:
            self.wall -= 2

    def move(self, direction):
        self.pos[0] += direction[0] * self.speed[0]
        self.pos[1] += direction[1] * self.speed[1]

        # Collision detection :
        if self.pos[0] + self.size[0] > MAXPOSXWALL:
            self.pos[0] = MAXPOSXWALL - self.size[0]
        elif self.pos[0] < MINPOSXWALL:
            self.pos[0] = MINPOSXWALL

        if self.pos[1] + self.size[1] > MAXPOSYWALL:
            self.pos[1] = MAXPOSYWALL - self.size[1]
        elif self.pos[1] < MINPOSYWALL:
            self.pos[1] = MINPOSYWALL

    def update(self, listMonster):
        self.pos[0] += self.gravitation[0]
        self.pos[1] += self.gravitation[1]

        self.pos[0] += self.push[0]
        self.pos[1] += self.push[1]

        if self.pos[0] + self.size[0] > MAXPOSXWALL:
            self.pos[0] = MAXPOSXWALL - self.size[0]
            self.push = [0, 0]
            self.airTime = False
        elif self.pos[0] < MINPOSXWALL:
            self.pos[0] = MINPOSXWALL
            self.push = [0, 0]
            self.airTime = False

        if self.pos[1] + self.size[1] > MAXPOSYWALL:
            self.pos[1] = MAXPOSYWALL - self.size[1]
            self.push = [0, 0]
            self.airTime = False
        elif self.pos[1] < MINPOSYWALL:
            self.pos[1] = MINPOSYWALL
            self.push = [0, 0]
            self.airTime = False

        newShots = []
        for shot in self.shots:
            shot.update(listMonster)
            if shot.est():
                newShots.append(shot)
        self.shots = newShots

        if self.wall == 1 or self.wall == 3:
            if pygame.mouse.get_pos()[0] > (self.pos[0] + (self.size[0] / 2)):
                self.shotDir = 1
            else:
                self.shotDir = 0
        else:
            if pygame.mouse.get_pos()[1] > (self.pos[1] + (self.size[1] / 2)):
                self.shotDir = 0
            else:
                self.shotDir = 1

        # Si le joueur a touché un ressort
        gravite = 5
        pushForce = 2

        if self.wall == 1: # mur du bas
            if self.pos[0] <= MINPOSXWALL + 35 and self.pos[1] + self.size[1] >= MAXPOSYWALL - 35:  # ressort bas/gauche
                self.gravityShift([gravite, 0])
                self.push = [pushForce, -pushForce]
                self.size = [self.size[1], self.size[0]]
                self.wall = 4
                self.airTime = True
                return 2
            elif self.pos[0] + self.size[0] >= MAXPOSXWALL - 35 and self.pos[1] + self.size[1] >= MAXPOSYWALL - 35: # ressort bas/droite
                self.gravityShift([-gravite, 0])
                self.push = [-pushForce, -pushForce]
                self.size = [self.size[1], self.size[0]]
                self.wall = 2
                self.airTime = True
                return 3
        elif self.wall == 2: # mur de gauche
            if self.pos[0] <= MINPOSXWALL + 35 and self.pos[1] <= MINPOSYWALL + 35:  # ressort haut/gauche
                self.gravityShift([0, gravite])
                self.push = [pushForce, pushForce]
                self.size = [self.size[1], self.size[0]]
                self.wall = 1
                self.airTime = True
                return 1
            elif self.pos[0] <= MINPOSXWALL + 35 and self.pos[1] >= MAXPOSYWALL - 35 - self.size[1]:  # ressort bas/gauche
                self.gravityShift([0, -gravite])
                self.push = [pushForce, -pushForce]
                self.size = [self.size[1], self.size[0]]
                self.wall = 3
                self.airTime = True
                return 2
        elif self.wall == 3: # mur du haut
            if self.pos[0] >= MAXPOSXWALL - 35 - self.size[0] and self.pos[1] >= MINPOSYWALL - 35:  # ressort haut/droite
                self.gravityShift([-gravite, 0])
                self.push = [-pushForce, pushForce]
                self.size = [self.size[1], self.size[0]]
                self.wall = 2
                self.airTime = True
                return 4
            elif self.pos[0] <= MINPOSXWALL + 35 and self.pos[1] <= MINPOSYWALL + 35: # ressort haut/gauche
                self.gravityShift([gravite, 0])
                self.push = [pushForce, pushForce]
                self.size = [self.size[1], self.size[0]]
                self.wall = 4
                self.airTime = True
                return 1
        else: # self.wall == 4; mur de droite
            if self.pos[0] + self.size[0] >= MAXPOSXWALL and self.pos[1] >= MAXPOSYWALL - 35 - self.size[1]:  # ressort bas/droite
                self.gravityShift([0, -gravite])
                self.push = [-pushForce, -pushForce]
                self.size = [self.size[1], self.size[0]]
                self.wall = 3
                self.airTime = True
                return 3
            elif self.pos[0] >= MAXPOSXWALL - self.size[0] and self.pos[1] <= MINPOSYWALL + 35:  # ressort haut/droite
                self.gravityShift([0, gravite])
                self.push = [-pushForce, pushForce]
                self.size = [self.size[1], self.size[0]]
                self.wall = 1
                self.airTime = True
                return 4
        return 0

class MeetBall:
    BULLETDAMAGE = 50

    def __init__(self, vX, vY, initVelocity):
        self.pos = [vX, vY]
        self.speed = initVelocity
        self.size = [8, 8]
        self.existe = True

    def update(self,listMonster):
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]

        if self.pos[0] + self.size[0] > MAXPOSXWALL:
            self.existe = False
        elif self.pos[0] < MINPOSXWALL:
            self.existe = False

        if self.pos[1] + self.size[1] > MAXPOSYWALL:
            self.existe = False
        elif self.pos[1] < MINPOSYWALL:
            self.existe = False

        if self.existe:
            for monster in listMonster:
                if (self.pos[0] > monster.pos[0]) and (self.pos[0] < (monster.pos[0] + monster.size[0])):
                    if (self.pos[1] > monster.pos[1]) and (self.pos[1] < (monster.pos[1] + monster.size[1])):
                        monster.take_damage(self.BULLETDAMAGE)
                        self.existe = False

    def est(self):
        return self.existe

class Corn(MeetBall):
    def __init__(self,initX, initY, initDir):
        MeetBall.__init__(self, initX, initY, initDir)

    def update(self, player):
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]

        if self.pos[0] + self.size[0] > MAXPOSXWALL:
            self.existe = False
        elif self.pos[0] < MINPOSXWALL:
            self.existe = False

        if self.pos[1] + self.size[1] > MAXPOSYWALL:
            self.existe = False
        elif self.pos[1] < MINPOSYWALL:
            self.existe = False

        if self.existe:
            if (self.pos[0] > player.pos[0]) and (self.pos[0] < (player.pos[0] + player.size[0])):
                if (self.pos[1] > player.pos[1]) and (self.pos[1] < (player.pos[1] + player.size[1])):
                    self.existe = False
                    return True
        return False

class Buf:
    SIZE = 20

    def __init__(self, type, value, duration, pos = None, wall = None):
        self.type = type
        self.value = value
        self.duration = duration

        if wall is None:
            self.wall = random.randint(1, 4)
        else:
            self.wall = wall

        if pos is None:
            self.pos = self.initPos()
        else:
            self.pos = pos

    def initPos(self):
        if self.wall == 1:
            x = random.randint(MINPOSXWALL, MAXPOSXWALL - self.SIZE)
            return [x, MAXPOSYWALL - self.SIZE]
        elif self.wall == 2:
            y = random.randint(MINPOSYWALL, MAXPOSYWALL - self.SIZE)
            return [MINPOSXWALL, y]
        elif self.wall == 3:
            x = random.randint(MINPOSXWALL, MAXPOSXWALL - self.SIZE)
            return [x, MINPOSYWALL]
        else:
            y = random.randint(MINPOSYWALL, MAXPOSYWALL - self.SIZE)
            return [MAXPOSXWALL - self.SIZE, y]
