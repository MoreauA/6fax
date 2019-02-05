import abc

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
        self.alive = True
        self.speed = initSpeed
        self.moving = True

    def take_damage(self, damage):
        self.life -= damage
        if self.life < 0:
            self.alive = False

    def deal_damage(self, target):
        target.take_damage(self.force)

    def isMoving(self):
        return self.moving

    def movement(self,movement):
        self.moving = movement

# Les différents monstres du jeu :
class Monster(Mob):
    def __init__(self, initValue, initPos, initLife, initSize, initForce, initSpeed):
       Mob.__init__(self, initPos, initLife, initSize, initForce, initSpeed)
       self.value = initValue

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



# Monstre inoffensife :
class Salade(Monster):
    VALUE = 4
    MAXLIFE = 25
    pass

class Tomate(Monster):
    VALUE = 2
    MAXLIFE = 50
    def __init__(self, initPosition,initWall):
        speed = self.initSpeed(initWall)
        Monster.__init__(self, self.VALUE, initPosition, self.MAXLIFE, [25, 25], 0, speed)
        self.wall = initWall

    def move(self):
        #Le déplacement sur le sol ou le plafond :
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

    def initSpeed(self, wall):
        if wall == 1 or wall == 3:
            return [0.4, 0]
        else :
            return [0, 0.4]

    def attack(self):
        pass


#Monstre agrésif :
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

    def shoot(self):
        pass

    def gravityShift(self,newGrav):
        self.gravitation = newGrav

    def move(self,direction):
        print("Movement : ")
        self.pos[0] += direction[0] * self.speed[0]
        self.pos[1] += direction[1] * self.speed[1]

        #Collision detection :
        if self.pos[0] + self.size[0] > MAXPOSXWALL:
            self.pos[0] = MAXPOSXWALL - self.size[0]
        elif self.pos[0] < MINPOSXWALL:
            self.pos[0] = MINPOSXWALL

        if self.pos[1] + self.size[1] > MAXPOSYWALL:
            self.pos[1] = MAXPOSYWALL - self.size[1]
        elif self.pos[1] < MINPOSYWALL:
            self.pos[1] = MINPOSYWALL

    def update(self):
        self.pos[0] += self.gravitation[0]
        self.pos[1] += self.gravitation[1]

        if self.pos[0] + self.size[0] > MAXPOSXWALL:
            self.pos[0] = MAXPOSXWALL - self.size[0]
        elif self.pos[0] < MINPOSXWALL:
            self.pos[0] = MINPOSXWALL

        if self.pos[1] + self.size[1] > MAXPOSYWALL:
            self.pos[1] = MAXPOSYWALL - self.size[1]
        elif self.pos[1] < MINPOSYWALL:
            self.pos[1] = MINPOSYWALL