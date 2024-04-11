class Type ():
    def __init__(self, nom, pvMax, pc, pd, tailleInvMax):
        self.nom = nom
        self.pvMax = pvMax
        self.pc = pc
        self.pd = pd
        self.tailleInvMax = float(tailleInvMax)


class Joueur ():
    def __init__(self, nom: str, classe: Type, race: Type):
        self.nom = nom
        self.classe = classe.nom
        self.race = race.nom
        self.pvMax = classe.pvMax + race.pvMax
        self.pv = classe.pvMax + race.pvMax
        self.pc = classe.pc + race.pc
        self.pd = classe.pd + race.pd
        self.tailleInvMax = classe.tailleInvMax + race.tailleInvMax
        self.tailleInv = 0
        self.inventaire = []
        self.argent = 0

    def inventaireEstPlein(self):
        poidsTotalInv = 0
        for objet in self.inventaire:
            poidsTotalInv += objet.poids
        if poidsTotalInv >= self.tailleInvMax:
            return True
        else:
            return False

    def changementEquipement(self, choixChgt: str):
        listeChgt = []
        for elt in self.inventaire:
            if elt.cat == choixChgt:
                listeChgt.append(elt)
        print("Voici la liste de votre équipement :", listeChgt)

    def __repr__(self):
        print(self.nom + ", vous êtes un " + self.classe +
              " de la race des " + self.race + "s.")
        print("Voici vos attributs :\n\t- PV : " + str(self.pv) +
              "\n\t- PC : " + str(self.pc) + "\n\t- PD : " + str(self.pd))


class Monstre ():
    def __init__(self, classe: Type, race: Type):
        self.classe = classe.nom
        self.race = race.nom
        self.pvMax = classe.pvMax + race.pvMax
        self.pv = classe.pvMax + race.pvMax
        self.pc = classe.pc + race.pc
        self.pd = classe.pd + race.pd
        self.tailleInvMax = classe.tailleInvMax + race.tailleInvMax
        self.tailleInv = 0
        self.inventaire = []


guerrier = Type("guerrier", 200, 10, 10, 20)
archer = Type("archer", 150, 8, 8, 20)
tank = Type("tank", 250, 8, 12, 40)

humain = Type("humain", 200, 10, 10, 20)
elfe = Type("elfe", 150, 8, 8, 20)
orc = Type("orc", 250, 8, 12, 40)

listeClasse = [guerrier, archer, tank]
listeRace = [humain, elfe, orc]

joueur = Joueur("Prout", guerrier, humain)
joueur.__repr__()
