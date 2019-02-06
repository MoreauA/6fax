import abc
import random
import math
import time
import pygame

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

class Mob:

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
       Mob.__init__(self, self.initPos(initSize), initLife, initSize, initForce, self.initSpeed(initSpeed))

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
            y = random.randint(MINPOSYWALL, MAXPOSYWALL-size[1])
            return [MINPOSXWALL, y]
        elif self.wall == 3:
            x = random.randint(MINPOSXWALL, MAXPOSXWALL-size[1])
            return [x, MINPOSYWALL]
        else:
            y = random.randint(MINPOSYWALL, MAXPOSYWALL-size[0])
            return [MAXPOSXWALL-size[0], y]


# Monstre inoffensif :
class Salade(Monster):
    VALUE = 4
    MAXLIFE = 25
    pass

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
                self.pos[1] = MAXPOSYWALL - self.size[0]
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
    pass

class MaisGunner(Monster):
    VALUE = 10
    MAXLIFE = 60
    pass

class Player(Mob):
    def __init__(self, initPos, initLife, initSize, initForce):
        Mob.__init__(self, initPos, initLife, initSize, initForce, [0.85, 0.85])
        self.gravitation = [0, 1.5]
        self.shots = []
        self.push = [0, 0]
        self.precShoot = time.time()
        self.gunPicLeft = pygame.image.load('View/Data/Player/gun_64.png')
        self.gunPicLeft = pygame.transform.scale(self.gunPicLeft, (30, 30))
        self.gunPicRight = pygame.transform.flip(self.gunPicLeft, True, False)
        self.shotDir = 1




    def shoot(self, posShoot):
        if time.time() - self.precShoot > 0.2:
            self.precShoot = time.time()
            velX = abs((self.pos[0]+self.size[0]/2)-posShoot[0])
            velY = abs((self.pos[1]+self.size[1]/2)-posShoot[1])
            hypo = math.sqrt(velX+velY)
            speedForce = 5 #Vitesse d'une balle

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
                else :
                    direction.append(X)
                    direction.append(-Y)
            else :
                if posShoot[1] > (self.pos[1]+self.size[1]/2) :
                    direction.append(-X)
                    direction.append(Y)
                else :
                    direction.append(-X)
                    direction.append(-Y)
            self.shots.append(MeetBall(self.pos[0]+(self.size[0]/2), self.pos[1]+(self.size[1]/2), direction))

    def gravityShift(self, newGrav):
        self.gravitation = newGrav

    def move(self, direction):
        # print("Movement : ")
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
        elif self.pos[0] < MINPOSXWALL:
            self.pos[0] = MINPOSXWALL
            self.push = [0, 0]

        if self.pos[1] + self.size[1] > MAXPOSYWALL:
            self.pos[1] = MAXPOSYWALL - self.size[1]
            self.push = [0, 0]
        elif self.pos[1] < MINPOSYWALL:
            self.pos[1] = MINPOSYWALL
            self.push = [0, 0]

        newShots = []
        for shot in self.shots:
            shot.update(listMonster)
            if shot.est():
                newShots.append(shot)
        self.shots = newShots

        if pygame.mouse.get_pos()[0] > (self.pos[0] + (self.size[0] / 2)):
            self.shotDir = 1
        else:
            self.shotDir = 0
        gravite = 1.5
        pushForce = 2
        if self.pos[0] <= MINPOSXWALL + 35 and self.pos[1] == MINPOSYWALL: # mur haut, ressort haut/gauche
            self.gravityShift([gravite, 0])
            self.push = [pushForce, pushForce]
        elif self.pos[0] == MINPOSXWALL and self.pos[1] <= MINPOSYWALL + 35: # mur gauche, ressort haut/gauche
            self.gravityShift([0, gravite])
            self.push = [pushForce, pushForce]
        elif self.pos[0] == MINPOSXWALL and self.pos[1] >= MAXPOSYWALL - 35 - self.size[1]: # mur gauche, ressort bas/gauche
            self.gravityShift([0, -gravite])
            self.push = [pushForce, -pushForce]
        elif self.pos[0] <= MINPOSXWALL + 35 and self.pos[1] == MAXPOSYWALL - self.size[1]: # mur bas, ressort bas/gauche
            self.gravityShift([gravite, 0])
            self.push = [pushForce, -pushForce]
        elif self.pos[0] >= MAXPOSXWALL - 35 - self.size[0] and self.pos[1] == MAXPOSYWALL - self.size[1]: # mur bas, ressort bas/droite
            self.gravityShift([-gravite, 0])
            self.push = [-pushForce, -pushForce]
        elif self.pos[0] == MAXPOSXWALL - self.size[0] and self.pos[1] >= MAXPOSYWALL - 35 - self.size[1]: # mur droite, ressort bas/droite
            self.gravityShift([0, -gravite])
            self.push = [-pushForce, -pushForce]
        elif self.pos[0] == MAXPOSXWALL - self.size[0] and self.pos[1] <= MINPOSYWALL + 35: # mur droite, ressort haut/droite
            self.gravityShift([0, gravite])
            self.push = [-pushForce, pushForce]
        elif self.pos[0] >= MAXPOSXWALL - 35 - self.size[0] and self.pos[1] == MINPOSYWALL: # mur haut, ressort haut/droite
            self.gravityShift([-gravite, 0])
            self.push = [-pushForce, pushForce]

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
