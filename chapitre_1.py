import entite as Ett
import combat as Cbt
import equipement as E
import chapitre_0 as C0


def ch1():
    print("Après la confrontation avec le garde, vous décidez de prendre un repos bien mérité pour reprendre des forces. Vous trouvez un endroit sûr à l'abri des regards, où vous pouvez vous reposer sans craindre d'être découvert. La nuit tombe lentement, le ciel s'embrasant de teintes rouges et dorées alors que le soleil se couche à l'horizon.")
    print("\n")
    print("Pendant votre sommeil, des rêves troublants hantent votre esprit. Des visions de ténèbres et de lumière se mêlent dans un tourbillon de confusion, révélant des fragments d'une histoire oubliée et des énigmes mystérieuses. Vous entendez des voix murmurer dans l'obscurité, appelant votre nom et vous incitant à découvrir la vérité cachée dans les Royaumes de l'Éclipse.")
    print("\n")
    print("Au matin, vous vous réveillez avec un sentiment d'urgence brûlant dans votre poitrine. Vous savez maintenant que votre destin est lié à une quête plus grande que vous, une quête pour trouver les Artefacts de l'Éclipse, des objets de pouvoir ancien qui pourraient changer le cours de la guerre entre la lumière et les ténèbres.")
    print("\n")
    print("Votre première tâche est de retrouver la Carte des Royaumes, un artefact légendaire qui révèle la localisation des autres Artefacts de l'Éclipse. On dit que la carte est cachée dans les ruines d'une ancienne cité, perdue depuis des siècles dans les Terres Éloignées à l'est.")
    print("\n")
    print("Déterminé à accomplir votre mission, vous vous levez et vous mettez en route vers les Terres Éloignées, votre cœur battant avec l'excitation de l'aventure à venir et la détermination de réaliser votre destinée.")
    print("\n")
    print("Alors que vous cheminez à travers les Terres Éloignées en quête de la Carte des Royaumes, vous tombez sur une scène troublante : un groupe de voyageurs sans défense est attaqué par des brigands impitoyables. Leurs cris de détresse percent le silence de la forêt, vous appelant à l'action.")
    print("\n")
    print("Option 1 : Obtenir de l'Équipement :")
    print("Vous décidez d'intervenir pour aider les voyageurs en détresse, mais avant de vous précipiter dans la bataille, vous remarquez un sac abandonné près du sentier. À l'intérieur, vous trouvez quelques pièces d'or et une épée étincelante, probablement abandonnées par un voyageur pris au piège. Vous pourriez garder l'équipement pour vous-même, vous offrant un avantage supplémentaire dans votre quête.")
    print("\n")
    print("Option 2 : Augmenter votre Karma :")
    print("D'un autre côté, vous pourriez choisir d'ignorer le sac d'équipement et de vous concentrer sur l'aide aux voyageurs. En intervenant rapidement, vous pourriez sauver des vies innocentes et gagner le respect et la gratitude des gens que vous rencontrez. Bien que cela puisse vous coûter un avantage temporaire, votre conscience serait claire et votre karma augmenterait.")
    print("\n")
    choix = str(input(
        "Quelle option choisissez vous ?\n\n1 : Obtenir de l'Équipement\n2 : Augmenter votre Karma"))
    if choix == 1:
        C0.hero.karma = - 1
        bouclier = E.Equipement("bouclier", 0, 15, 10, 5, "main_gauche")
        potion = E.Consommable("Potion de Soin", 0, 0, 10, 10, "soin")
    if choix == 2:
        C0.hero.karma = + 5

    if C0.hero.karma > 0:
        print("Le héros, dans la lueur tamisée de la forêt, se tenait là, respirant encore avec le poids de la liberté fraîchement acquise. Son souffle s'accélérait avec l'adrénaline de la bataille récente. À travers les arbres, une voix mystérieuse et profonde s'éleva, portée par une brise légère.")
        print("\n")
        print("''Bravo, valeureux héros'', résonna la voix, empreinte d'une solennité antique. ''Tu as montré un courage exceptionnel en te dressant contre l'oppression et en offrant ton aide à ceux dans le besoin. Les dieux eux-mêmes ont pris note de ton altruisme et de ta compassion envers tes semblables.''")
        print("\n")
        print("Les feuilles bruissaient doucement, comme si la forêt elle-même applaudissait la bravoure du héros.")
        print("\n")
        print("''Tu es l'élu, celui choisi pour restaurer l'équilibre dans ce monde tourmenté. Les ténèbres menacent de l'engloutir, mais avec ta force et ta détermination, tu peux apporter la lumière là où règne l'ombre. Sache que tu n'es pas seul dans cette quête. Des alliés se présenteront à toi, des épreuves te testeront, mais à chaque pas, sache que ta vertu guidera tes choix.''")
        print("\n")
        print("")
        print("\n")
        print("La voix sembla se fondre dans le murmure de la forêt, laissant le héros avec un sentiment de responsabilité mêlé d'espoir. Il se tint là, absorbant les paroles du destin, prêt à embrasser sa nouvelle mission avec tout le courage et la compassion dont il était capable.")
        print("\n")
    if C0.hero.karma <= 0:
        print("''Tu as commis des erreurs, mais les dieux, dans leur clémence infinie, te tendent maintenant une chance de te racheter. Malgré ta décision égoïste, ils voient encore en toi le potentiel de changer et de faire le bien. Tu as été choisi pour une mission qui dépasse tes propres désirs, une chance de réparer les torts que tu as causés.''")
        print("\n")
        print("La voix résonnait avec une douceur empreinte de patience, comme une main tendue dans l'obscurité.")
        print("\n")
        print("''Accepte cette opportunité avec humilité et reconnaissance. Utilise-la pour rectifier tes erreurs passées et pour trouver la rédemption dans les actions futures. Les dieux ne t'abandonneront pas, même lorsque tu doutes de toi-même. Reste fidèle à cette nouvelle voie qui s'ouvre à toi, et peut-être, un jour, trouveras-tu la paix que tu cherches.''")
        print("\n")

    print("Inspiré par les paroles mystiques de la voix de la forêt, le héros sentit une flamme nouvelle s'allumer en lui. Son cœur, autrefois alourdi par le poids du doute et des erreurs passées, s'éleva maintenant avec un sentiment de dessein et de détermination. Les mots résonnaient en lui, réaffirmant sa foi en sa capacité à faire une différence dans ce monde troublé.")
    print("\n")
    print("Ses pas résonnèrent sur le sol de la forêt alors qu'il se préparait à l'aventure qui l'attendait. Son esprit s'embrasa d'une volonté féroce, prêt à affronter les défis et les dangers qui se dresseraient sur son chemin. Guidé par la voix de la destinée, il leva les yeux vers les cieux étoilés, où l'ombre menaçante de l'éclipse s'étendait.")
    print("\n")
