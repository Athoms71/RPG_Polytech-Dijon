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
        attaquer(ennemi, personnage)


def action_du_tour_joueur(personnage:  Ett.Joueur, ennemi: Ett.Monstre):
    """effectue une action parmis celles disponible, prend en parametre les ennemis present dans le combat et le joueur"""
    choix = input("choisissez une action parmi :\n1: attaquer\n\n")
    if (int(choix) == 1):
        attaquer(personnage, ennemi, 1)
    else:
        print("choix indisponible, votre tour est passé :)")


def attaquer(source, destination, type_attaquant: int):
    """prend en parametre la source de l attaque et sa destination, 
    elle peuvent chacun etre de type joueur ou monstre, puis on enleve 
    aux pv de la destinantion autant que les dégats de la source
    Si le type attaquant est 1, le joueur attaque un monstre, sinon, 
    c est le montres qui attaque le joueur"""
    if type_attaquant == 1:
        atkspe = int(input(
            "voulez vous tenter une attaque critique ?\n1 : oui\n2 : non\n\n"))
        if atkspe == 1:
            # par exemple si l attaque de bas (source.pc est 10, on attaque entre 0 et 20)
            degat = 2*(source.pc) - DX(2*(source.pc))
        else:
            degat = source.pc

    resistance = destination.pd
    destination.pv = destination.pv - (degat-resistance)
