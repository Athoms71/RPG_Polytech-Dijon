import entite as Ett


class Equipement():
    def __init__(self, nom: str, atk: int, dfc: int, prix: int,  cat: str):
        self.nom = nom
        self.atk = atk
        self.dfc = dfc
        self.prix = prix
        self.cat = cat


class Consommable():
    def __init__(self, nom: str, atk: int, dfc: int, heal: int, prix: int,  cat: str):
        self.nom = nom
        self.atk = atk
        self.dfc = dfc
        self.heal = heal
        self.prix = prix
        self.cat = cat

    def utilisation(self, joueur: Ett.Joueur):
        '''Met à jour les statistiques du joueur après utilisation d'un objet'''
        joueur.pv = min(joueur.pv+self.heal, joueur.pv_max)
        joueur.pc += self.atk
        joueur.pd += self.dfc
