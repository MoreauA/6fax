from Model.Buf import Buf

class Element:

    def __init__(self, nom):
        self.nom = nom

        if nom == "tacos":
            self.buf = Buf("monnaie", 1, 5)
