import entite as Ett
import combat as Cbt


def intro():
    print("Bienvenue, aventurier, dans les Royaumes de l'Éclipse !\n\nAu seuil de cette aventure épique, vous êtes sur le point de vous embarquer pour des terres inconnues, où les destins se tissent dans les ombres et la lumière.\n\nPréparez-vous à plonger dans un monde de mystère et de magie, où chaque choix que vous ferez influencera le cours de l'histoire. Des terres sauvages aux cités florissantes, des donjons oubliés aux montagnes glacées, l'aventure vous attend à chaque tournant.\n\nAvant de commencer votre voyage, il est temps de forger votre propre destin. Créez votre personnage, choisissez votre race, votre classe et vos compétences, et préparez-vous à affronter les défis qui vous attendent. Votre courage, votre astuce et votre détermination seront vos meilleurs alliés dans cette quête pour la gloire et la fortune.\n\nL'aventure vous appelle, cher héros. Êtes-vous prêt à répondre à son appel et à laisser votre marque sur les Royaumes de l'Éclipse ?\n\n")

    nom = input("Veuillez entrer le nom de votre personnage\n\n")
    race = input(
        "Veuillez selectionner une race parmi :\n\n1 humain\n2 elfe\n3 orc\n\n")

    classe = input(
        "Veuillez selectionner une classe parmi :\n\n1 guerrier\n2 archer\n3 tank\n\n")

    # on créé un hero avec le X eme element de la liste des race/classes
    hero = Ett.Joueur(nom, Ett.listeClasse[int(
        classe)-1], Ett.listeRace[int(classe)-1])

    print("Vous vous réveillez dans une cellule sombre et humide, les murs de pierre émanant une froideur glaciale. Votre tête tourne, et vous vous rendez compte que vous avez été capturé. Avant même que vous puissiez rassembler vos pensées, des bruits de lutte retentissent à l'extérieur de votre cellule. Des cris, des grondements de métal et le son de pas pressés remplissent l'air, vous laissant avec un sentiment d'urgence.")
    print("\n")
    print("Soudain, la porte de votre cellule est forcée avec violence, révélant une scène chaotique. Des gardes en armure engagent le combat avec des assaillants masqués, créant une diversion parfaite pour votre évasion. Profitant de l'opportunité, vous vous précipitez hors de votre cellule et vous frayer un chemin à travers le chaos qui règne dans les couloirs obscurs du donjon.")
    print("\n")
    print("Dans le tumulte, vous parvenez à vous emparer de quelques armes et pièces d'équipement abandonnées par les combattants. Armé et prêt à tout, vous atteignez enfin l'extérieur du donjon, émergeant dans une clairière bordée d'une dense forêt.\n\nCependant, à peine avez-vous eu le temps de reprendre votre souffle que vous vous rendez compte que vous n'êtes pas seul. Un garde en uniforme, l'épée déjà tirée, émerge des ombres de la forêt, sa présence chargée d'hostilité. Il semble déterminé à vous ramener, et il n'hésitera pas à utiliser la force pour accomplir sa mission. Les échos de la lutte résonnent encore derrière vous, et vous réalisez que vous n'avez pas d'autre choix que de vous défendre")

    classeGardeRoyalIntro = Ett.Type("Garde Royal", 100, 5, 5, 10)

    gardeRoyal = Ett.Monstre(classeGardeRoyalIntro, Ett.humain)

    Cbt.bataille(hero, gardeRoyal)

    del (gardeRoyal)


intro()
