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

    def update_sprite(self):
        '''Prend en paramètre un joueur et renvoie le chemin vers son sprite en fonction de sa race et de sa classe'''
        return f"./img/{self.race}_{self.classe}.png"

    def lister_inventaire_consommable(self):
        '''Prend en paramètre un joueur et renvoie une liste avec le nom de chaque consommable qu'il a dans son inventaire'''
        liste_inventaire = []
        for i in range(len(self.inventaire)):
            if self.inventaire[i].cat in ["soin", "attaque", "defense"]:
                liste_inventaire.append(self.inventaire[i].nom)
        return liste_inventaire


class Monstre ():
    def __init__(self, classe: Type, race: Type):
        self.classe = classe.nom
        self.race = race.nom
        self.pv_max = classe.pv_max + race.pv_max
        self.pv = classe.pv_max + race.pv_max
        self.pc = classe.pc + race.pc
        self.pd = classe.pd + race.pd
        self.inventaire = []


# Joueur & monstres normaux : somme = 70
guerrier = Type("guerrier", 50, 10, 10)
archer = Type("archer", 50, 10, 5)
tank = Type("tank", 55, 10, 5)
# somme = 70
humain = Type("humain", 50, 10, 10)
elfe = Type("elfe", 50, 10, 5)
orc = Type("orc", 55, 10, 5)

# Monstres spéciaux (ou boss) -> fin de chapitre

# ombre: somme = 60 + 50
ombre_race = Type("ombre", 40, 15, 0)
ombre_assaillante_classe = Type("Ombre Assaillante", 30, 15, 0)


# garde squelette : somme = 70 + 40
squelette_race = Type("squelette", 50, 20, 0)
garde_squelette_classe = Type("Garde Squelette", 20, 10, 10)

# garde golem : somme = 120 + 60
golem_race = Type("Golem", 100, 20, 10)
golem_foret_classe = Type("Le Gardien de la Fôret", 50, 10, 10)

# Gardien Nocturne : somme : 120 + 50
gardiens_race = Type("Gardiens", 100, 10, 20)
gardiens_nocturnes_classe = Type("Gardiens Nocturnes", 55, 30, 10)

# spectreGardien  : somme : 150 + 50
spectres_gardiens_classe = Type("spectres Gardiens", 150, 30, 20)

# spectre labyrinyhe : somme 120 + 100

spectre_race = Type("spectre", 160, 20, 20)
spectres_labyrinthe = Type("Spectre du labyrinthe", 80, 50, 30)


# spectre labyrinyhe : somme 120 + 100

spectres_profondeurs = Type("Spectre des profondeurs", 90, 50, 30)

# Gardien ombre

Gardiens_ombres_classe = Type("Gardiens Nocturnes", 170, 50, 70)

# boss final
boss_final_classe = Type("Seigneur des Ombres", 150, 40, 50)
boss_final_race = Type("Seigneur des Ombres race", 150, 30, 20)

liste_classe = [guerrier, archer, tank]
liste_race = [humain, elfe, orc]
