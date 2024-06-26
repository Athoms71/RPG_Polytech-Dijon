import entite as Ett
import textbox as TB
import operation_fichier as OF
import os
import pygame
from pygame.locals import *
import pygame_widgets
from pygame_widgets.button import Button
import combat as C
import marchand as M
import equipement as E


def fontaine(heros: Ett.Joueur):
    '''Soigne le héros spécifié en paramètre'''
    TB.textbox_output(
        "Vous tombez face à une fontaine, vous décidez de boire son eau, et vous sentez votre énergie vitale vous revenir...")
    heros.pv = heros.pv_max
    TB.textbox_output(
        "Vous avez été soigné de vos blessures :@"+str(heros.pv)+"/"+str(heros.pv_max)+"PV")


def dimensions_ecran():
    '''Récupère les dimensions de l'écran du joueur et les retourne dans un tuple (w,h)'''
    screen_info = pygame.display.Info()  # Récupère les infos de l'écran
    screen_width = screen_info.current_w
    screen_height = screen_info.current_h
    return (screen_width, screen_height)


def check_events():
    '''Regarde les évènements dans la queue et réalise des actions en fonction des conditions (touches, état des variables...)'''
    global ETAT
    global GAME_RUNNING
    global DICT_VAR
    events = pygame.event.get()
    for event in events:
        dicKeys = pygame.key.get_pressed()
        if event.type == QUIT or dicKeys[K_TAB]:
            fin_fenetre()
        if dicKeys[K_ESCAPE] and ETAT == "jeu":     #
            changement_affichage()
            OF.save(DICT_VAR)
            GAME_RUNNING = False
            pygame.mixer.music.load("./sounds/title_theme.mp3")
            pygame.mixer.music.play(-1)
    pygame_widgets.update(events)
    pygame.display.flip()


def fade(mode: int, ch_image: str, text: str = ""):
    '''Définit le fondu à créer :\n
        - 1 : fade in\n
        - -1 : fade out'''
    global BLACK
    # On récupère les dimensions de l'écran
    screen_width, screen_height = dimensions_ecran()
    # On vérifie que le chemin spécifié est valide
    if ch_image != "":
        image = pygame.image.load(ch_image)
        image = pygame.transform.scale(image, (screen_width, screen_height))
    # Render du texte à afficher pour le nom des chapitres
    font = pygame.font.Font("./font/VecnaBold-4YY4.ttf", 100)
    texte = font.render(text, True, WHITE)
    texte_rect = texte.get_rect(center=(window_width//2, window_height//2))
    # Création du fade
    fade = pygame.Surface((screen_width, screen_height))
    fade.fill(BLACK, (0, 0, window_width, window_height))
    # Fade in de l'image spécifiée
    if mode == 1:
        opacity = 300
        for r in range(300):
            opacity -= 1
            fade.set_alpha(opacity)
            screen.blit(image, (0, 0))
            screen.blit(texte, texte_rect)
            screen.blit(fade, (0, 0))
            pygame.display.update()
            pygame.time.wait(5)
            check_events()
    # Fade out de l'image spécifiée
    elif mode == -1:
        opacity = 0
        for r in range(300):
            opacity += 1
            fade.set_alpha(opacity)
            screen.blit(image, (0, 0))
            screen.blit(texte, texte_rect)
            screen.blit(fade, (0, 0))
            pygame.display.update()
            pygame.time.wait(5)
            check_events()
    # Délai pour lire le texte
    if text != "":
        pygame.time.wait(2500)


def fin_fenetre():
    '''Ferme la fenêtre de jeu'''
    global RUNNING
    RUNNING = False
    pygame.quit()
    pygame.mixer.quit()
    quit()


def changement_affichage():
    '''Change d'affichage entre l'écran titre et le jeu'''
    global ETAT
    if ETAT == "ecran_titre":
        ETAT = "jeu"
    elif ETAT == "jeu":
        ETAT = "ecran_titre"
        fade(1, "./img/chemin_fond_flou.png")


def nouvelle_partie():
    '''Crée une nouvelle partie en effaçant une potentielle sauvegarde déjà existante'''
    global AVANCEMENT
    if os.path.exists("save.txt"):
        os.remove("save.txt")
    AVANCEMENT = 0
    changement_affichage()


def continuer_partie():
    '''Charge la sauvegarde et met à jour les variables du jeu'''
    global DICT_VAR
    global AVANCEMENT
    global HEROS
    if os.path.exists("save.txt"):
        HEROS = Ett.Joueur("", Ett.guerrier, Ett.humain)
        DICT_VAR = OF.load()
        HEROS.nom = DICT_VAR["nom_joueur"]
        match DICT_VAR["classe_joueur"]:
            case "guerrier":
                HEROS.classe = Ett.guerrier.nom
                HEROS.pv_max = Ett.guerrier.pv_max
                HEROS.pc = Ett.guerrier.pc
                HEROS.pd = Ett.guerrier.pd
            case "archer":
                HEROS.classe = Ett.archer.nom
                HEROS.pv_max = Ett.archer.pv_max
                HEROS.pc = Ett.archer.pc
                HEROS.pd = Ett.archer.pd
            case "tank":
                HEROS.classe = Ett.tank.nom
                HEROS.pv_max = Ett.tank.pv_max
                HEROS.pc = Ett.tank.pc
                HEROS.pd = Ett.tank.pd
        match DICT_VAR["race_joueur"]:
            case "humain":
                HEROS.race = Ett.humain.nom
                HEROS.pv_max += Ett.humain.pv_max
                HEROS.pc += Ett.humain.pc
                HEROS.pd += Ett.humain.pd
            case "elfe":
                HEROS.race = Ett.elfe.nom
                HEROS.pv_max += Ett.elfe.pv_max
                HEROS.pc += Ett.elfe.pc
                HEROS.pd += Ett.elfe.pd
            case "orc":
                HEROS.race = Ett.orc.nom
                HEROS.pv_max += Ett.orc.pv_max
                HEROS.pc += Ett.orc.pc
                HEROS.pd += Ett.orc.pd
        for elt in DICT_VAR["inventaire_joueur"]:
            if len(elt) == 6:
                new_conso = E.Consommable(elt[0], int(elt[1]), int(
                    elt[2]), int(elt[3]), int(elt[4]), elt[5])
            elif len(elt) == 5:
                new_conso = E.Equipement(elt[0], int(elt[1]), int(
                    elt[2]), int(elt[3]), elt[4])
            HEROS.inventaire.append(new_conso)
        HEROS.pv = int(DICT_VAR["pv_joueur"])
        HEROS.argent = int(DICT_VAR["argent_joueur"])
        AVANCEMENT = int(DICT_VAR["avancement"])
        changement_affichage()


def dict_var_update(dict_var: dict, avancement: int):
    '''Sauvegarde les valeurs des différentes variables dans le dictionnaire de sauvegarde'''
    global HEROS
    dict_var["nom_joueur"] = HEROS.nom
    dict_var["classe_joueur"] = HEROS.classe
    dict_var["race_joueur"] = HEROS.race
    for elt in HEROS.inventaire:
        list_temp = []
        list_temp.append(elt.nom)
        list_temp.append(elt.atk)
        list_temp.append(elt.dfc)
        if type(elt) == E.Consommable:
            list_temp.append(elt.heal)
        list_temp.append(elt.prix)
        list_temp.append(elt.cat)
        dict_var["inventaire_joueur"].append(list_temp)
    dict_var["pv_joueur"] = HEROS.pv
    dict_var["argent_joueur"] = HEROS.argent
    dict_var["avancement"] = avancement
    return dict_var


def ecran_titre():
    '''Affiche l'écran titre'''
    global ICON
    button_font = pygame.font.Font(
        "./font/VecnaBold-4YY4.ttf", 45)
    title_font_size = 200
    title_font = pygame.font.Font(
        "./font/VecnaBold-4YY4.ttf", title_font_size)
    title_text = title_font.render(
        "Les Royaumes de l'Éclipse", True, WHITE)
    title_rect = title_text.get_rect()
    title_max_rect = pygame.Rect(
        150+window_height//5, 100, window_width-(window_width//5+100), window_height//5)
    while title_rect.w > title_max_rect.w or title_rect.h > title_max_rect.h:
        title_font_size -= 5
        title_font = pygame.font.Font(
            "./font/VecnaBold-4YY4.ttf", title_font_size)
        title_text = title_font.render(
            "Les Royaumes de l'Éclipse", True, WHITE)
        title_rect = title_text.get_rect()
    button_new = Button(
        screen,
        window_width//2-button_w//2,
        2*window_height//5,
        button_w,
        button_h,
        text="Nouvelle partie",
        font=button_font,
        textColour=(0, 0, 0),
        fontSize=60,
        margin=5,
        inactiveColour=(255, 255, 255, 128),
        hoverColour=(210, 210, 210),
        pressedColour=(180, 180, 180),
        radius=10,
        onClick=nouvelle_partie
    )
    button_continue = Button(
        screen,
        window_width//2-button_w//2,
        2*window_height//5+button_h+50,
        button_w,
        button_h,
        text="Continuer",
        font=button_font,
        textColour=(0, 0, 0),
        fontSize=60,
        margin=5,
        inactiveColour=(255, 255, 255),
        hoverColour=(210, 210, 210),
        pressedColour=(180, 180, 180),
        radius=10,
        onClick=continuer_partie
    )
    button_quit = Button(
        screen,
        window_width//2-button_w//2,
        2*window_height//5+2*(button_h+50),
        button_w,
        button_h,

        text="Quitter",
        font=button_font,
        textColour=(0, 0, 0),
        fontSize=60,
        margin=5,
        inactiveColour=(255, 255, 255, 128),
        hoverColour=(210, 210, 210),
        pressedColour=(180, 180, 180),
        radius=10,
        onClick=fin_fenetre
    )
    background = pygame.image.load(
        "img/chemin_fond_flou.png").convert_alpha()
    background = pygame.transform.scale(
        background, (window_width, window_height))
    ICON = pygame.transform.scale(
        ICON, (window_height//5, window_height//5))
    screen.blit(background, (0, 0))
    screen.blit(title_text, (150+window_height//5, window_height//5-50))
    screen.blit(ICON, (100, 100))
    check_events()


def jeu():
    '''Affiche le chapitre du jeu en fonction de l'avancement dans celui-ci et si le joueur continue ou recommence une partie'''
    global ETAT
    global GAME_RUNNING
    global AVANCEMENT
    global DICT_VAR
    global HEROS
    GAME_RUNNING = True
    fade(-1, "./img/chemin_fond_flou.png")
    while GAME_RUNNING:
        match AVANCEMENT:
            case 0:
                AVANCEMENT, HEROS = chapitre0()
            case 1:
                pygame.mixer.music.load("./sounds/ch1_music.mp3")
                pygame.mixer.music.play(-1)
                fade(1, "./img/burning_village.png",
                     "Chapitre 1 : L'aube de l'Éclipse")
                fade(-1, "./img/burning_village.png")
                fade(1, "./img/burning_village.jpg")
                AVANCEMENT, HEROS = chapitre1()
                fade(-1, "./img/chemin_pierre_runes.jpg")
            case 2:
                pygame.mixer.music.load("./sounds/ch2_music.mp3")
                pygame.mixer.music.play(-1)
                fade(1, "./img/ruines_dans_foret.jpg",
                     "Chapitre 2 : Les ruines oubliées")
                fade(-1, "./img/ruines_dans_foret.jpg")
                fade(1, "./img/ruines_dans_foret.png")
                AVANCEMENT, HEROS = chapitre2()
                fade(-1, "./img/book_in_ruins.jpg")
            case 3:
                pygame.mixer.music.load("./sounds/ch3_music.mp3")
                pygame.mixer.music.play(-1)
                fade(1, "./img/foret_sombre.png",
                     "Chapitre 3 : La forêt des murmures")
                fade(-1, "./img/foret_sombre.png")
                fade(1, "./img/foret_sombre.jpg")
                AVANCEMENT, HEROS = chapitre3()
                fade(-1, "./img/foret_sombre.jpg")
            case 4:
                pygame.mixer.music.load("./sounds/ch4_music.mp3")
                pygame.mixer.music.play(-1)
                fade(1, "./img/fond ch4.jpg",
                     "Chapitre 4 : La cité sous la lune")
                fade(-1, "./img/fond ch4.jpg")
                fade(1, "./img/fond ch4.jpg")
                AVANCEMENT, HEROS = chapitre4()
                fade(-1, "./img/fond ch4.jpg")
            case 5:
                pygame.mixer.music.load("./sounds/ch5_music.mp3")
                pygame.mixer.music.play(-1)
                fade(1, "./img/fond ch5.jpg",
                     "Chapitre 5 : Le temple des étoiles")
                fade(-1, "./img/fond ch5.jpg")
                fade(1, "./img/fond ch5.jpg")
                AVANCEMENT, HEROS = chapitre5()
                fade(-1, "./img/fond ch5.jpg")
            case 6:
                pygame.mixer.music.load("./sounds/ch6_music.mp3")
                pygame.mixer.music.play(-1)
                fade(1, "./img/fond_ch6.jpg",
                     "Chapitre 6 : Les cavernes de l'oubli")
                fade(-1, "./img/fond_ch6.jpg")
                fade(1, "./img/fond_ch6.jpg")
                AVANCEMENT, HEROS = chapitre6()
                fade(-1, "./img/fond ch6.jpg")
            case 7:
                pygame.mixer.music.load("./sounds/ch7_music.mp3")
                pygame.mixer.music.play(-1)
                fade(1, "./img/fond ch7.jpg",
                     "Chapitre 7 : La mer des âmes")
                fade(-1, "./img/fond ch7.jpg")
                fade(1, "./img/fond ch7.jpg")
                AVANCEMENT, HEROS = chapitre7()
                fade(-1, "./img/fond ch7.jpg")
            case 8:
                pygame.mixer.music.load("./sounds/ch8_music.mp3")
                pygame.mixer.music.play(-1)
                fade(1, "./img/fond ch8.jpg",
                     "Chapitre 8 : Le château des ombres")
                fade(-1, "./img/fond ch8.jpg")
                fade(1, "./img/fond ch8.jpg")
                AVANCEMENT, HEROS = chapitre8()
                fade(-1, "./img/fond ch8.jpg")
            case 9:
                pygame.mixer.music.load("./sounds/ch9_music.mp3")
                pygame.mixer.music.play(-1)
                fade(1, "./img/fond ch9.jpg",
                     "Chapitre 9 : Le retour des Héros")
                fade(-1, "./img/fond ch9.jpg")
                fade(1, "./img/fond ch9.jpg")
                AVANCEMENT, HEROS = chapitre9()
                fade(-1, "./img/fond ch9.jpg")
            case 10:
                pygame.mixer.music.load("./sounds/ch10_music.mp3")
                pygame.mixer.music.play(-1)
                fade(1, "./img/fond ch10.jpg",
                     "Chapitre 10 : Épilogue")
                fade(-1, "./img/fond ch10.jpg")
                fade(1, "./img/fond ch10.jpg")
                AVANCEMENT, HEROS = chapitre10()
                fade(-1, "./img/fond ch10.jpg")
                changement_affichage()
                GAME_RUNNING = False
                fade(1, "./img/chemin_fond_flou.png")
            case _:
                check_events()
        DICT_VAR = dict_var_update(DICT_VAR, AVANCEMENT)
        OF.save(DICT_VAR)
        check_events()


def chapitre0():
    '''Lance le chapitre d'introduction du jeu'''
    global HEROS
    TB.textbox_output(
        "Bonjour aventurier ! Avant de commencer, nous vous proposons un petit didacticiel.@@Pour passer à la boite de texte suivante, appuyez sur n'importe quelle touche.@@@@@Appuyez pour continuer")
    TB.textbox_output(
        "Bien joué, continuez comme ça !@@@@@@@Appuyez pour continuer")
    done = 0
    while not done:
        if (TB.textbox_input("Pour entrer du texte, une boite de dialogue vierge va apparaître. Tu pourras y entrer ta réponse ou ce que tu souhaites communiquer puis appuyer sur 'entrer' pour valider ta réponse. Les questions seront formalisées comme suit :@Avez vous compris ?@- 1 : Oui@- 2 : Non@Vous devrez écrire dans la boîte de texte vierge qui va aparaitre '1' pour répondre 'oui' et '2' pour répondre 'Non'.@Appuyez pour continuer") == "1"):
            done = 1
            break
        TB.textbox_output(
            "Quand cette boîte de dialogue disparaîtra, écrivez '1' pour répondre 'oui' ou '2' pour 'non' puis appuyez sur 'entrer' pour valider.@@@@@@Appuyez pour continuer")
    TB.textbox_output(
        "Bien joué, continuez comme ça !@@@@@@@Appuyez pour continuer")
    TB.textbox_output(
        "Enfin, si vous le souhaitez, vous pouvez quitter à tout moment en appuyant sur 'tab'. Une sauvegarde automatique se fait à la fin de chaque chapitre.")
    TB.textbox_output("Bienvenue aventurier, dans les Royaumes de l'Éclipse !@Au seuil de cette aventure épique, vous êtes sur le point d'embarquer pour des terres inconnues, où le destin se tisse entre les ombres et la lumière.")
    TB.textbox_output("Préparez-vous à plonger dans un monde de mystère et de magie, où chaque choix que vous ferez influencera le cours de l'Histoire. Des terres sauvages aux cités florissantes, des donjons oubliés aux montagnes glacées, l'aventure vous attend à chaque tournant.")
    TB.textbox_output("Avant de commencer votre voyage, il est temps de forger votre propre destin. Créez votre personnage, choisissez votre race, votre classe et préparez-vous à affronter les défis qui vous attendent. Votre courage, votre astuce et votre détermination seront vos meilleurs alliés dans cette quête pour la gloire et l'honneur.")
    TB.textbox_output(
        "L'aventure vous appelle, cher héros. Êtes-vous prêt à répondre à son appel et à laisser votre marque sur les Royaumes de l'Éclipse ?")
    done = False
    nom_heros = TB.textbox_input(
        "Veuillez entrer le nom de votre personnage : ")
    while not done:
        race_heros = ""
        choix_race = TB.textbox_input(
            "Veuillez sélectionner une race parmi :@- 1 : humain@- 2 : elfe@- 3 : orc")
        if (choix_race) in ["1", "2", "3"]:
            done = True
            race_heros = int(choix_race)
    done = False
    while not done:
        classe_heros = ""
        choix_classe = TB.textbox_input(
            "Veuillez sélectionner une classe parmi :@- 1 : guerrier@- 2 : archer@- 3 : tank")
        if choix_classe in ["1", "2", "3"]:
            done = True
            classe_heros = int(choix_classe)

    # on crée un heros avec le X eme element de la liste des races/classes
    HEROS = Ett.Joueur(nom_heros, Ett.liste_classe[int(
        classe_heros)-1], Ett.liste_race[int(race_heros)-1])
    sprite = pygame.image.load(HEROS.update_sprite())
    screen.blit(sprite, (-25, window_height-(sprite.get_height()+100)))
    TB.textbox_output("Vous êtes : "+HEROS.nom+", de la race des "+HEROS.race+"s. Vous êtes un futur " +
                      HEROS.classe+" dont on contera l'hisoire pendant des générations !")
    TB.textbox_output("Voici vos statistiques :@- PV max : " +
                      str(HEROS.pv_max)+"@- Points de Combat (dégâts par coup): "+str(HEROS.pc)+"@- Points de Défense (quantité des blessures prévenu par coup): "+str(HEROS.pd))
    return 1, HEROS


def chapitre1():
    '''Lance le chapitre 1 du jeu'''
    global HEROS
    global RUNNING

    background = pygame.image.load(
        "./img/burning_village.jpg").convert_alpha()
    background = pygame.transform.scale(
        background, (window_width, window_height))
    sprite = pygame.image.load(f"./img/{HEROS.race}_{HEROS.classe}.png")
    screen.blit(sprite, (-25, window_height-(sprite.get_height()+100)))
    TB.textbox_output("Vous vous réveillez en sursaut dans votre humble demeure, l'air empli de fumée et les cris déchirant la tranquillité de la nuit. Votre village est attaqué par des créatures mystérieuses, surgies des ombres. Vous entendez les hurlements de vos voisins et le rugissement des flammes qui dévorent les maisons autour de vous.")
    TB.textbox_output("Vous vous précipitez hors de votre maison, arme en main, prêt à défendre ce qui reste de votre foyer. Mais il est déjà trop tard. Les créatures, ressemblant à des ombres animées, ont réduit votre village en cendres. Seuls les souvenirs de vos proches perdurent dans votre esprit.")

    tps_musique = pygame.mixer.music.get_pos()
    C.bataille(screen, HEROS, Ett.Monstre(
        Ett.ombre_assaillante_classe, Ett.ombre_race), "./img/ombre assayante.png")
    if HEROS.pv <= 0:
        RUNNING = False
        pygame.quit()
        pygame.mixer.quit()
        quit()
    pygame.mixer.music.load("./sounds/ch1_music.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_pos(tps_musique)
    screen.blit(background, (0, 0))
    screen.blit(sprite, (-25, window_height-(sprite.get_height()+100)))
    M.obt_objet(E.Consommable(
        "Petite potion de soin", 0, 0, 30, 10,  "soin"), HEROS)
    M.obt_objet(E.Consommable(
        "Petite potion de soin", 0, 0, 30, 10, "soin"), HEROS)

    TB.textbox_output("Après un combat acharné, vous parvenez à abattre l'une des créatures, mais vous réalisez que vous ne pouvez pas sauver ce qui reste du village. Vous devez fuir et trouver un endroit sûr.")
    fade(-1, "./img/burning_village.jpg")
    fade(1, "./img/chemin_pierre_runes.jpg")
    screen.blit(sprite, (-25, window_height-(sprite.get_height()+100)))
    TB.textbox_output("Vous vous dirigez vers la forêt voisine, cherchant à échapper à l'horreur qui s'est abattue sur vous. En vous enfonçant dans les bois, vous découvrez un sentier à peine visible, marqué par des signes anciens. Vous sentez une étrange énergie émanant de ces symboles.")
    done = False
    while not done:
        choix = TB.textbox_input(
            "Choix : @- 1 : Suivre le sentier marqué@- 2 : Ignorer les symboles et avancer dans la forêt")
        if choix in ["1", "2"]:
            done = True
    if choix == "1":
        TB.textbox_output("1. Suivre le sentier marqué :@Vous décidez de suivre le sentier, intrigué par les signes. Après une marche prudente, vous tombez sur une petite clairière où repose un ancien autel. Sur l'autel, vous trouvez une dague en argent finement ouvragée, ornée de runes protectrices. Vous la prenez, sentant une légère chaleur émaner de l'arme, comme si elle vous acceptait comme son porteur légitime.")
        M.obt_objet(E.Equipement("Dague en argent",
                    25, 0, 30, "main_droite"), HEROS)

    if choix == "2":
        TB.textbox_output("2. Ignorer les symboles et avancer dans la forêt :@Vous choisissez de ne pas suivre le sentier et de continuer votre chemin dans la forêt. Plus loin, vous trouvez une cachette naturelle sous un arbre colossal. En fouillant, vous découvrez un vieux sac contenant un arc en bois sombre et un carquois rempli de flèches enchantées. Vous vous équipez de l'arc, sentant une connexion immédiate avec l'arme.")
        M.obt_objet(E.Equipement("Arc", 30, 0, 15, "main_droite"), HEROS)

    TB.textbox_output("Vous continuez votre marche, les ténèbres de la forêt vous enveloppant. Chaque pas que vous faites vous éloigne un peu plus de votre passé et vous rapproche de la vérité sur cette Éclipse mystérieuse et des créatures qui ont ravagé votre village. ")
    TB.textbox_output(
        "La quête pour découvrir la source de cette malédiction et venger votre foyer commence maintenant.")
    sprite_marchand = pygame.image.load("./img/marchand.png")
    screen.blit(sprite_marchand, (screen.get_width()-25-sprite_marchand.get_width(),
                                  screen.get_height()-(sprite_marchand.get_height()+50)))
    M.ouvertureDeLaBoutique(
        HEROS, 1, [(E.Consommable("Petite potion de force", 5, 5, 0, 10, "attaque")), (E.Equipement("Bouclier de bois", 0, 5, 5, "main_gauche")), (E.Equipement("épé en bois", 10, 0, 5, "main_droite"))])
    screen.blit(background, (0, 0))
    screen.blit(sprite, (-25, window_height-(sprite.get_height()+100)))
    return 2, HEROS


def chapitre2():
    '''Lance le chapitre 2 du jeu'''
    global HEROS
    global RUNNING
    background = pygame.image.load(
        "./img/ruines_dans_foret.png").convert_alpha()
    background = pygame.transform.scale(
        background, (window_width, window_height))
    sprite = pygame.image.load(
        f"./img/{HEROS.race}_{HEROS.classe}.png")
    screen.blit(sprite, (-25, window_height-(sprite.get_height()+100)))
    TB.textbox_output("Après avoir échappé à l'attaque de votre village, vous errez dans la forêt pendant plusieurs jours, cherchant des réponses et un refuge. Les arbres s'éclaircissent finalement, révélant une vallée cachée où se dressent les ruines d'une civilisation ancienne, à moitié enfouies sous la végétation.")
    TB.textbox_output("Vous avancez prudemment parmi les pierres effondrées et les colonnes brisées, sentant l'aura mystique qui émane de cet endroit oublié. Des fresques murales racontent l'histoire d'un royaume autrefois prospère, détruit par une force obscure similaire à celle qui a attaqué votre village. Vous comprenez que ces ruines détiennent des secrets vitaux pour votre quête.")
    TB.textbox_output("Soudain, des bruits étranges retentissent autour de vous. Des silhouettes se déplacent parmi les décombres. Vous vous cachez derrière une colonne et observez des créatures humanoïdes aux yeux brillants, gardant les lieux.")
    tps_musique = pygame.mixer.music.get_pos()
    C.bataille(screen, HEROS, Ett.Monstre(
        Ett.garde_squelette_classe, Ett.squelette_race), "./img/skeleton_warrior.png")
    if HEROS.pv <= 0:
        RUNNING = False
        pygame.quit()
        pygame.mixer.quit()
        quit()
    pygame.mixer.music.load("./sounds/ch2_music.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_pos(tps_musique)
    screen.blit(background, (0, 0))
    screen.blit(sprite, (-25, window_height-(sprite.get_height()+100)))
    M.obt_objet(E.Consommable("Petite potion de force",
                5, 5, 0, 10, "attaque"), HEROS)
    M.obt_objet(E.Equipement("Heaume Basique",
                0, 5, 7, "tete"), HEROS)
    M.obt_objet(E.Equipement("Plastron Basique",
                             0, 7, 10, "torse"), HEROS)
    M.obt_objet(E.Equipement("Jambières Basique",
                             0, 5, 7, "jambes"), HEROS)
    M.obt_objet(E.Equipement("Bottes Basique",
                             0, 3, 5, "pieds"), HEROS)
    TB.textbox_output("Après avoir vaincu l'un des gardes squelettiques, vous fouillez les ruines à la recherche d'indices. Vous tombez sur une chambre secrète, protégée par un mécanisme complexe.")
    done = False

    while not done:
        choix = TB.textbox_input(
            "Choix: @- 1 : Résoudre l'énigme du mécanisme@- 2 : Forcer l'entrée")
        if choix in ["1", "2"]:
            done = True
        if choix == "1":
            TB.textbox_output("1. Résoudre l'énigme du mécanisme :@Vous examinez le mécanisme et remarquez des symboles similaires à ceux vus dans la forêt. En manipulant soigneusement les pièces mobiles, vous parvenez à déverrouiller la porte. À l'intérieur, vous trouvez une amulette ancienne, gravée de runes protectrices. En la mettant autour de votre cou, vous ressentez un pouvoir de protection et de clairvoyance.")

            M.obt_objet(E.Equipement("Amulette de clairevoyance",
                                     0, 8, 10, "tete"), HEROS)
        if choix == "2":
            TB.textbox_output("2. Forcer l'entrée :@Impatient, vous décidez de forcer l'entrée en utilisant votre force et vos armes. Après plusieurs essais, la porte finit par céder. À l'intérieur, vous trouvez une épée en cristal, légèrement fissurée mais encore imprégnée d'une énergie redoutable. L'épée vibre légèrement entre vos mains, comme si elle reconnaissait votre détermination.")
            M.obt_objet(E.Equipement("épé de cristal",
                        40, 0, 15, "main_droite"), HEROS)
    TB.textbox_output(
        "Avec votre nouvelle acquisition, vous continuez à explorer les ruines.")
    fade(-1, "./img/ruines_dans_foret.png")
    fade(1, "./img/book_in_ruins.jpg")
    TB.textbox_output("Vous trouvez finalement un ancien grimoire, contenant des histoires et des prophéties sur l'Éclipse et les créatures des ombres. En le feuilletant, vous apprenez qu'un artefact puissant, capable de contrôler ou détruire ces créatures, est caché quelque part dans le royaume.")
    TB.textbox_output("Votre quête prend une nouvelle tournure. Armé de nouvelles connaissances et de puissants artefacts, vous quittez les ruines et vous vous enfoncez plus profondément dans la vallée, déterminé à trouver cet artefact avant qu'il ne soit trop tard.")
    fontaine(HEROS)
    sprite_marchand = pygame.image.load("./img/marchand.png")
    screen.blit(sprite_marchand, (screen.get_width()-25-sprite_marchand.get_width(),
                                  screen.get_height()-(sprite_marchand.get_height()+50)))
    M.ouvertureDeLaBoutique(
        HEROS, 1, [(E.Consommable("Petite potion de force", 5, 5, 0, 10, "attaque")), (E.Consommable("Petite potion de force", 5, 5, 0, 10, "attaque")), (E.Consommable("Potion étrange", 15, 10, 0, 25, "attaque")), (E.Equipement("Bottes d'aventurier", 0, 7, 10, "pieds"))])
    screen.blit(background, (0, 0))
    screen.blit(sprite, (-25, window_height-(sprite.get_height()+100)))
    return 3, HEROS


def chapitre3():
    '''Lance le chapitre 3 du jeu'''
    global HEROS
    global RUNNING
    background = pygame.image.load(
        "./img/foret_sombre.jpg").convert_alpha()
    background = pygame.transform.scale(
        background, (window_width, window_height))
    sprite = pygame.image.load(f"./img/{HEROS.race}_{HEROS.classe}.png")
    screen.blit(sprite, (-25, window_height-(sprite.get_height()+100)))
    TB.textbox_output("Après avoir quitté les ruines oubliées avec une nouvelle détermination, vous vous dirigez vers la Forêt des Murmures, un endroit réputé pour être hanté par des esprits malveillants. La forêt est dense et sombre, les arbres immenses bloquant la lumière du soleil. Chaque pas que vous faites est accompagné de murmures étranges qui semblent vous suivre, chuchotant des secrets oubliés et des avertissements cryptiques.")
    TB.textbox_output("Les murmures deviennent plus insistants alors que vous vous enfoncez dans la forêt. Vous commencez à distinguer des mots et des phrases, comme si les arbres eux-mêmes tentaient de communiquer avec vous. Vous comprenez que pour progresser, vous devez déchiffrer ces murmures et comprendre leur signification.")
    TB.textbox_output("En vous concentrant, vous percevez une direction à suivre. Les murmures vous conduisent à une clairière où se dresse un arbre ancien, ses racines formant une sorte de sanctuaire naturel. Là, vous trouvez un autel entouré de pierres gravées de runes. Vous devez résoudre l'énigme des runes pour libérer l'énergie protectrice de l'arbre.")
    done = False

    while not done:
        choix = TB.textbox_input(
            "Choix: @- 1 : Tenter de déchiffrer les runes@- 2 : Ignorer les runes et explorer la clairière")
        if choix in ["1", "2"]:
            done = True
        if choix == "1":
            TB.textbox_output("1. Tenter de déchiffrer les runes :@Vous décidez de vous concentrer sur les runes. En utilisant les connaissances acquises dans les ruines, vous parvenez à déchiffrer les symboles et à activer l'autel. Un éclat de lumière enveloppe l'arbre, révélant une baguette ancienne imprégnée de magie. Vous prenez la baguette, sentant une puissance nouvelle couler dans vos veines.")
            M.obt_objet(E.Equipement("Baguette de sorcier ancienne",
                                     45, 0, 10, "main_droite"), HEROS)

        if choix == "2":
            TB.textbox_output("2. Ignorer les runes et explorer la clairière :@Vous choisissez de ne pas perdre de temps avec les runes et d'explorer la clairière à la place. En fouillant les environs, vous découvrez un petit coffret enterré sous les racines de l'arbre. À l'intérieur, vous trouvez une amulette en jade, gravée de symboles de protection. Vous mettez l'amulette autour de votre cou, sentant une aura protectrice vous envelopper.")
            M.obt_objet(E.Equipement("Amulette de jade",
                                     10, 10, 10, "tete"), HEROS)
    TB.textbox_output("Alors que vous continuez à explorer la forêt, vous entendez soudain des bruits de pas lourds derrière vous. Vous vous retournez pour voir une créature massive, composée de branches et de feuillage, ses yeux brillants de malveillance. Elle avance vers vous, ses griffes prêtes à frapper.")
    tps_musique = pygame.mixer.music.get_pos()
    C.bataille(screen, HEROS, Ett.Monstre(
        Ett.golem_foret_classe, Ett.golem_race), "img/golem.png")
    if HEROS.pv <= 0:
        RUNNING = False
        pygame.quit()
        pygame.mixer.quit()
        quit()
    pygame.mixer.music.load("./sounds/ch3_music.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_pos(tps_musique)
    screen.blit(background, (0, 0))
    screen.blit(sprite, (-25, window_height-(sprite.get_height()+100)))
    TB.textbox_output("Après un combat intense, vous parvenez à vaincre le Golem de la Forêt, utilisant votre nouvelle arme ou votre amulette pour vous protéger. Avec la créature vaincue, les murmures de la forêt s'apaisent, comme si les esprits vous reconnaissaient enfin comme un allié.")
    TB.textbox_output("Vous quittez la Forêt des Murmures, votre équipement renforcé et votre détermination intacte. Vous savez que les défis à venir seront encore plus redoutables, mais chaque pas vous rapproche de la vérité sur l'Éclipse et du moyen de sauver votre royaume.")
    sprite_marchand = pygame.image.load("./img/marchand.png")
    screen.blit(sprite_marchand, (screen.get_width()-25-sprite_marchand.get_width(),
                                  screen.get_height()-(sprite_marchand.get_height()+50)))
    M.ouvertureDeLaBoutique(
        HEROS, 1, [(E.Consommable("Potion de force intermédiaire", 10, 0, 3, 40, "attaque")), (E.Consommable("Dague elfique", 17, 0, 20, "main_droite"))])
    screen.blit(background, (0, 0))
    screen.blit(sprite, (-25, window_height-(sprite.get_height()+100)))
    return 4, HEROS


def chapitre4():
    '''Lance le chapitre 4 du jeu'''
    global HEROS
    global RUNNING
    background = pygame.image.load(
        "./img/fond ch4.jpg").convert_alpha()
    background = pygame.transform.scale(
        background, (window_width, window_height))
    sprite = pygame.image.load(f"./img/{HEROS.race}_{HEROS.classe}.png")
    screen.blit(sprite, (-25, window_height-(sprite.get_height()+100)))
    TB.textbox_output("Après avoir quitté la Forêt des Murmures, vous continuez votre voyage jusqu'à atteindre une vallée cachée où se trouve une ville mystérieuse. Dès que vous pénétrez dans cette cité, vous remarquez quelque chose d'étrange : la lune y brille constamment, ne laissant jamais place au jour. Les habitants semblent mener une vie normale, mais il y a une mélancolie palpable dans l'air, comme s'ils étaient prisonniers de cette nuit éternelle.")
    TB.textbox_output("En explorant les rues pavées et les bâtiments élégants mais décrépits, vous apprenez que la cité est sous l'emprise d'une malédiction qui maintient la lune éternellement dans le ciel. Les habitants vivent dans la peur, sachant que cette anomalie attire des créatures nocturnes dangereuses. Vous êtes déterminé à les aider et à en apprendre plus sur cette malédiction.")
    TB.textbox_output("Vous rencontrez le chef de la cité, un vieil homme sage nommé Alaric, qui vous explique que la clé pour briser la malédiction se trouve dans un ancien sanctuaire au centre de la ville. Cependant, le sanctuaire est gardé par des créatures de l'ombre. En vous approchant du sanctuaire, vous êtes attaqué par un groupe de gardiens nocturnes.")
    tps_musique = pygame.mixer.music.get_pos()
    C.bataille(screen, HEROS, Ett.Monstre(
        Ett.gardiens_nocturnes_classe, Ett.gardiens_race), "img/gardien nocturne.png")
    if HEROS.pv <= 0:
        RUNNING = False
        pygame.quit()
        pygame.mixer.quit()
        quit()
    pygame.mixer.music.load("./sounds/ch4_music.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_pos(tps_musique)
    screen.blit(background, (0, 0))
    screen.blit(sprite, (-25, window_height-(sprite.get_height()+100)))
    M.obt_objet(E.Equipement("Bouclier de fer",
                0, 20, 40, "main_gauche"), HEROS)

    TB.textbox_output("Après avoir vaincu les gardiens, vous entrez dans le sanctuaire et trouvez un autel au centre de la pièce, illuminé par une lumière lunaire intense. L'autel est orné de cristaux lunaires et de symboles anciens.")

    done = False
    while not done:
        choix = TB.textbox_input(
            "Choix: @- 1 : Utiliser un cristal lunaire sur l'autel@- 2 : Réciter une incantation des runes découvertes")
        if choix in ["1", "2"]:
            done = True
        if choix == "1":
            TB.textbox_output("1. Utiliser un cristal lunaire sur l'autel :@Vous choisissez de prendre un cristal lunaire et de le placer sur l'autel. Dès que le cristal touche la surface, une lumière éclatante inonde la pièce et l'autel se met à vibrer. Un bouclier lunaire apparaît devant vous, fait d'une lumière pure et protectrice. Vous prenez le bouclier, sentant sa force apaisante vous envelopper.")
            M.obt_objet(E.Equipement(
                "Bouclier de fer", 0, 25, 45, "main_gauche"))
        if choix == "2":
            TB.textbox_output("2. Réciter une incantation des runes découvertes :@Vous vous souvenez des runes que vous avez vues dans la Forêt des Murmures et commencez à réciter une incantation. Les symboles sur l'autel s'illuminent, et une vague d'énergie vous traverse. Une bague de lune apparaît sur l'autel, ornée de pierres scintillantes. Vous la mettez, sentant une puissance nouvelle renforcer vos capacités magiques.")
            M.obt_objet(E.Equipement("L'Anneau de la Lune",
                                     15, 15, 10, "main_gauche"), HEROS)

    TB.textbox_output("Avec cet artéfact légendaire, vous sentez que vous avez maintenant le pouvoir de libérer la cité de sa malédiction. Vous retournez voir Alaric et ensemble, vous organisez un rituel pour invoquer l'énergie de la lune et dissiper la malédiction.")

    TB.textbox_output("Le rituel est un succès, et pour la première fois depuis des décennies, le soleil se lève sur la cité. Les habitants vous remercient chaleureusement, offrant leur aide pour votre quête future. Vous quittez la cité sous la lune, maintenant libérée, avec un sentiment renouvelé de force et d'espoir.")
    fontaine(HEROS)
    sprite_marchand = pygame.image.load("./img/marchand.png")
    screen.blit(sprite_marchand, (screen.get_width()-25-sprite_marchand.get_width(),
                                  screen.get_height()-(sprite_marchand.get_height()+50)))
    M.ouvertureDeLaBoutique(
        HEROS, 1, [(E.Equipement("Épée de l'élu", 60, 0, 90, "main_droite")), (E.Consommable("Potion de soin intermédiaire", 0, 0, 70, 40, "soin"))])
    screen.blit(background, (0, 0))
    screen.blit(sprite, (-25, window_height-(sprite.get_height()+100)))
    return 5, HEROS


def chapitre5():
    '''Lance le chapitre 5 du jeu'''
    global HEROS
    global RUNNING
    background = pygame.image.load(
        "./img/fond ch5.jpg").convert_alpha()
    background = pygame.transform.scale(
        background, (window_width, window_height))
    sprite = pygame.image.load(f"./img/{HEROS.race}_{HEROS.classe}.png")
    screen.blit(sprite, (-25, window_height-(sprite.get_height()+100)))
    TB.textbox_output("Après avoir libéré la cité sous la lune, vous continuez votre quête vers le nord, suivant les indications des anciens textes et des conseils des habitants reconnaissants. Votre destination est un temple ancien, caché dans les montagnes, dédié aux étoiles et à leurs mystérieux pouvoirs.")
    TB.textbox_output("La montée est ardue, les sentiers escarpés et souvent masqués par des nuages épais. Après plusieurs jours de marche, vous atteignez enfin l'entrée du temple des étoiles. Devant vous se dresse une structure imposante, faite de pierres anciennes et ornée de symboles célestes. L'air est imprégné de magie, et vous sentez une énergie puissante émaner des lieux.")
    TB.textbox_output("En entrant dans le temple, vous découvrez une salle immense, avec un plafond voûté parsemé de cristaux brillants, imitant un ciel étoilé. Au centre de la salle, un autel lumineux attire votre attention. Alors que vous vous en approchez, des créatures spectrales surgissent des ombres pour défendre le sanctuaire.")
    tps_musique = pygame.mixer.music.get_pos()
    C.bataille(screen, HEROS, Ett.Monstre(Ett.spectres_gardiens_classe,
               Ett.gardiens_race), "img/spectres gardiens.png")
    if HEROS.pv <= 0:
        RUNNING = False
        pygame.quit()
        pygame.mixer.quit()
        quit()
    pygame.mixer.music.load("./sounds/ch5_music.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_pos(tps_musique)
    screen.blit(background, (0, 0))
    screen.blit(sprite, (-25, window_height-(sprite.get_height()+100)))
    done = False
    while not done:
        choix = TB.textbox_input(
            "Choix: @- 1 : Résoudre l'énigme de l'étoile polaire@- 2 : Résoudre l'énigme de la constellation du lion")
        if choix in ["1", "2"]:
            done = True
        if choix == "1":
            TB.textbox_output("1. Résoudre l'énigme de l'étoile polaire :@Vous décidez de vous concentrer sur l'énigme de l'étoile polaire. Après avoir aligné les cristaux selon les indications des symboles, un éclat de lumière illumine l'autel et une cape étoilée apparaît. En l'enfilant, vous ressentez une protection contre les forces obscures et une clarté mentale accrue.")
            M.obt_objet(E.Equipement(
                "Cape d'étoile", 0, 35, 45, "main_gauche"))
        if choix == "2":
            TB.textbox_output("2. Résoudre l'énigme de la constellation du lion :@Vous choisissez de résoudre l'énigme de la constellation du lion. En replaçant les cristaux pour former la constellation, l'autel s'illumine et une épée céleste se matérialise. Vous saisissez l'épée, sentant une puissance nouvelle et une force inébranlable couler dans vos bras.")
            M.obt_objet(E.Equipement("Épée de la Constellation du Lion",
                                     55, 0, 55, "main_gauche"), HEROS)
    TB.textbox_output("Avec votre nouvelle acquisition, vous explorez plus en avant le temple. Vous découvrez des fresques et des inscriptions révélant l'histoire de l'Éclipse et de l'ancien royaume. Vous apprenez que l'Éclipse est liée à un artefact puissant, caché dans un lieu secret et protégé par des forces redoutables.")
    TB.textbox_output("Soudain, une porte secrète s'ouvre, révélant un passage vers une chambre intérieure. Là, vous trouvez un ancien grimoire, contenant des sorts et des incantations oubliées, ainsi qu'une carte détaillant l'emplacement de l'artefact que vous cherchez.")
    TB.textbox_output("Vous quittez le temple des étoiles, votre esprit éclairé par les nouvelles connaissances et votre équipement renforcé par les artefacts célestes. Vous savez que le chemin sera encore long et dangereux, mais vous êtes déterminé à poursuivre votre quête pour sauver votre royaume de l'Éclipse imminente.")
    sprite_marchand = pygame.image.load("./img/marchand.png")
    screen.blit(sprite_marchand, (screen.get_width()-25-sprite_marchand.get_width(),
                                  screen.get_height()-(sprite_marchand.get_height()+50)))
    M.ouvertureDeLaBoutique(
        HEROS, 1, [(E.Equipement("Épée des ténebres", 65, 0, 85, "main_droite")), (E.Equipement("Bouclier des ténebres", 5, 30, 65, "main_droite"))])
    screen.blit(background, (0, 0))
    screen.blit(sprite, (-25, window_height-(sprite.get_height()+100)))
    fontaine(HEROS)
    return 6, HEROS


def chapitre6():
    '''Lance le chapitre 6 du jeu'''
    global HEROS
    global RUNNING
    background = pygame.image.load(
        "./img/fond ch6.jpg").convert_alpha()
    background = pygame.transform.scale(
        background, (window_width, window_height))
    sprite = pygame.image.load(f"./img/{HEROS.race}_{HEROS.classe}.png")
    screen.blit(sprite, (-25, window_height-(sprite.get_height()+100)))
    TB.textbox_output("Avec la carte et les connaissances acquises au temple des étoiles, vous vous dirigez maintenant vers un réseau de cavernes souterraines connues sous le nom de Cavernes de l'Oubli. Ces cavernes sont réputées pour leur labyrinthe sans fin et leurs créatures de l'ombre. On dit que ceux qui y pénètrent sont confrontés à leurs peurs les plus profondes.")
    TB.textbox_output("En entrant dans les cavernes, l'air devient plus froid et une obscurité oppressante vous enveloppe. Vos pas résonnent contre les parois humides et vous sentez que quelque chose vous observe dans les ténèbres. Vous allumez une torche pour éclairer votre chemin et avancez prudemment.")
    TB.textbox_output(
        "Rapidement, vous vous trouvez face à un choix de chemins, chacun menant plus profondément dans le labyrinthe.")
    done = False
    while not done:
        choix = TB.textbox_input(
            "Choix: @- 1 : Prendre le chemin de droite, marqué par des symboles mystérieux@- 2 : Prendre le chemin de gauche, illuminé par une lueur étrange")
        if choix in ["1", "2"]:
            done = True
        if choix == "1":
            TB.textbox_output("1. Prendre le chemin de droite, marqué par des symboles mystérieux :@Vous décidez de suivre le chemin de droite, attiré par les symboles gravés sur les parois. Les symboles ressemblent à ceux vus dans le temple des étoiles, et vous les suivez en espérant qu'ils vous mèneront à quelque chose d'important. Au bout du chemin, vous trouvez une alcôve cachée avec une bague d'ombre, qui semble absorber la lumière. En la mettant, vous sentez une connexion avec les ombres, vous permettant de passer inaperçu.")
            M.obt_objet(E.Equipement(
                "Bague des ombres", 10, 35, 55, "main_gauche"), HEROS)
        if choix == "2":
            TB.textbox_output("2. Prendre le chemin de gauche, illuminé par une lueur étrange :@Vous choisissez le chemin de gauche, intrigué par la lueur mystérieuse. En suivant cette lumière, vous arrivez dans une caverne où des cristaux phosphorescents illuminent une source souterraine. À côté de la source, vous trouvez un bracelet d'ombre, qui semble renforcer votre force physique. Vous mettez le bracelet, sentant un pouvoir brut se réveiller en vous.")
            M.obt_objet(E.Equipement("Bracelet étrange",
                                     70, 0, 55, "main_droite"), HEROS)
    TB.textbox_output(
        "Alors que vous continuez à explorer les cavernes, vous êtes soudain attaqué par une créature massive, formée de ténèbres mouvantes et de cris d'âmes perdues.")
    tps_musique = pygame.mixer.music.get_pos()
    C.bataille(screen, HEROS, Ett.Monstre(Ett.spectres_labyrinthe,
               Ett.spectre_race), "img/spectre labyrinthe.png")
    if HEROS.pv <= 0:
        RUNNING = False
        pygame.quit()
        pygame.mixer.quit()
        quit()
    pygame.mixer.music.load("./sounds/ch6_music.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_pos(tps_musique)
    screen.blit(background, (0, 0))
    screen.blit(sprite, (-25, window_height-(sprite.get_height()+100)))

    TB.textbox_output("Après un combat éprouvant, vous parvenez à vaincre le Spectre du Labyrinthe, utilisant vos nouvelles compétences et équipements. Le spectre vaincu, les ténèbres autour de vous semblent se dissiper légèrement, révélant un passage secret plus loin dans la caverne.")
    TB.textbox_output("Vous suivez ce passage jusqu'à une chambre cachée, où des fresques anciennes racontent l'histoire de héros passés, ceux qui ont tenté de combattre l'Éclipse mais ont échoué. Vous comprenez que ces âmes perdues sont celles des anciens héros, piégées dans les cavernes pour l'éternité.")
    TB.textbox_output("Dans cette chambre, vous trouvez un vieux grimoire, contenant des sorts oubliés et des incantations pour sceller les créatures de l'ombre. En le prenant, vous ressentez une lourdeur sur vos épaules, comme si vous héritiez du destin des anciens héros.")
    TB.textbox_output("En sortant des cavernes de l'oubli, vous êtes plus déterminé que jamais à réussir là où les autres ont échoué. Vous avez acquis de nouveaux pouvoirs et des connaissances cruciales, mais vous savez que le chemin qui vous attend est encore plus périlleux.")
    sprite_marchand = pygame.image.load("./img/marchand.png")
    screen.blit(sprite_marchand, (screen.get_width()-25-sprite_marchand.get_width(),
                                  screen.get_height()-(sprite_marchand.get_height()+50)))
    M.ouvertureDeLaBoutique(
        HEROS, 1, [(E.Equipement("Couronne étrange", 0, 25, 55, "tete"))])
    screen.blit(background, (0, 0))
    screen.blit(sprite, (-25, window_height-(sprite.get_height()+100)))
    return 7, HEROS


def chapitre7():
    '''Lance le chapitre 7 du jeu'''
    global HEROS
    global RUNNING
    background = pygame.image.load(
        "./img/fond ch7.jpg").convert_alpha()
    background = pygame.transform.scale(
        background, (window_width, window_height))
    sprite = pygame.image.load(f"./img/{HEROS.race}_{HEROS.classe}.png")
    screen.blit(sprite, (-25, window_height-(sprite.get_height()+100)))
    TB.textbox_output("Après avoir traversé les Cavernes de l'Oubli et acquis de nouveaux pouvoirs, vous poursuivez votre quête vers la mer des âmes, un océan mystérieux entouré de légendes et de contes lugubres. On dit que cette mer est le lieu où reposent les âmes des défunts, piégées dans un cycle éternel de tourment.")
    TB.textbox_output("Naviguant à bord d'un vieux navire abandonné que vous avez réparé, vous sentez une étrange aura de malédiction planer sur ces eaux. La mer est agitée, les vagues déferlent avec une intensité déconcertante et le ciel est constamment obscurci par des nuages sombres.")
    TB.textbox_output("Alors que vous avancez dans les eaux tumultueuses, votre navire est soudain attaqué par des créatures marines, des esprits tourmentés cherchant à vous engloutir dans les profondeurs de l'océan.")
    tps_musique = pygame.mixer.music.get_pos()
    C.bataille(screen, HEROS, Ett.Monstre(Ett.spectres_profondeurs,
               Ett.spectre_race), "img/spectre profondeurs.png")
    if HEROS.pv <= 0:
        RUNNING = False
        pygame.quit()
        pygame.mixer.quit()
        quit()
    pygame.mixer.music.load("./sounds/ch7_music.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_pos(tps_musique)
    screen.blit(background, (0, 0))
    screen.blit(sprite, (-25, window_height-(sprite.get_height()+100)))
    TB.textbox_output("Après avoir repoussé les attaquants, vous continuez à naviguer, cherchant un signe, un indice sur la manière de traverser la mer des âmes en toute sécurité. Au loin, vous apercevez une île isolée, entourée d'un halo de lumière éthérée. Vous décidez de vous en approcher, espérant y trouver des réponses.")
    TB.textbox_output("En abordant l'île, vous découvrez un ancien sanctuaire, gardé par une entité marine bienveillante. Elle vous raconte l'histoire de la mer des âmes et vous informe qu'un ancien artefact, capable de contrôler les flots tumultueux de l'océan, est caché au fond des eaux.")

    done = False
    while not done:
        choix = TB.textbox_input(
            "Choix: @- 1 : Plonger dans les profondeurs pour trouver l'artéfact@- 2 : Demander à l'entité marine de vous guider vers l'artéfact")
        if choix in ["1", "2"]:
            done = True
        if choix == "1":
            TB.textbox_output("1. Plonger dans les profondeurs pour trouver l'artéfact :@Vous décidez de plonger dans les profondeurs de la mer des âmes, bravant les dangers pour trouver l'artefact par vous-même. Après une plongée périlleuse, vous découvrez une épave ancienne au fond de l'océan. En explorant l'épave, vous trouvez un trident ancien, orné de runes marines. Vous le récupérez, sentant le pouvoir de l'océan couler à travers vous.")
            M.obt_objet(E.Equipement(
                "Trident ancien", 60, 0, 75, "main_droite"), HEROS)
        if choix == "2":
            TB.textbox_output("2. Demander à l'entité marine de vous guider vers l'artéfact :@Vous choisissez de demander à l'entité marine de vous guider vers l'artefact. Avec sa guidance, vous plongez dans les eaux profondes et trouvez rapidement un coffre ancien enfoui dans le sable. À l'intérieur, vous trouvez un collier de coquillages lumineux, qui semble émettre une lueur protectrice. Vous le prenez, sentant une connexion avec les créatures marines.")
            M.obt_objet(E.Equipement("Collier de coquillages",
                                     0, 35, 75, "tete"), HEROS)

    TB.textbox_output("Avec l'artefact en votre possession, vous retournez sur votre navire, prêt à continuer votre voyage à travers la mer des âmes. Vous avez maintenant les moyens de naviguer en sécurité à travers ces eaux hantées, mais vous savez que de nouveaux défis vous attendent avant d'atteindre votre destination finale.")
    fontaine(HEROS)
    sprite_marchand = pygame.image.load("./img/marchand.png")
    screen.blit(sprite_marchand, (screen.get_width()-25-sprite_marchand.get_width(),
                                  screen.get_height()-(sprite_marchand.get_height()+50)))
    M.ouvertureDeLaBoutique(HEROS, 1, [])
    screen.blit(background, (0, 0))
    screen.blit(sprite, (-25, window_height-(sprite.get_height()+100)))
    return 8, HEROS


def chapitre8():
    '''Lance le chapitre 8 du jeu'''
    global HEROS
    global RUNNING
    background = pygame.image.load(
        "./img/fond ch8.jpg").convert_alpha()
    background = pygame.transform.scale(
        background, (window_width, window_height))
    sprite = pygame.image.load(f"./img/{HEROS.race}_{HEROS.classe}.png")
    screen.blit(sprite, (-25, window_height-(sprite.get_height()+100)))

    TB.textbox_output("Votre voyage à travers la mer des âmes vous conduit finalement aux abords d'un château lugubre, perché sur une falaise escarpée. Ce château est connu sous le nom de Château des Ombres, le repaire supposé de la source de l'Éclipse et de son instigateur, un être de ténèbres ancestrales.")
    TB.textbox_output("Alors que vous approchez du château, vous sentez une aura maléfique vous envelopper, vous mettant au défi avant même d'avoir franchi les portes. Vous savez que le combat qui vous attend sera le plus difficile de votre quête jusqu'à présent, mais vous êtes déterminé à mettre fin à l'Éclipse et à sauver votre royaume.")
    TB.textbox_output(
        "Vous entrez dans le château et êtes immédiatement assailli par des hordes de créatures des ténèbres, invoquées pour défendre leur maître.")

    tps_musique = pygame.mixer.music.get_pos()
    C.bataille(screen, HEROS, Ett.Monstre(Ett.Gardiens_ombres_classe,
               Ett.gardiens_race), "img/garde des ombres.png")
    if HEROS.pv <= 0:
        RUNNING = False
        pygame.quit()
        pygame.mixer.quit()
        quit()
    pygame.mixer.music.load("./sounds/ch8_music.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_pos(tps_musique)
    screen.blit(background, (0, 0))
    screen.blit(sprite, (-25, window_height-(sprite.get_height()+100)))

    TB.textbox_output("Après avoir triomphé des gardes, vous vous frayez un chemin à travers les couloirs sombres et tortueux du château, suivant les traces de l'énergie maléfique jusqu'à ce que vous arriviez devant une grande porte verrouillée. Vous savez que derrière cette porte se trouve votre destinée, mais vous devez d'abord la déverrouiller.")

    done = False
    while not done:
        choix = TB.textbox_input(
            "Choix: @- 1 : Forcer la porte@- 2 : Chercher une clé")
        if choix in ["1", "2"]:
            done = True
        if choix == "1":
            TB.textbox_output("1. Forcer la porte :@Vous décidez de forcer la porte avec toute votre force, déterminé à affronter ce qui se cache derrière. Après plusieurs essais, la porte cède finalement, révélant une chambre sombre où flotte une aura sinistre. Vous avancez, prêt à affronter votre adversaire.")
        if choix == "2":
            TB.textbox_output("2. Chercher une clé :@Vous choisissez de chercher une clé pour ouvrir la porte, espérant qu'elle révélera un chemin plus sûr. En fouillant les pièces adjacentes, vous trouvez une clé cachée dans une vieille armoire. Avec la clé en main, vous ouvrez la porte et pénétrez dans la chambre, prêt à affronter ce qui vous attend.")

    TB.textbox_output("Vous vous retrouvez face à face avec l'instigateur de l'Éclipse, un être de ténèbres ancestrales connu sous le nom de Seigneur des Ombres. Son regard est empli de malice et de pouvoir, mais vous savez que vous devez le vaincre pour mettre fin à l'Éclipse et sauver votre royaume.")
    fontaine(HEROS)
    C.bataille(screen, HEROS, Ett.Monstre(Ett.boss_final_classe,
               Ett.boss_final_race), "./img/seigneur_ombres.png")
    if HEROS.pv <= 0:
        RUNNING = False
        pygame.quit()
        pygame.mixer.quit()
        quit()
    pygame.mixer.music.stop()  # c est normal qu il n y ai plus de musique
    screen.blit(background, (0, 0))
    screen.blit(sprite, (-25, window_height-(sprite.get_height()+100)))

    TB.textbox_output("Après un combat épique et épuisant, vous parvenez finalement à vaincre le Seigneur des Ombres, mettant ainsi un terme à son règne de terreur. L'Éclipse commence à se dissiper lentement, laissant place à la lumière du soleil et à l'espoir pour votre royaume.")
    TB.textbox_output("Vous êtes acclamé comme un héros par votre peuple reconnaissant, mais vous savez que votre aventure ne fait que commencer. Avec l'Éclipse vaincue, de nouveaux défis et de nouvelles quêtes vous attendent, mais vous êtes prêt à affronter l'avenir avec courage et détermination.")

    return 9, HEROS


def chapitre9():
    '''Lance le chapitre 9 du jeu'''
    global HEROS
    global RUNNING
    background = pygame.image.load(
        "./img/fond ch9.jpg").convert_alpha()
    background = pygame.transform.scale(
        background, (window_width, window_height))
    sprite = pygame.image.load(f"./img/{HEROS.race}_{HEROS.classe}.png")
    screen.blit(sprite, (-25, window_height-(sprite.get_height()+100)))

    TB.textbox_output("Avec la défaite du Seigneur des Ombres et la fin de l'Éclipse, la paix commence à revenir sur votre royaume. Les habitants, libérés de l'ombre qui pesait sur eux, célèbrent votre victoire et vous honorent comme des héros. Cependant, vous savez que votre quête n'est pas encore terminée.")
    TB.textbox_output("Alors que vous vous reposez après votre victoire, une nouvelle menace se profile à l'horizon. Des rumeurs circulent selon lesquelles des forces maléfiques, ayant survécu à la chute du Seigneur des Ombres, se rassemblent dans les recoins les plus sombres du royaume, prêtes à lancer une nouvelle attaque.")
    TB.textbox_output(
        "Vous décidez de reprendre votre équipement et de vous préparer à affronter cette nouvelle menace, déterminé à protéger votre royaume une fois de plus.")
    TB.textbox_output(
        "Alors que vous parcourez le royaume à la recherche des forces ennemies, vous rencontrez un groupe de guerriers déterminés à vous aider dans votre quête.")

    done = False
    while not done:
        choix = TB.textbox_input(
            "Choix: @- 1 : Accepter l'aide des guerriers@- 2 : Continuer seul")
        if choix in ["1", "2"]:
            done = True
        if choix == "1":
            TB.textbox_output("1. Accepter l'aide des guerriers :@Reconnaissant la valeur de l'unité, vous acceptez l'aide des guerriers. Ensemble, vous formez une force imposante, prête à affronter n'importe quelle menace qui se dresse sur votre chemin. En échange de leur aide, les guerriers vous offrent des armes et des armures améliorées, renforçant ainsi votre préparation pour le combat à venir.")
        if choix == "2":
            TB.textbox_output("2. Continuer seul :@Déterminé à prouver votre force et votre courage, vous décidez de continuer seul. Vous remerciez les guerriers pour leur offre d'aide, mais vous préférez suivre votre propre chemin. Vous savez que la tâche qui vous attend est ardue, mais vous êtes prêt à la relever seul, avec votre détermination comme seule arme.")

    TB.textbox_output(
        "Quel que soit votre choix, vous vous lancez dans une série de batailles épiques contre les forces maléfiques, repoussant chaque assaut avec force et courage.")
    TB.textbox_output("Finalement, après de nombreuses batailles et de nombreux défis surmontés, vous parvenez à vaincre les forces maléfiques et à ramener la paix durable dans votre royaume. Les habitants vous honorent une fois de plus comme des héros, reconnaissant votre dévouement et votre bravoure.")
    TB.textbox_output("Avec votre quête accomplie et votre royaume en sécurité, vous vous retirez pour profiter enfin de la paix que vous avez si durement gagnée. Mais vous savez que, si jamais une nouvelle menace surgit, vous serez prêt à défendre votre royaume avec la même détermination et la même force.")
    tps_musique = pygame.mixer.music.get_pos()
    C.bataille(screen, HEROS, Ett.Monstre(Ett.spectres_gardiens_classe,
               Ett.gardiens_race), "img/spectres gardiens.png")
    if HEROS.pv <= 0:
        RUNNING = False
        pygame.quit()
        pygame.mixer.quit()
        quit()
    pygame.mixer.music.load("./sounds/ch9_music.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_pos(tps_musique)

    return 10, HEROS


def chapitre10():
    '''Lance le chapitre 10 du jeu'''
    global HEROS
    background = pygame.image.load(
        "./img/fond ch10.jpg").convert_alpha()
    background = pygame.transform.scale(
        background, (window_width, window_height))
    sprite = pygame.image.load(f"./img/{HEROS.race}_{HEROS.classe}.png")
    screen.blit(sprite, (-25, window_height-(sprite.get_height()+100)))
    TB.textbox_output("Des années ont passé depuis la fin de la grande Éclipse qui a menacé votre royaume. La paix règne désormais en maître, les habitants vaquent à leurs occupations avec sérénité, et les histoires des héros qui ont sauvé le royaume sont maintenant légendaires.")
    TB.textbox_output("Vous, le héros de cette histoire, avez trouvé votre place dans ce nouveau monde de paix. Certains jours, vous voyagez à travers le royaume, rencontrant des gens reconnaissants qui vous remercient pour votre courage et votre dévouement. D'autres jours, vous vous reposez dans votre demeure, profitant des doux moments de calme et de tranquillité.")
    TB.textbox_output("Mais même dans cette ère de paix, il y a toujours des défis à relever. De temps en temps, une nouvelle menace émerge, un bandit à traquer, une bête à chasser, ou un mystère à résoudre. À chaque fois, vous vous levez pour affronter ces défis avec la même détermination et le même courage qui vous ont permis de vaincre l'Éclipse.")
    TB.textbox_output("Vous vous souvenez des compagnons qui ont partagé votre quête, des amis que vous avez rencontrés en chemin, et des ennemis que vous avez affrontés. Leurs visages et leurs histoires restent gravés dans votre mémoire, rappelant les épreuves que vous avez traversées et les victoires que vous avez remportées ensemble.")
    TB.textbox_output("Alors que vous regardez le ciel étoilé, vous vous souvenez de l'Éclipse qui a assombri votre royaume, mais aussi de la lumière qui a brillé dans les ténèbres, celle de l'espoir, de la bravoure et de la détermination. Et vous savez que, quoi qu'il arrive, cette lumière brillera toujours, guidant votre chemin et illuminant votre destinée.")
    TB.textbox_output("Votre aventure dans le royaume de l'Éclipse se termine ici, mais votre histoire ne fait que commencer. Car tant qu'il y aura des héros prêts à se battre pour ce en quoi ils croient, le royaume continuera à prospérer, baigné dans la lumière de l'espoir et de la paix.")

    TB.textbox_output("Merci d'avoir joué")
    TB.textbox_output("Fin de la partie")
    return 10, HEROS


# Variables globales
ICON = pygame.image.load("img/logo.png").convert_alpha()
RUNNING = True
BLACK = (0, 0, 0)
GREY_30 = (30, 30, 30)
WHITE = (255, 255, 255)
DICT_VAR = {            # Dictionnaire de sauvegarde
    "nom_joueur": "",
    "classe_joueur": "",
    "race_joueur": "",
    "inventaire_joueur": [],
    "pv_joueur": 0,
    "argent_joueur": 0,
    "avancement": 0
}
ETAT = "ecran_titre"    # Variable de sélection de menus : ecran_titre / jeu
GAME_RUNNING = False    # Variable qui indique si le jeu tourne ou non
AVANCEMENT = 0

pygame.init()
pygame.mixer_music.load("./sounds/title_theme.mp3")
pygame.mixer.music.play(-1)
pygame.display.set_caption("Les Royaumes de l'Éclipse")
pygame.key.set_repeat(400, 30)
pygame.display.set_icon(ICON)
window_width, window_height = dimensions_ecran()
button_w, button_h = 350, 80
screen = pygame.display.set_mode((window_width, window_height))

fade(1, "./img/chemin_fond_flou.png")
while RUNNING:
    if ETAT == "ecran_titre":
        ecran_titre()
    elif ETAT == "jeu":
        jeu()
