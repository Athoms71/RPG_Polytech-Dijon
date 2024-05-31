import entite as Ett
import equipement as E
import random
import textbox as TB


def DX(X):
    """renvoie un nombre aléatoire entre 1 et X"""
    return (random.randint(1, X))


def bataille(personnage: Ett.Joueur, ennemi: Ett.Monstre):
    """tant que le joueur et le(s) ennemi(s) ont 1 PV ou plus, on alterne entre le tour du joueur et celui du monstre"""
    while personnage.pv > 0 and ennemi.pv > 0:
        if personnage.pv > 0:
            TB.textbox_output("Votre tour :")
            action_du_tour_joueur(personnage, ennemi)
        if ennemi.pv > 0:
            TB.textbox_output("Tour du "+str(ennemi.classe+" :"))
            action_du_tour_monstre(personnage, ennemi)

    TB.textbox_output("La bataille est terminée !")
    if personnage.pv <= 0:
        TB.textbox_output("Vous avez perdu...")
    else:
        TB.textbox_output("Vous avez gagné !")


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
    choix = TB.textbox_input(
        "choisissez une action parmi :@-1 : attaquer@-2 : compétence spéciale@-3 : utiliser un objet@")
    if choix == "1":
        if premier_tour:
            degat_bonus = 0
            premier_tour = False
        attaquer(personnage, ennemi, 1, degat_bonus)
    elif choix == "2":
        if temps_recup_competence == 0:
            degat_bonus, compteur_tour_competence = personnage.competence_speciale()
            temps_recup_competence = 6
        elif temps_recup_competence == temps_recup_competence - compteur_tour_competence:
            degat_bonus = 0

    elif choix == "3":
        liste_equipements = ''  # il s agit de la liste bien formatée
        for i in range(len(personnage.lister_inventaire_consommable())):
            liste_equipements += str(
                # on ajoute tt les élément a la suite en leur donnant un indice et en ajoutant des sauts al la ligne
                str(i+1)+'- '+personnage.lister_inventaire_consommable()[i])+'@'
        choix_consommable = TB.textbox_input("Choisissez l objet que vous souhaitez utiliser parmi la liste de vos objets :@" +
                                             liste_equipements)

        if (choix_consommable in ["1", "2", "3", "4", "5", "6", "7", "8"]):
            choix_consommable = int(choix_consommable)-1
            if (choix_consommable <= len((personnage.lister_inventaire_consommable())) and len((personnage.lister_inventaire_consommable())) != 0):
                objChoisi = personnage.lister_inventaire_consommable()[
                    choix_consommable]
                TB.textbox_output(str(objChoisi))

                objChoisi.utilisation(personnage)
                TB.textbox_output(
                    "vous avez utilisé '"+str(objChoisi)+"@Vous nouvelles statisitiques sont :@- PV : "+str(personnage.pv)+"/"+str(personnage.pv_max)+"@- Dégâts par coup : "+str(personnage.pc))

        else:
            TB.textbox_output(
                "choix invalide, votre tour est passé :)")
            TB.textbox_output("le choix est"+str(choix_consommable))

    else:
        TB.textbox_output("choix indisponible, votre tour est passé :)")
    temps_recup_competence -= 1


def attaquer(source, destination, type_attaquant: int, degat_bonus=0):
    """prend en parametre la source de l attaque et sa destination,
    elle peuvent chacune etre de type joueur ou monstre, puis on enleve
    aux pv de la destinantion autant que les dégats de la source
    Si le type attaquant est 1, le joueur attaque un monstre, sinon,
    c est le monstre qui attaque le joueur"""

    if type_attaquant == 1:
        crit = TB.textbox_input(
            "Voulez vous tenter une attaque critique ?@-1 : oui@-2 : non@")
        if crit == "1":
            # par exemple si l attaque de bas (source.pc est 10, on attaque entre 0 et 20)
            degat = int(source.pc/2 + DX((source.pc))/2)
        else:
            degat = source.pc + degat_bonus

        TB.textbox_output("vous avez infligé "+str(degat-destination.pd) +
                          " dégats, l'adversaire a encore " + str(max(0, destination.pv-(degat-destination.pd)))+" PV.")
    elif type_attaquant == 0:
        degat = source.pc
        TB.textbox_output("le "+str(source.classe)+" vous attaque et vous inflige "+(
            str(degat-destination.pd)) + " degats. Il vous reste " + str(max(0, destination.pv-(degat-destination.pd))) + " PV")
    resistance = destination.pd
    destination.pv -= (degat-resistance)
