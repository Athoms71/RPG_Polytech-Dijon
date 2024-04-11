class Equipement():
    def __init__(self, nom, atk, dfc, prix, poids, cat, equip=False):
        self.nom = nom
        self.atk = atk
        self.dfc = dfc
        self.prix = prix
        self.equip = equip
        self.poids = poids
        self.cat = cat


class Consommable():
    def __init__(self, nom, atk, dfc, heal, prix, poids, cat):
        self.nom = nom
        self.atk = atk
        self.dfc = dfc
        self.heal = heal
        self.prix = prix
        self.poids = poids
        self.cat = cat

    def utilisation(self, joueur):
        if self.cat == "soin":
            joueur.pv += self.heal
        elif self.cat == "attaque":
            joueur.pc += self.atk
        elif self.cat == "defense":
            joueur.pd += self.dfc
