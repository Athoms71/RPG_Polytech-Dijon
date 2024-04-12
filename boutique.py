def vente(joueur, objet):
    if objet in joueur.inventaire:
        joueur.inventaire.remove(objet)
        joueur.argent += objet.prix


def achat(joueur, objet):
    if joueur.argent >= objet.prix:
        joueur.inventaire.append(objet)
        joueur.argent -= objet.prix
