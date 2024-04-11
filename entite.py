class Type ():
    def __init__(self, nom, pv_max, pc, pd, taille_inv_max):
        self.nom = nom
        self.pv_max = pv_max
        self.pc = pc
        self.pd = pd
        self.taille_inv_max = float(taille_inv_max)


class Joueur ():
    def __init__(self, nom: str, classe: Type, race: Type):
        self.nom = nom
        self.classe = classe.nom
        self.race = race.nom
        self.pv_max = classe.pv_max + race.pv_max
        self.pv = classe.pv_max + race.pv_max
        self.pc = classe.pc + race.pc
        self.pd = classe.pd + race.pd
        self.taille_inv_max = classe.taille_inv_max + race.taille_inv_max
        self.taille_inv = 0
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

    def inventaire_est_plein(self):
        poids_total_inv = 0
        for objet in self.inventaire:
            poids_total_inv += objet.poids
        if poids_total_inv >= self.taille_inv_max:
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
        self.taille_inv_max = classe.taille_inv_max + race.taille_inv_max
        self.taille_inv = 0
        self.inventaire = []


guerrier = Type("guerrier", 200, 10, 10, 20)
archer = Type("archer", 150, 8, 8, 20)
tank = Type("tank", 250, 8, 12, 40)

humain = Type("humain", 200, 10, 10, 20)
elfe = Type("elfe", 150, 8, 8, 20)
orc = Type("orc", 250, 100, 15, 40)

liste_classe = [guerrier, archer, tank]
liste_race = [humain, elfe, orc]

joueur = Joueur("Prout", guerrier, humain)
joueur.__repr__()
