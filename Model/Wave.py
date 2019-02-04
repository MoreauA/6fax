class Wave :

    def __init__(self, nbMonster):
        self.nbMonster = nbMonster

    def __get_nbMonster__(self):
        return self.nbMonster

    def __set_name__(self, nbMonster):
        if nbMonster > 0 :
            self.nbMonster = nbMonster
