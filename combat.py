import entite as Ett
import equipement as E
import random


def DX(X):
    """renvoie un nombre aléatoire entre 1 et X"""
    return (random.randint(1, X))


def bataille(personnage: Ett.Joueur, ennemi: Ett.Monstre):
    """tant que le joueur et le(s) ennemi(s) ont 1 PV ou plus, on alterne entre le tour du joueur et celui du monstre"""
    combat = 1
    while (combat):
        action_du_tour_joueur(personnage, ennemi)
        action_du_tour_monstre(personnage, ennemi)
        if (personnage.pv == 0 or ennemi.pv == 0):
            combat = 0


def action_du_tour_monstre(personnage: Ett.Joueur, ennemi: Ett.Monstre):
    if ennemi.pv <= 20*ennemi.pv_max/100 and ennemi.taille_inv > 0:
        liste_inv = []
        for elt in ennemi.inventaire:
            if elt.cat == "soin":
                liste_inv.append(elt)
        if len(liste_inv) > 0:
            liste_inv[0].utilisation(ennemi)
    else:
        attaquer(ennemi, personnage, 0)


def action_du_tour_joueur(personnage:  Ett.Joueur, ennemi: Ett.Monstre):
    """effectue une action parmi celles disponibles, prend en parametre l ennemi et le joueur"""
    temps_recup_competence = 0
    premier_tour = True
    choix = input(
        "choisissez une action parmi :\n\t1 : attaquer\n\t2 : compétence spéciale\n\t3 : utiliser un objet\n")
    if int(choix) == 1:
        if premier_tour:
            degat_bonus = 0
            premier_tour = False
        attaquer(personnage, ennemi, 1, degat_bonus)
    elif int(choix) == 2:
        if temps_recuperation == 0:
            degat_bonus, compteur_tour_competence = personnage.competence_speciale()
            temps_recup_competence = 6
        elif temps_recup_competence == temps_recup_competence - compteur_tour_competence:
            degat_bonus = 0
    elif int(choix) == 3:
        print("Voici la liste de vos objets :\n")
        liste_inventaire = personnage.lister_inventaire_consommable()
    else:
        print("choix indisponible, votre tour est passé :)")
    temps_recuperation -= 1


def attaquer(source, destination, type_attaquant: int, degat_bonus=0):
    """prend en parametre la source de l attaque et sa destination, 
    elle peuvent chacune etre de type joueur ou monstre, puis on enleve 
    aux pv de la destinantion autant que les dégats de la source
    Si le type attaquant est 1, le joueur attaque un monstre, sinon, 
    c est le monstre qui attaque le joueur"""
    if type_attaquant == 1:
        atkspe = int(input(
            "Voulez vous tenter une attaque critique ?\n\t1 : oui\n\t2 : non\n"))
        if atkspe == 1:
            # par exemple si l attaque de bas (source.pc est 10, on attaque entre 0 et 20)
            degat = 2*(source.pc) - DX(2*(source.pc))
        else:
            degat = source.pc + degat_bonus
    elif type_attaquant == 0:
        degat = source.pc

    resistance = destination.pd
    destination.pv -= (degat-resistance)


joueur = Ett.Joueur("t", Ett.guerrier, Ett.humain)
monstre = Ett.Monstre(Ett.guerrier, Ett.humain)
bataille(joueur, monstre)
