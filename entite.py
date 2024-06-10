class Type ():
    def __init__(self, nom, pv_max, pc, pd):
        self.nom = nom
        self.pv_max = pv_max
        self.pc = pc
        self.pd = pd


class Joueur ():
    def __init__(self, nom: str, classe: Type, race: Type):
        self.nom = nom
        self.classe = classe.nom
        self.race = race.nom
        self.pv_max = classe.pv_max + race.pv_max
        self.pv = classe.pv_max + race.pv_max
        self.pc = classe.pc + race.pc
        self.pd = classe.pd + race.pd
        self.inventaire = []
        self.argent = 0
        self.karma = 0.0
        self.main_gauche = None
        self.main_droite = None
        self.tete = None
        self.torse = None
        self.gants = None
        self.jambes = None
        self.pieds = None

    def lister_inventaire_consommable(self):
        liste_inventaire = []
        for i in range(len(self.inventaire)):
            if self.inventaire[i].cat in ["soin", "attaque", "defense"]:
                liste_inventaire.append(self.inventaire[i].nom)
        return liste_inventaire

    def inventaire_est_plein(self):
        if self.taille_inv >= self.taille_inv_max:
            return True
        else:
            return False

    def changement_equipement(self, choix_chgt: str):
        liste_chgt = []
        for elt in self.inventaire:
            if elt.cat == choix_chgt:
                liste_chgt.append(elt)
        print("Voici la liste de votre équipement :", liste_chgt)
        i_chgt = int(
            input("Entrez le numéro de l'équipement que vous souhaitez équiper : "))
        if choix_chgt == "main_gauche":
            self.main_gauche, liste_chgt[i_chgt -
                                         1] = liste_chgt[i_chgt-1], self.main_gauche
        elif choix_chgt == "main_droite":
            self.main_droite, liste_chgt[i_chgt -
                                         1] = liste_chgt[i_chgt-1], self.main_droite
            print("Vous venez d'équiper \""+self.main_droite+"\".")
        elif choix_chgt == "tete":
            self.tete, liste_chgt[i_chgt-1] = liste_chgt[i_chgt-1], self.tete
            print("Vous venez d'équiper \""+self.tete+"\".")
        elif choix_chgt == "torse":
            self.torse, liste_chgt[i_chgt-1] = liste_chgt[i_chgt-1], self.torse
            print("Vous venez d'équiper \""+self.torse+"\".")
        elif choix_chgt == "gants":
            self.gants, liste_chgt[i_chgt-1] = liste_chgt[i_chgt-1], self.gants
            print("Vous venez d'équiper \""+self.gants+"\".")
        elif choix_chgt == "jambes":
            self.jambes, liste_chgt[i_chgt -
                                    1] = liste_chgt[i_chgt-1], self.jambes
            print("Vous venez d'équiper \""+self.jambes+"\".")
        elif choix_chgt == "pieds":
            self.pieds, liste_chgt[i_chgt-1] = liste_chgt[i_chgt-1], self.pieds
            print("Vous venez d'équiper \""+self.pieds+"\".")
        if liste_chgt[i_chgt-1] != None:
            self.inventaire.append(liste_chgt[i_chgt-1])

    def __repr__(self):
        print(self.nom + ", vous êtes un " + self.classe +
              " de la race des " + self.race + "s.")
        print("Voici vos attributs :\n\t- PV : " + str(self.pv) +
              "\n\t- PC : " + str(self.pc) + "\n\t- PD : " + str(self.pd))


class Monstre ():
    def __init__(self, classe: Type, race: Type):
        self.classe = classe.nom
        self.race = race.nom
        self.pv_max = classe.pv_max + race.pv_max
        self.pv = classe.pv_max + race.pv_max
        self.pc = classe.pc + race.pc
        self.pd = classe.pd + race.pd
        self.inventaire = []

# Joueur


guerrier = Type("guerrier", 0, 20, 5)
archer = Type("archer", 0, 30, 0)
tank = Type("tank", 20, 2, 10)

humain = Type("humain", 100, 30, 20)
elfe = Type("elfe", 75, 40, 20)
orc = Type("orc", 200, 10, 40)

# monstres

ombre_race = Type("ombre", 50, 10, 0)
ombre_assayante_classe = Type("Ombre Assaillante", 10, 5, 3)


liste_classe = [guerrier, archer, tank]
liste_race = [humain, elfe, orc]
