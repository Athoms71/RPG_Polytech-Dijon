import entite as Ett
import equipement as E
import textbox as TB


def ouvertureDeLaBoutique(joueur: Ett.Joueur, honnetete: int):
    if (TB.textbox_input("Voulez vous vendre des objets ?@@- 1 : Oui@- 2 : Non") == "1"):
        choixType = (TB.textbox_input(
            "Voulez vous vendre?@@- 1 : des consommables@- 2 : De l'équipement") == "1")
        if choixType == "1":
            pass
        if choixType == "2":
            pass

    else:
        pass


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


def obt_objet(objet: E.Equipement | E.Consommable, joueur: Ett.Joueur):
    if type(objet) == E.Consommable:
        if (len(Ett.Joueur.lister_inventaire_consommable()) <= 5):
            joueur.inventaire.append(objet)
        else:
            venteObligatoireConsommable(joueur.inventaire)
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
