import time

class Map :

    def __init__(self, level, dislock):
        self.level = level
        self.dislock = dislock
        # self.tableauScore = open("../map-"+level+".txt", "r")
        self.score = 0
        self.start = time.time()

    def running(self):
        return 180 - self.start > 0
