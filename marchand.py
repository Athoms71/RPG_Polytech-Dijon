import entite as Ett
import equipement as E
import textbox as TB


def ouvertureDeLaBoutique(joueur: Ett.Joueur, honnetete: float):
    done = False
    while not done:
        if (TB.textbox_input("Voulez vous vendre des objets ?@@- 1 : Oui@- 2 : Non") == "1"):
            choixType = (TB.textbox_input(
                "Voulez vous vendre?@@- 1 : des consommables@- 2 : De l'équipement"))
            j = 0
            if (choixType == "2"):
                TB.textbox_output("Lequel souhaitez vous vendre ?")
                liste_equip_a_afficher = ""
                for i in range(len(joueur.inventaire)):
                    if joueur.inventaire[i].cat in ["main_droite", "main_gauche", "tete", "torse", "jambe", "pied"]:
                        j += 1
                        liste_equip_a_afficher += (str(j) + " - "+str(joueur.inventaire[i].cat) +
                                                   " : "+str(joueur.inventaire[i].nom) +
                                                   " : "+str(joueur.inventaire[i].prix*honnetete) + " PO@")
                choixVente = TB.textbox_input(str(liste_equip_a_afficher))
                if choixVente in ["1", "2", "3", "4", "5", "6",]:
                    choixVente = int(choixVente) - 1
                    if choixVente <= len(joueur.inventaire):
                        joueur.argent += joueur.inventaire[choixVente].prix
                        joueur.inventaire.pop(choixVente)
            if (choixType == "1"):
                TB.textbox_output("Lequel souhaitez vous vendre ?")
                liste_equip_a_afficher = ""
                for i in range(len(joueur.inventaire)):
                    if joueur.inventaire[i].cat in ["soin", "attaque", "defense"]:
                        j += 1
                        liste_equip_a_afficher += (str(j) + " - "+str(joueur.inventaire[i].cat) +
                                                   " : "+str(joueur.inventaire[i].nom) +
                                                   " : "+str(joueur.inventaire[i].prix*honnetete) + " PO@")
                choixVente = TB.textbox_input(str(liste_equip_a_afficher))
                if choixVente in ["1", "2", "3", "4", "5", "6",]:
                    choixVente = int(choixVente) - 1
                    if choixVente <= len(joueur.inventaire):
                        joueur.argent += joueur.inventaire[choixVente].prix
                        joueur.inventaire.pop(choixVente)

        else:
            done = True


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
        "il semblerait que vous ayez trop de consommables dans dans votre inventaire, veuillez en vendre :")
    liste_conso_joueur = []
    for i in range(len(joueur.inventaire)):
        if (type(joueur.inventaire[i]) == E.Consommable):
            liste_conso_joueur.append(joueur.inventaire[i])
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
