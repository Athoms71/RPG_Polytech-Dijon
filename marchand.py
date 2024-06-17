import entite as Ett
import equipement as E
import textbox as TB
import pygame


def ouvertureDeLaBoutique(joueur: Ett.Joueur, honnetete: float, listeAchat: list = []):
    """Attention, liste achat doit estre de 5 elements ou moins !"""
    pygame.mixer.music.load("./sounds/marchand_theme.mp3")
    done = False
    stockMarchand = listeAchat
    TB.textbox_output("Vous croisez un marchand itinérant.")
    while not done:
        choix = TB.textbox_input(
            "Voulez vous vendre ou acheter des objets ?@@- 1 : Vendre@- 2 : Acheter@- 3 : Partir")
        if (choix == "1"):  # Vendre
            choixType = (TB.textbox_input(
                "Voulez vous vendre?@@- 1 : des consommables@- 2 : De l'équipement"))
            j = 0

            if (choixType == "1"):  # on vend des consommables
                liste_equip_a_afficher = ""
                liste_equipements_vente = []  # liste des equipements que l'on peut vendre
                for i in range(len(joueur.inventaire)):
                    if joueur.inventaire[i].cat in ["soin", "attaque", "defense"]:
                        j += 1
                        liste_equip_a_afficher += (str(j) + " - "+str(joueur.inventaire[i].cat) +
                                                   " : "+str(joueur.inventaire[i].nom) +
                                                   " : "+str(joueur.inventaire[i].prix*honnetete) + " PO@")
                        liste_equipements_vente.append(joueur.inventaire[i])
                if (len(liste_equip_a_afficher)) == 0:
                    TB.textbox_output(
                        "Vous ne possédez rien de valeur dans cette catégorie :)")
                else:
                    TB.textbox_output("Lequel souhaitez vous vendre ?")
                    choixVente = TB.textbox_input(str(liste_equip_a_afficher))
                    if choixVente in ["1", "2", "3", "4", "5", "6",]:
                        # normalisation du choi aux bons indices
                        choixVente = int(choixVente) - 1
                        # on verifie que l'on ne vend pas un consommable d indice trop grand
                        if choixVente < len(liste_equipements_vente):
                            for i in range(len(joueur.inventaire)):
                                if joueur.inventaire[i].nom == liste_equipements_vente[choixVente].nom:
                                    joueur.argent += joueur.inventaire[i].prix
                                    TB.textbox_output(
                                        "vous avez vendu : "+str(joueur.inventaire.pop(i).nom))
                                    break

            if (choixType == "2"):  # on vend de l'équipement
                liste_equip_a_afficher = ""
                liste_equipements_vente = []  # liste des equipements que l'on peut vendre
                for i in range(len(joueur.inventaire)):
                    if joueur.inventaire[i].cat in ["main_droite", "main_gauche", "tete", "torse", "jambe", "pied"]:
                        j += 1
                        liste_equip_a_afficher += (str(j) + " - "+str(joueur.inventaire[i].cat) +
                                                   " : "+str(joueur.inventaire[i].nom) +
                                                   " : "+str(joueur.inventaire[i].prix*honnetete) + " PO@")
                        liste_equipements_vente.append(joueur.inventaire[i])
                if (len(liste_equip_a_afficher)) == 0:
                    TB.textbox_output(
                        "Vous ne possédez rien de valeur dans cette catégorie :)")
                else:
                    TB.textbox_output("Lequel souhaitez vous vendre ?")
                    choixVente = TB.textbox_input(str(liste_equip_a_afficher))
                    if choixVente in ["1", "2", "3", "4", "5", "6",]:
                        # normalisation du choi aux bons indices
                        choixVente = int(choixVente) - 1
                        # on verifie que l'on ne vend pas un consommable d indice trop grand
                        if choixVente < len(liste_equipements_vente):
                            for i in range(len(joueur.inventaire)):
                                if joueur.inventaire[i].nom == liste_equipements_vente[choixVente].nom:
                                    joueur.argent += joueur.inventaire[i].prix
                                    TB.textbox_output(
                                        "vous avez vendu : "+str(joueur.inventaire.pop(i).nom))
                                    break

                    else:
                        TB.textbox_output(
                            "Le marchand vous regarde bizzarement, il ne semble pas comprendre votre réponse")
            elif choix not in ["1", "2"]:
                TB.textbox_output(
                    "Le marchand vous regarde bizzarement, il ne semble pas comprendre votre réponse")

        if choix == "2":
            if len(stockMarchand) == 0:
                TB.textbox_output(
                    "Le marchand n'a rien à vous proposer à acheter")
            else:
                TB.textbox_output(
                    "Le marchand vous sort des equipements, lequel voudriez vous acheter ?")
                aAfficherMarchand = "Vous avez " + \
                    str(joueur.argent)+" PO, le marchand vous propose :"
                for i in range(len(stockMarchand)):
                    aAfficherMarchand += "@- " + \
                        str(i+1)+" : " + \
                        str(stockMarchand[i].nom) + \
                        " -> "+str(stockMarchand[i].prix*honnetete)+" PO"
                choixAchat = TB.textbox_input(aAfficherMarchand)
                if choixAchat in ["1", "2", "3", "4", "5"]:
                    choixAchat = int(choixAchat)-1
                    if choixAchat < len(stockMarchand):
                        if stockMarchand[choixAchat].prix*honnetete <= joueur.argent:
                            joueur.argent -= stockMarchand[choixAchat].prix*honnetete
                            obt_objet(stockMarchand.pop(i), joueur)
                        else:
                            TB.textbox_output("Vous n avez pas assez d'argent")
                    else:
                        TB.textbox_output(
                            "Le marchand vous regarde bizzarement, il ne semble pas comprendre votre réponse")
                else:
                    TB.textbox_output(
                        "Le marchand vous regarde bizzarement, il ne semble pas comprendre votre réponse")

        elif choix == "3":  # partir
            TB.textbox_output("Vous quittez le marchand.")
            done = True

        elif choix not in ["1", "2", "3"]:
            TB.textbox_output(
                "Le marchand vous regarde bizzarement, il ne semble pas comprendre votre réponse")


def venteObligatoireEquipement(joueur: Ett.Joueur, equipement1: E.Equipement, equipement2: E.Equipement):
    """propose de vendre un des deux objets mis en parametre, le vend puis le retire de l'inventaire"""
    TB.textbox_output(
        "Il semblerait que vous ayez deux equipement équipés sur la meme partie du corps, veuillez en vendre un des deux.")
    done = False
    while (not done):
        choix = (TB.textbox_input("lequel de ces deux equipement souhaitez vous ventre ?@@-1 : " +
                                  equipement1.nom+" -> "+str(equipement1.prix)+" Pièces d'or@-2 : "+equipement2.nom+" -> "+str(equipement2.prix)+" Pièces d'or"))
        if choix in ["1", "2"]:
            done = True

    if choix == "1":
        for i in range(len(joueur.inventaire)):
            if joueur.inventaire[i].nom == equipement1.nom:
                joueur.argent += equipement1.prix
                joueur.inventaire.pop(i)
                break

    if choix == "2":
        for i in range(len(joueur.inventaire)):
            if joueur.inventaire[i].nom == equipement2.nom:
                joueur.argent += equipement2.prix
                joueur.inventaire.pop(i)
                break


def venteObligatoireConsommable(joueur: Ett.Joueur):
    TB.textbox_output(
        "il semblerait que vous ayez trop de consommables dans votre inventaire, veuillez en vendre :")
    liste_conso_joueur = joueur.inventaire
    if len(liste_conso_joueur) == 6:

        choix_vente = int(TB.textbox_input("Lequel de ces consommables souhaitez vous vendre parmis :@- 1 :" +
                                           str(liste_conso_joueur[0].nom)+" -> " +
                                           str(liste_conso_joueur[0].prix)+" PO@- 2 :" +
                                           str(liste_conso_joueur[1].nom)+" -> " +
                                           str(liste_conso_joueur[1].prix)+" PO@- 3 :" +
                                           str(liste_conso_joueur[2].nom)+" -> " +
                                           str(liste_conso_joueur[2].prix)+" PO@- 4 :" +
                                           str(liste_conso_joueur[3].nom)+" -> " +
                                           str(liste_conso_joueur[3].prix)+" PO@- 5 :" +
                                           str(liste_conso_joueur[4].nom)+" -> " +
                                           str(liste_conso_joueur[4].prix)+" PO@- 6 :" +
                                           str(liste_conso_joueur[5].nom)+" -> " +
                                           str(liste_conso_joueur[5].prix)+" PO"))-1

        for i in range(len(joueur.inventaire)):
            if joueur.inventaire[i].nom == liste_conso_joueur[choix_vente].nom:
                joueur.argent += liste_conso_joueur[choix_vente].prix
                joueur.inventaire.pop(i)
                break


def obt_objet(objet: E.Equipement | E.Consommable, joueur: Ett.Joueur):
    TB.textbox_output("Vous avez obtenu : "+str(objet.nom))
    if type(objet) == E.Consommable:
        if (len(Ett.Joueur.lister_inventaire_consommable(joueur)) <= 5):
            joueur.inventaire.append(objet)
        else:
            venteObligatoireConsommable(joueur)
        pass

    if type(objet) == E.Equipement:
        ttVaBienPourlemoment = True
        for i in range(len(joueur.inventaire)):

            if objet.cat == joueur.inventaire[i].cat:
                ttVaBienPourlemoment = False
                break
        joueur.inventaire.append(objet)

        if (not ttVaBienPourlemoment):
            venteObligatoireEquipement(joueur, joueur.inventaire[i], objet)
