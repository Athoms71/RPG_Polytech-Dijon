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

    def lister_inventaire_consommable(self):
        liste_inventaire = []
        for i in range(len(self.inventaire)):
            if self.inventaire[i].cat in ["soin", "attaque", "defense"]:
                liste_inventaire.append(self.inventaire[i])
                print("\t-", i+1, ":", self.inventaire[i])
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

    def competence_speciale(self):
        degat_bonus = 0
        if self.classe == "guerrier":
            print(
                "Vous infligez un effet d'hémorragie à votre adversaire pendant 2 tours !")
            degat_bonus = 10
            compteur_tour_competence = 2
        elif self.classe == "archer":
            print("Vos flèches sont empoisonnées pendant 3 tours !")
            degat_bonus = 5
            compteur_tour_competence = 3
        elif self.classe == "tank":
            print("Vous courez sur votre adversaire et l'écrasez sous votre poids !")
            degat_bonus = 20
            compteur_tour_competence = 1
        return degat_bonus, compteur_tour_competence

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
