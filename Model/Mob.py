class Mob:

    def __init__(self, initPos, initLife, initSize, initForce, initSpeed):
        self.pos = initPos
        self.life = initLife
        self.size = initSize
        self.force = initForce
        self.alive = True
        self.speed = initSpeed

    def take_damage(self, damage):
        self.life -= damage
        if self.life < 0 :
            self.die()

    def die(self):
        self.alive = False

    def attack(self, target):
        target.take_damage(self.force)


class Monster(Mob):
    def __init__(self,initType):
       self.type = initType

    def move(self,player):
        if player.gravity :


class Player(Mob):
    def update(self):
        print("LoL")