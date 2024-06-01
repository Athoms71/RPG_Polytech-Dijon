import entite as Ett
import combat as Cbt
import equipement as E
import textbox as TB


def intro():
    TB.textbox_output(
        "Bonjour, avant de comencer, nous vous proposons un petit didacticiel.@@Pour passer à la boite de texte suivante, appuyez sur n importe quelle touche.@@@@@appuyez pour continuer")
    TB.textbox_output(
        "Bien joué, continuez comme ça !@@@@@@@appuyez pour continuer")
    done = 0
    while not done:
        if (TB.textbox_input("Pour entrer du texte, une boite de dialogue vierge va apparaitre, tu pourra y entre ta réponse ou ce que tu souhaite communiquer puis appuyer sur 'entrer'pour valider ta réponse. les questions seront formalisées comme suit :@Avez vous compris ?@- 1 : Oui@- 2 : Non@(vous devrez écrir dans la boite de texte vierge qui va aparaitre '1' pour répondre 'oui' et '2' pour répondre 'Non').@appuyez pour continuer") == "1"):
            done = 1
            break
        TB.textbox_output(
            "Quand cette boite de dialogue disparaitera ,  écrivez'1' pour repondre 'oui', appuyer, pour 'non',  écrivez 2. Puis appuyez sur 'entrer' pour valider@@@@@@appuyez pour continuer")
    TB.textbox_output(
        "Bien joué, continuez comme ça !@@@@@@@appuyez pour continuer")
    TB.textbox_output("Bienvenue aventurier, dans les Royaumes de l'Éclipse !@Au seuil de cette aventure épique, vous êtes sur le point d'embarquer pour des terres inconnues, où le destin se tisse entre les ombres et la lumière.")
    TB.textbox_output("Préparez-vous à plonger dans un monde de mystère et de magie, où chaque choix que vous ferez influencera le cours de l'histoire. Des terres sauvages aux cités florissantes, des donjons oubliés aux montagnes glacées, l'aventure vous attend à chaque tournant.")
    TB.textbox_output("Avant de commencer votre voyage, il est temps de forger votre propre destin. Créez votre personnage, choisissez votre race, votre classe et vos compétences, et préparez-vous à affronter les défis qui vous attendent. Votre courage, votre astuce et votre détermination seront vos meilleurs alliés dans cette quête pour la gloire et la fortune.")
    TB.textbox_output(
        "L'aventure vous appelle, cher héros. Êtes-vous prêt à répondre à son appel et à laisser votre marque sur les Royaumes de l'Éclipse ?")

    nom = TB.textbox_input("Veuillez entrer le nom de votre personnage : ")
    race = TB.textbox_input(
        "Veuillez selectionner une race parmi :@- 1 : humain@- 2 : elfe@- 3 : orc")
    classe = TB.textbox_input(
        "Veuillez selectionner une classe parmi :@@1 guerrier@2 archer@3 tank@@")

    # on crée un hero avec le X eme element de la liste des races/classes
    hero = Ett.Joueur(nom, Ett.liste_classe[int(
        classe)-1], Ett.liste_race[int(race)-1])
    TB.textbox_output("Vous etes : "+hero.nom+", de la race des "+hero.race+", vous etes un futur " +
                      hero.classe+" dont on racontera l'hisoire pendant des générations !")
    TB.textbox_output("Vous vous réveillez dans une cellule sombre et humide, une froideur glaciale émanant des murs de pierre qui vous entourent. Votre tête tourne, et vous vous rendez compte que vous avez été capturé. Avant même que vous puissiez rassembler vos pensées, des bruits de lutte retentissent à l'extérieur de votre cellule. Des cris, des grondements de métal et le son de pas pressés remplissent l'air, vous laissant avec un sentiment d'urgence.")
    TB.textbox_output("Soudain, la porte de votre cellule est forcée avec violence, révélant une scène chaotique. Des gardes en armure engagent le combat avec des assaillants masqués, créant une diversion parfaite pour votre évasion. Profitant de l'opportunité, vous vous précipitez hors de votre cellule et vous frayez un chemin à travers le chaos qui règne dans les couloirs obscurs du donjon.")
    TB.textbox_output("Dans le tumulte, vous parvenez à vous emparer de quelques armes et pièces d'équipement abandonnées par les combattants. Armé et prêt à tout, vous atteignez enfin l'extérieur du donjon, émergeant dans une clairière bordée d'une dense forêt.@@Cependant, à peine avez-vous eu le temps de reprendre votre souffle que vous vous rendez compte que vous n'êtes pas seul. Un garde en uniforme, l'épée déjà tirée, émerge des ombres de la forêt, sa présence chargée d'hostilité.")
    TB.textbox_output("Il semble déterminé à vous ramener, et il n'hésitera pas à utiliser la force pour accomplir sa mission. Les échos de la lutte résonnent encore derrière vous, et vous réalisez que vous n'avez pas d'autre choix que de vous défendre...")

    TB.textbox_output("Dans un échange de coups féroces, vous parvenez à surmonter le garde, le forçant à reculer sous la puissance de vos attaques bien placées. Avec un ultime effort, il tombe à genoux, désarmé et vaincu. Le silence retombe sur la clairière, brisé seulement par le souffle haletant de vos efforts et le bruissement des feuilles dans le vent.")
    TB.textbox_output("Alors que vous vous éloignez de la clairière, le soleil déclinant jette des reflets dorés à travers les feuilles, éclairant le chemin devant vous d'une lueur chaleureuse et réconfortante. Vous ne savez pas ce que l'avenir vous réserve, mais une chose est sûre : vous êtes prêt à affronter chaque défi avec courage et détermination, car dans les Royaumes de l'Éclipse, seuls les plus forts et les plus audacieux survivent.")
    TB.textbox_output("Votre aventure ne fait que commencer. Êtes-vous prêt à laisser votre empreinte sur ce monde tumultueux et à découvrir les secrets qui se cachent dans ses recoins les plus sombres ?")


def speedrun_dev():
    # voici thomas, il est cool

    hero = Ett.Joueur("thomas le puissant",
                      Ett.liste_classe[1], Ett.liste_race[1])
    # TB.textbox_output("Vous etes : "+hero.nom+", de la race des "+hero.race+", vous etes un futur " +hero.classe+" dont on racontera l'hisoire pendant des générations !")
    # creation du gare
    type_garde_royal_intro = Ett.Type("Garde Royal", 5, 5, 3)
    garde_royal = Ett.Monstre(type_garde_royal_intro, Ett.humain)
    # obtention de l equipement :
    pSoin = E.Consommable("Petite potion de soin", 0, 0, 5, 5, 5, "soin")
    hero.inventaire.append(pSoin)
    gpSoin = E.Consommable("Grosse popo", 0, 0, 700, 5, 5, "soin")
    hero.inventaire.append(gpSoin)
    epee = E.Equipement("epee", 35, 0, 5, 5, "main_droite")
    hero.inventaire.append(epee)
    Cbt.bataille(hero, garde_royal)

    del (garde_royal)

    # obtention de l equipement :
    epee = E.Equipement("epee", 10, 0, 5, 5, "main_droite")
    hero.inventaire.append(epee)


# intro()


speedrun_dev()
