import entite as Ett
import random


def DX(X):
    """renvoie un nombre aléatoire entre 1 et X"""
    return (random.randint(1, X))


def bataille(personnage: Ett.Joueur, ennemi: Ett.Monstre):
    """tant que le joueur et le(s) ennemi(s) on 1 PV ou plus, on alterne entre le tour du joueur et celui du monstre"""
    combat = 1
    while (combat):
        actionDuTourJoueur(personnage, ennemi)
        actionDuTourMonstre(personnage, ennemi)
        if (
                personnage.pv == 0 or ennemi.pv == 0):
            combat = 0


def actionDuTourMonstre(personnage: Ett.Joueur, ennemi: Ett.Monstre):
    # on prevoit quand les montres pourront faire plusieurs actions (IA du monstre)
    choix = 1
    if (int(choix) == 1):
        attaquer(ennemi, personnage)
    elif (int(choix) == 2):
        pass


def actionDuTourJoueur(personnage:  Ett.Joueur, ennemi: Ett.Monstre):
    """effectue une action parmis celles disponible, prend en parametre les ennemis present dans le combat et le joueur"""
    choix = input("choisissez une action parmis :\n1: attaquer\n\n")
    if (int(choix) == 1):
        attaquer(personnage, ennemi)
    else:
        print("choix indisponible, votre trour est passé :)")


def attaquer(source, destination):
    """prend en parametre la source de l attaque et sa destination, 
    elle peuvent chacun etre de type joueur ou monstre, puis on enleve 
    aux pv de la destinantion autant que les dégats de la source"""
    atkspe = input(
        "voulez vous tenter une attaque critique ?\n1 : oui\n2 : non\n\n")
    if atkspe == 1:
        # par exemple si l attaque de bas (source.pc est 10, on attaque entre 0 et 20)
        degat = 2*(source.pc) - main.DX(2*(source.pc))
    else:
        degat = source.pc

    resistance = destination.pd
    destination.pv = destination.pv - (degat-resistance)


# def objet(source):
#    for i in source.
