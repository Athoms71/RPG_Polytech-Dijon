import entite as Ett
import equipement as E
import gestion_bruits as GB
import random
import textbox as TB
import pygame


def DX(X):
    '''Renvoie un nombre aléatoire entre 1 et X'''
    return (random.randint(1, X))


def bataille(screen: pygame.Surface, personnage: Ett.Joueur, ennemi: Ett.Monstre, ch_sprite_ennemi: str = "./img/skeleton_warriors.jpg"):
    '''Tant que le joueur et le(s) ennemi(s) ont 1 PV ou plus, on alterne entre le tour du joueur et celui du monstre'''
    if ch_sprite_ennemi == "./img/seigneur_ombres.png":
        # Cas particulier de musique si on est face au boss final
        pygame.mixer.music.load("./sounds/battle_of_the_dragons.mp3")
    else:
        pygame.mixer.music.load("./sounds/battle_music.mp3")
    pygame.mixer.music.play(-1)
    sprite_ennemi = pygame.image.load(ch_sprite_ennemi)
    sprite_ennemi = pygame.transform.flip(sprite_ennemi, True, False)
    screen.blit(sprite_ennemi, (screen.get_width()-25-sprite_ennemi.get_width(),
                                screen.get_height()-(sprite_ennemi.get_height()+50)))
    TB.textbox_output("Vous allez vous battre contre " +
                      str(ennemi.classe)+", préparez vous au combat !")
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
        TB.textbox_output(
            "Tous les espoirs du royaume s'évanouissent avec votre mort...")
        TB.textbox_output("Fin du jeu")
    else:
        TB.textbox_output("Vous avez gagné !")


def action_du_tour_monstre(personnage: Ett.Joueur, ennemi: Ett.Monstre):
    '''On regarde si le monstre a moins de 20% de ses PV, puis, s'il a une potion de soins, il se soigne en l'utilisant. Sinon, il attaque'''
    liste_inv = []
    for elt in ennemi.inventaire:
        if elt.cat == "soin":
            liste_inv.append(elt)
    if ennemi.pv <= 20*ennemi.pv_max/100 and len(liste_inv) > 0:
        liste_inv[0].utilisation(ennemi)
    else:
        attaquer(ennemi, personnage, 0)


def action_du_tour_joueur(personnage:  Ett.Joueur, ennemi: Ett.Monstre):
    '''Effectue une action parmi celles disponibles (utiliser un consommable ou attaquer, si le joueur n'a pas de consommable dans son inventaire, il n'a pas le choix et il attaque nécessairement)\n
    Prend en paramètre l'ennemi et le joueur'''
    done = False
    if (len(personnage.lister_inventaire_consommable()) > 0):
        while not done:
            choix = TB.textbox_input(
                "Choisissez une action parmi :@- 1 : attaquer@- 2 : utiliser un objet")
            if choix in ["1", "2"]:
                done = True
    else:
        choix = "1"
        TB.textbox_output("Vous attaquez")

    if choix == "1":
        if premier_tour:
            premier_tour = False
        attaquer(personnage, ennemi, 1)

    elif choix == "2":
        liste_equipements = ''  # il s'agit de la liste bien formatée
        for i in range(len(personnage.lister_inventaire_consommable())):
            liste_equipements += str(
                # on ajoute tous les éléments à la suite en leur donnant un indice et en ajoutant des sauts à la ligne
                str(i+1)+'- '+personnage.lister_inventaire_consommable()[i])+'@'
        done2 = False
        while not done2:
            choix_consommable = TB.textbox_input("Choisissez l'objet que vous souhaitez utiliser parmi la liste de vos objets :@" +
                                                 liste_equipements)
            if (choix_consommable in ["1", "2", "3", "4", "5", "6", "7", "8"]):
                choix_consommable = int(choix_consommable)-1
                done2 = True
                if (choix_consommable <= len((personnage.lister_inventaire_consommable())) and len((personnage.lister_inventaire_consommable())) != 0):
                    nomObjChoisi = personnage.lister_inventaire_consommable()[
                        choix_consommable]

                done = False
                i = 0
                # on vient parcourir l'inventaire du joueur pour y trouver l'élément cherché
                while (not done):
                    if personnage.inventaire[i].nom == nomObjChoisi:
                        objChoisi = personnage.inventaire[i]
                        done = True
                        break
                    i += 1
                    if i > len(personnage.inventaire):
                        break
                # on utilise l'élément choisi, puis on le retire
                objChoisi.utilisation(personnage)
                personnage.inventaire.pop(i)

                bonusArmes = 0
                bonusDef = 0

                if (len(personnage.inventaire) != 0):
                    for i in range(len(personnage.inventaire)):
                        if type(personnage.inventaire[i]) == E.Equipement:
                            bonusArmes += personnage.inventaire[i].atk
                # on calcule les bonus de def liés aux défenses

                if (len(ennemi.inventaire) != 0):
                    for i in range(len(ennemi.inventaire)):
                        if type(ennemi.inventaire[i]) == E.Equipement:
                            bonusDef += ennemi.inventaire[i].dfc

                TB.textbox_output(
                    "Vous avez utilisé '"+str(nomObjChoisi)+"'@Vos nouvelles statisitiques sont :@- PV : "+str(personnage.pv)+"/"+str(personnage.pv_max)+"@- Dégâts par coup : "+(str(max(0, personnage.pc-ennemi.pd+bonusArmes)))+"@- Résistance : "+str(personnage.pd+bonusDef))

    else:
        TB.textbox_output("Choix indisponible, votre tour est passé :)")


def attaquer(source, destination, type_attaquant: int):
    '''Prend en paramètre la source de l'attaque et sa destination (Joueur / Monstre).\n
    On enlève aux pv de la destinantion autant que les dégats de la source.\n
    Si le type attaquant est 1, le joueur attaque un monstre, sinon c'est le monstre qui attaque le joueur, pour attaquer.\n
    On calcule ensuite les bonus d'attaque et défense de chaque entité pour les ajouter et soustraire à la fin.'''

    if type_attaquant == 1:
        # on calcule le bonus d'attaque lié aux armes
        bonusArmes = 0
        bonusDef = 0

        if (len(source.inventaire) != 0):
            for i in range(len(source.inventaire)):
                if type(source.inventaire[i]) == E.Equipement:
                    bonusArmes += source.inventaire[i].atk
        # on calcule le bonus de def lié aux défenses

        if (len(destination.inventaire) != 0):
            for i in range(len(destination.inventaire)):
                if type(destination.inventaire[i]) == E.Equipement:
                    bonusDef += destination.inventaire[i].dfc
        done = False
        while not done:
            crit = TB.textbox_input(
                "Voulez vous tenter une attaque critique ?@- 1 : oui@- 2 : non@")
            if crit in ["1", "2"]:
                done = True
        if crit == "1":
            # par exemple si l attaque de bas (source.pc est 10, on attaque entre 5 et 15)
            degat = int(source.pc/2 + DX(source.pc)) + bonusArmes
        else:
            degat = source.pc + bonusArmes

        resistance = destination.pd + bonusDef
        for i in range(len(GB.sons_epee.bruits)//2):
            GB.sons_epee.play_sound()
        TB.textbox_output("Vous avez infligé "+str(max(0, degat-resistance)) +
                          " dégats, l'adversaire a encore " +
                          str(max(0, destination.pv-(max(0, degat-resistance)))
                              )+"/"+str(destination.pv_max)+" PV.")

    elif type_attaquant == 0:
        # on calcule le bonus d attaque lié aux armes
        bonusArmes = 0
        bonusDef = 0

        if (len(source.inventaire) != 0):
            for i in range(len(source.inventaire)):
                if type(source.inventaire[i]) == E.Equipement:
                    bonusArmes += source.inventaire[i].atk

            # on calcul les bonus de def lié aux defences
        if (len(destination.inventaire) != 0):
            for i in range(len(destination.inventaire)):
                if type(destination.inventaire[i]) == E.Equipement:
                    bonusDef += destination.inventaire[i].dfc

        degat = source.pc + bonusArmes
        resistance = destination.pd + bonusDef
        GB.sons_epee.play_sound()
        TB.textbox_output("Le "+str(source.classe)+" vous attaque et vous inflige "+(
            str(max(0, degat-resistance))) + " dégâts. Il vous reste " + str(max(0, destination.pv-max(0, (degat-resistance)))) + "/"+str(destination.pv_max) + " PV.")

    destination.pv -= max(0, (degat-resistance))
