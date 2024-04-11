class Equipement():
    def __init__(self, nom: str, atk: int, dfc: int, prix: float, poids: float, cat: str):
        self.nom = nom
        self.atk = atk
        self.dfc = dfc
        self.prix = prix
        self.poids = poids
        self.cat = cat


class Consommable():
    def __init__(self, nom: str, atk: int, dfc: int, heal: int, prix: float, poids: float, cat: str):
        self.nom = nom
        self.atk = atk
        self.dfc = dfc
        self.heal = heal
        self.prix = prix
        self.poids = poids

    def utilisation(self, joueur):
        joueur.pv += self.heal
        joueur.pc += self.atk
        joueur.pd += self.dfc
