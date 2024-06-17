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


def dimensions_ecran():
    '''Récupère les dimensions de l'écran du joueur et les retourne dans un tuple (w,h)'''
    screen_info = pygame.display.Info()
    screen_width = screen_info.current_w
    screen_height = screen_info.current_h
    return (screen_width, screen_height)


def fade(mode: str, ch_image1: str = "./img/chemin_fond_flou.png", ch_image2: str = "./img/chemin_fond_flou.png", text: str = ""):
    global BLACK
    screen_width, screen_height = dimensions_ecran()
    image1 = pygame.image.load(ch_image1)
    image2 = pygame.image.load(ch_image2)
    image1 = pygame.transform.scale(image1, (screen_width, screen_height))
    image2 = pygame.transform.scale(image2, (screen_width, screen_height))
    font = pygame.font.Font("./font/VecnaBold-4YY4.ttf", 100)
    texte = font.render(text, True, WHITE)
    texte_rect = texte.get_rect(center=(window_width//2, window_height//2))
    fade = pygame.Surface((screen_width, screen_height))
    fade.fill(BLACK, (0, 0, window_width, window_height))
    if mode == "img_to_black":
        opacity = 0
        for r in range(300):
            opacity += 1
            fade.set_alpha(opacity)
            screen.blit(image1, (0, 0))
            screen.blit(texte, texte_rect)
            screen.blit(fade, (0, 0))
            pygame.display.update()
            pygame.time.delay(5)
    elif mode == "black_to_img":
        opacity = 300
        for r in range(300):
            opacity -= 1
            fade.set_alpha(opacity)
            screen.blit(image1, (0, 0))
            screen.blit(texte, texte_rect)
            screen.blit(fade, (0, 0))
            pygame.display.update()
            pygame.time.delay(5)
    elif mode == "img_to_black_to_img":
        opacity = 0
        for r in range(300):
            opacity += 1
            fade.set_alpha(opacity)
            screen.blit(image1, (0, 0))
            screen.blit(texte, texte_rect)
            screen.blit(fade, (0, 0))
            pygame.display.update()
            pygame.time.delay(5)
        for r in range(300):
            opacity -= 1
            fade.set_alpha(opacity)
            screen.blit(image2, (0, 0))
            screen.blit(fade, (0, 0))
            pygame.display.update()
            pygame.time.delay(5)
    elif mode == "black_to_img_to_black":
        opacity = 300
        for r in range(300):
            opacity -= 1
            fade.set_alpha(opacity)
            screen.blit(image2, (0, 0))
            screen.blit(texte, texte_rect)
            screen.blit(fade, (0, 0))
            pygame.display.update()
            pygame.time.delay(5)
        pygame.time.delay(3000)
        for r in range(300):
            opacity += 1
            fade.set_alpha(opacity)
            screen.blit(image2, (0, 0))
            screen.blit(fade, (0, 0))
            pygame.display.update()
            pygame.time.delay(5)


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
        if dicKeys[K_ESCAPE] and ETAT == "jeu":
            changement_affichage()
            OF.save(DICT_VAR)
            GAME_RUNNING = False
            pygame.mixer.music.load("./sounds/main_theme.mp3")
            pygame.mixer.music.play(-1)
    pygame_widgets.update(events)
    pygame.display.flip()


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
        DICT_VAR = OF.load()
        print(DICT_VAR)
        HEROS.nom = DICT_VAR["nom_joueur"]
        match DICT_VAR["classe_joueur"]:
            case "guerrier":
                HEROS.classe = Ett.guerrier
                HEROS.pv_max = Ett.guerrier.pv_max
                HEROS.pc = Ett.guerrier.pc
                HEROS.pd = Ett.guerrier.pd
            case "archer":
                HEROS.classe = Ett.archer
                HEROS.pv_max = Ett.archer.pv_max
                HEROS.pc = Ett.archer.pc
                HEROS.pd = Ett.archer.pd
            case "tank":
                HEROS.classe = Ett.tank
                HEROS.pv_max = Ett.tank.pv_max
                HEROS.pc = Ett.tank.pc
                HEROS.pd = Ett.tank.pd
        match DICT_VAR["race_joueur"]:
            case "humain":
                HEROS.race = Ett.humain
                HEROS.pv_max += Ett.humain.pv_max
                HEROS.pc += Ett.humain.pc
                HEROS.pd += Ett.humain.pd
            case "elfe":
                HEROS.race = Ett.elfe
                HEROS.pv_max += Ett.elfe.pv_max
                HEROS.pc += Ett.elfe.pc
                HEROS.pd += Ett.elfe.pd
            case "orc":
                HEROS.race = Ett.orc
                HEROS.pv_max += Ett.orc.pv_max
                HEROS.pc += Ett.orc.pc
                HEROS.pd += Ett.orc.pd
        for elt in DICT_VAR["inventaire_joueur"]:
            if len(elt) == 6:
                new_conso = E.Consommable(elt[0], int(elt[1]), int(
                    elt[2]), int(elt[3]), int(elt[4]), elt[5])
            elif len(elt) == 5:
                new_conso = E.Consommable(elt[0], int(elt[1]), int(
                    elt[2]), int(elt[3]), elt[4])
            HEROS.inventaire.append(new_conso)
        HEROS.pv = int(DICT_VAR["pv_joueur"])
        HEROS.argent = int(DICT_VAR["argent_joueur"])
        lmg = DICT_VAR["main_gauche_joueur"]
        lmd = DICT_VAR["main_droite_joueur"]
        lte = DICT_VAR["tete_joueur"]
        lto = DICT_VAR["torse_joueur"]
        lg = DICT_VAR["gants_joueur"]
        lj = DICT_VAR["jambes_joueur"]
        lp = DICT_VAR["pieds_joueur"]
        if lmg != []:
            HEROS.main_gauche = E.Equipement(lmg[0], int(lmg[1]), int(
                lmg[2]), int(lmg[3]), lmg[4])
        if lmd != []:
            HEROS.main_droite = E.Equipement(lmd[0], int(lmd[1]), int(
                lmd[2]), int(lmd[3]), lmd[4])
        if lte != []:
            HEROS.tete = E.Equipement(lte[0], int(lte[1]), int(
                lte[2]), int(lte[3]), lte[4])
        if lto != []:
            HEROS.torse = E.Equipement(lto[0], int(lto[1]), int(
                lto[2]), int(lto[3]), lto[4])
        if lg != []:
            HEROS.gants = E.Equipement(lg[0], int(lg[1]), int(
                lg[2]), int(lg[3]), lg[4])
        if lj != []:
            HEROS.jambes = E.Equipement(lj[0], int(lj[1]), int(
                lj[2]), int(lj[3]), lj[4])
        if lp != []:
            HEROS.pieds = E.Equipement(lp[0], int(lp[1]), int(
                lp[2]), int(lp[3]), lp[4])
        AVANCEMENT = int(DICT_VAR["avancement"])
        changement_affichage()


def dict_var_update(dict_var: dict, heros: Ett.Joueur, avancement: int):
    '''Sauvegarde les valeurs des différentes variables dans le dictionnaire de sauvegarde'''
    def attribuer_equipement(partie_corps):
        if partie_corps == []:
            return []
        return [partie_corps.nom, int(partie_corps.atk), int(partie_corps.dfc), int(partie_corps.prix), partie_corps.cat]
    dict_var["nom_joueur"] = heros.nom
    dict_var["classe_joueur"] = heros.classe.nom
    dict_var["race_joueur"] = heros.race.nom
    for elt in heros.inventaire:
        list_temp = []
        list_temp.append(elt.nom)
        list_temp.append(elt.atk)
        list_temp.append(elt.dfc)
        if type(elt) == E.Consommable:
            list_temp.append(elt.heal)
        list_temp.append(elt.prix)
        list_temp.append(elt.cat)
        dict_var["inventaire_joueur"] = list_temp
    dict_var["pv_joueur"] = heros.pv
    dict_var["argent_joueur"] = heros.argent
    dict_var["sprite_joueur"] = heros.sprite
    dict_var["main_gauche_joueur"] = attribuer_equipement(heros.main_gauche)
    dict_var["main_droite_joueur"] = attribuer_equipement(heros.main_droite)
    dict_var["tete_joueur"] = attribuer_equipement(heros.tete)
    dict_var["torse_joueur"] = attribuer_equipement(heros.torse)
    dict_var["gants_joueur"] = attribuer_equipement(heros.gants)
    dict_var["jambes_joueur"] = attribuer_equipement(heros.jambes)
    dict_var["pieds_joueur"] = attribuer_equipement(heros.pieds)
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
    while GAME_RUNNING:
        match AVANCEMENT:
            case 0:
                pygame.mixer.music.load("./sounds/musique_jeu.mp3")
                pygame.mixer.music.play(-1)
                AVANCEMENT, HEROS = chapitre0(HEROS)
            case 1:
                pygame.mixer.music.load("./sounds/marchand_theme.mp3")
                pygame.mixer.music.play(-1)
                fade("black_to_img_to_black", "./img/chemin_fond_flou.png",
                     "./img/burning_village.jpg", "Chapitre 1 : L'aube de l'Éclipse")
                background = pygame.image.load("./img/pont_fond.jpg")
                background = pygame.transform.scale(
                    background, (window_width, window_height))
                screen.blit(background, (0, 0))
                AVANCEMENT, HEROS = chapitre1(HEROS)
            case 2:
                pygame.mixer.music.load("./sounds/musique_jeu.mp3")
                pygame.mixer.music.play(-1)
                background = pygame.image.load(
                    "img/chemin_fond.jpg").convert_alpha()
                background = pygame.transform.scale(
                    background, (window_width, window_height))
                screen.blit(background, (0, 0))
                AVANCEMENT = chapitre2()
            case 3:
                pygame.mixer.music.load("./sounds/marchand_theme.mp3")
                pygame.mixer.music.play(-1)
                background = pygame.image.load("./img/pont_fond.jpg")
                background = pygame.transform.scale(
                    background, (window_width, window_height))
                screen.blit(background, (0, 0))
                AVANCEMENT = chapitre3()
            case 4:
                pygame.mixer.music.load("./sounds/musique_jeu.mp3")
                pygame.mixer.music.play(-1)
                background = pygame.image.load(
                    "img/chemin_fond.jpg").convert_alpha()
                background = pygame.transform.scale(
                    background, (window_width, window_height))
                screen.blit(background, (0, 0))
                AVANCEMENT = chapitre4()
            case 5:
                pygame.mixer.music.load("./sounds/marchand_theme.mp3")
                pygame.mixer.music.play(-1)
                background = pygame.image.load("./img/pont_fond.jpg")
                background = pygame.transform.scale(
                    background, (window_width, window_height))
                screen.blit(background, (0, 0))
                AVANCEMENT = chapitre5()
            case 6:
                pygame.mixer.music.load("./sounds/musique_jeu.mp3")
                pygame.mixer.music.play(-1)
                background = pygame.image.load(
                    "img/chemin_fond.jpg").convert_alpha()
                background = pygame.transform.scale(
                    background, (window_width, window_height))
                screen.blit(background, (0, 0))
                AVANCEMENT = chapitre6()
            case 7:
                pygame.mixer.music.load("./sounds/marchand_theme.mp3")
                pygame.mixer.music.play(-1)
                background = pygame.image.load("./img/pont_fond.jpg")
                background = pygame.transform.scale(
                    background, (window_width, window_height))
                screen.blit(background, (0, 0))
                AVANCEMENT = chapitre7()
            case 8:
                pygame.mixer.music.load("./sounds/musique_jeu.mp3")
                pygame.mixer.music.play(-1)
                background = pygame.image.load(
                    "img/chemin_fond.jpg").convert_alpha()
                background = pygame.transform.scale(
                    background, (window_width, window_height))
                screen.blit(background, (0, 0))
                AVANCEMENT = chapitre8()
            case 9:
                pygame.mixer.music.load("./sounds/marchand_theme.mp3")
                pygame.mixer.music.play(-1)
                background = pygame.image.load("./img/pont_fond.jpg")
                background = pygame.transform.scale(
                    background, (window_width, window_height))
                screen.blit(background, (0, 0))
                AVANCEMENT = chapitre9()
            case 10:
                pygame.mixer.music.load("./sounds/musique_jeu.mp3")
                pygame.mixer.music.play(-1)
                background = pygame.image.load(
                    "img/chemin_fond.jpg").convert_alpha()
                background = pygame.transform.scale(
                    background, (window_width, window_height))
                screen.blit(background, (0, 0))
                AVANCEMENT = chapitre10()
                changement_affichage()
                GAME_RUNNING = False
            case _:
                check_events()
        DICT_VAR = dict_var_update(DICT_VAR, HEROS, AVANCEMENT)
        OF.save(DICT_VAR)
        check_events()


def chapitre0(heros: Ett.Joueur):
    '''Lance le chapitre d'introduction du jeu'''
    screen.fill(BLACK)
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
    done = False
    nom_heros = TB.textbox_input(
        "Veuillez entrer le nom de votre personnage : ")
    while not done:
        race_heros = ""
        choix_race = TB.textbox_input(
            "Veuillez selectionner une race parmi :@- 1 : humain@- 2 : elfe@- 3 : orc")
        if (choix_race) in ["1", "2", "3"]:
            done = True
            race_heros = int(choix_race)
    done = False
    while not done:
        classe_heros = ""
        choix_classe = TB.textbox_input(
            "Veuillez selectionner une classe parmi :@@- 1 : guerrier@- 2 : archer@- 3 : tank@@")
        if choix_classe in ["1", "2", "3"]:
            done = True
            classe_heros = int(choix_classe)

    # on crée un heros avec le X eme element de la liste des races/classes
    heros.nom = nom_heros
    heros.classe = Ett.liste_classe[int(classe_heros)-1]
    heros.race = Ett.liste_race[int(race_heros)-1]
    sprite = pygame.image.load(heros.update_sprite())
    screen.blit(sprite, (-window_width//6,
                # windwow_width//2 pour ennemi à droite
                         window_height-1.01*sprite.get_height()))
    TB.textbox_output("Vous etes : "+heros.nom+", de la race des "+heros.race.nom+", vous etes un futur " +
                      heros.classe.nom+" dont on racontera l'hisoire pendant des générations !")
    return (1, heros)


def chapitre1(heros: Ett.Joueur):
    '''Lance le chapitre 1 du jeu'''
    fade("black_to_img", "./img/burning_village.jpg")
    background = pygame.image.load(
        "./img/burning_village.jpg").convert_alpha()
    background = pygame.transform.scale(
        background, (window_width, window_height))
    screen.blit(background, (0, 0))

    TB.textbox_output("Vous vous réveillez en sursaut dans votre humble demeure, l'air empli de fumée et les cris déchirant la tranquillité de la nuit. Votre village est attaqué par des créatures mystérieuses, surgies des ombres. Vous entendez les hurlements de vos voisins et le rugissement des flammes qui dévorent les maisons autour de vous.")
    TB.textbox_output("Vous vous précipitez hors de votre maison, arme en main, prêt à défendre ce qui reste de votre foyer. Mais il est déjà trop tard. Les créatures, ressemblant à des ombres animées, ont réduit votre village en cendres. Seuls les souvenirs de vos proches perdurent dans votre esprit.")
    C.bataille(heros, Ett.Monstre(
        Ett.ombre_assaillante_classe, Ett.ombre_race))
    M.obt_objet(E.Consommable(
        "Petite potion de soin", 0, 0, 10, 10,  "soin"), heros)
    M.obt_objet(E.Consommable(
        "Petite potion de soin", 0, 0, 10, 10, "soin"), heros)
    TB.textbox_output("Après un combat acharné, vous parvenez à abattre l'une des créatures, mais vous réalisez que vous ne pouvez pas sauver ce qui reste du village. Vous devez fuir et trouver un endroit sûr.")
    background = pygame.image.load(
        "./img/chemin_pierre_runes.jpg").convert_alpha()
    background = pygame.transform.scale(
        background, (window_width, window_height))
    screen.blit(background, (0, 0))
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
                    25, 0, 30, "main_droite"), heros)

    if choix == "2":
        TB.textbox_output("2. Ignorer les symboles et avancer dans la forêt :@ Vous choisissez de ne pas suivre le sentier et de continuer votre chemin dans la forêt. Plus loin, vous trouvez une cachette naturelle sous un arbre colossal. En fouillant, vous découvrez un vieux sac contenant un arc en bois sombre et un carquois rempli de flèches enchantées. Vous vous équipez de l'arc, sentant une connexion immédiate avec l'arme.")
        M.obt_objet(E.Equipement("Arc", 30, 0, 15, "main_droite"), heros)

    TB.textbox_output("Vous continuez votre marche, les ténèbres de la forêt vous enveloppant. Chaque pas que vous faites vous éloigne un peu plus de votre passé et vous rapproche de la vérité sur cette éclipse mystérieuse et des créatures qui ont ravagé votre village. ")
    TB.textbox_output(
        "La quête pour découvrir la source de cette malédiction et venger votre foyer commence maintenant.")
    M.ouvertureDeLaBoutique(
        heros, 1, [(E.Consommable("Petite potion de force", 5, 5, 0, 10, "attaque"))])
    return 2, heros


def chapitre2(heros: Ett.Joueur):
    '''Lance le chapitre 2 du jeu'''
    TB.textbox_output("Après avoir échappé à l'attaque de votre village, vous errez dans la forêt pendant plusieurs jours, cherchant des réponses et un refuge. Les arbres s'éclaircissent finalement, révélant une vallée cachée où se dressent les ruines d'une civilisation ancienne, à moitié enfouies sous la végétation.")
    TB.textbox_output("Vous avancez prudemment parmi les pierres effondrées et les colonnes brisées, sentant l'aura mystique qui émane de cet endroit oublié. Des fresques murales racontent l'histoire d'un royaume autrefois prospère, détruit par une force obscure similaire à celle qui a attaqué votre village. Vous comprenez que ces ruines détiennent des secrets vitaux pour votre quête.")
    TB.textbox_output("Soudain, des bruits étranges retentissent autour de vous. Des silhouettes se déplacent parmi les décombres. Vous vous cachez derrière une colonne et observez des créatures humanoïdes aux yeux brillants, gardant les lieux.")
    C.bataille(heros, Ett.Monstre(
        Ett.Garde_squelette_classe, Ett.squelette_race))
    M.obt_objet(E.Consommable("Petite potion de force",
                5, 5, 0, 10, "attaque"), heros)
    M.obt_objet(E.Equipement("Heaume Basique",
                0, 5, 10, "tete"), heros)
    M.obt_objet(E.Equipement("Plastron Basique",
                             0, 7, 10, "torse"), heros)
    M.obt_objet(E.Equipement("Jambières Basique",
                             0, 5, 10, "jambes"), heros)
    M.obt_objet(E.Equipement("Bottes Basique",
                             0, 3, 10, "pieds"), heros)
    M.ouvertureDeLaBoutique(
        heros, 1, [(E.Consommable("Petite potion de force", 5, 5, 0, 10, "attaque"))])
    TB.textbox_output("Après avoir vaincu l'un des gardes squelettiques, vous fouillez les ruines à la recherche d'indices. Vous tombez sur une chambre secrète, protégée par un mécanisme complexe.")
    done = False
    choix = ""
    while not done:
        TB.textbox_output(
            "Choix: @ - 1 : Résoudre l'énigme du mécanisme@- 2 : Forcer l'entrée")
        if choix in ["1", "2"]:
            done = True
    if choix == "1":
        TB.textbox_output("1. Résoudre l'énigme du mécanisme :@Vous examinez le mécanisme et remarquez des symboles similaires à ceux vus dans la forêt. En manipulant soigneusement les pièces mobiles, vous parvenez à déverrouiller la porte. À l'intérieur, vous trouvez une amulette ancienne, gravée de runes protectrices. En la mettant autour de votre cou, vous ressentez un pouvoir de protection et de clairvoyance.")

        M.obt_objet(E.Equipement("Amulette de clairevoyance",
                    0, 8, 10, "tete"), heros)
        if choix == "2":
            TB.textbox_output("2. Forcer l'entrée :@Impatient, vous décidez de forcer l'entrée en utilisant votre force et vos armes. Après plusieurs essais, la porte finit par céder. À l'intérieur, vous trouvez une épée en cristal, légèrement fissurée mais encore imprégnée d'une énergie redoutable. L'épée vibre légèrement entre vos mains, comme si elle reconnaissait votre détermination.")
            M.obt_objet(E.Equipement("épé de cristal",
                        40, 0, 15, "main_droite"), heros)
    TB.textbox_output("Avec votre nouvelle acquisition, vous continuez à explorer les ruines. Vous trouvez finalement un ancien grimoire, contenant des histoires et des prophéties sur l'éclipse et les créatures des ombres. En le feuilletant, vous apprenez qu'un artefact puissant, capable de contrôler ou détruire ces créatures, est caché quelque part dans le royaume.")
    TB.textbox_output("Votre quête prend une nouvelle tournure. Armé de nouvelles connaissances et de puissants artefacts, vous quittez les ruines et vous vous enfoncez plus profondément dans la vallée, déterminé à trouver cet artefact avant qu'il ne soit trop tard.")
    return 3, heros


def chapitre3(heros: Ett.Joueur):
    '''Lance le chapitre 3 du jeu'''
    TB.textbox_output("Vous venez de passer au chapitre 3.")

    return 4, heros


def chapitre4(heros: Ett.Joueur):
    '''Lance le chapitre 4 du jeu'''
    TB.textbox_output("Vous venez de passer au chapitre 4.")
    return 5, heros


def chapitre5(heros: Ett.Joueur):
    '''Lance le chapitre 5 du jeu'''
    TB.textbox_output("Vous venez de passer au chapitre 5.")
    return 6, heros


def chapitre6(heros: Ett.Joueur):
    '''Lance le chapitre 6 du jeu'''
    TB.textbox_output("Vous venez de passer au chapitre 6.")
    return 7, heros


def chapitre7(heros: Ett.Joueur):
    '''Lance le chapitre 7 du jeu'''
    TB.textbox_output("Vous venez de passer au chapitre 7.")
    return 8, heros


def chapitre8(heros: Ett.Joueur):
    '''Lance le chapitre 8 du jeu'''
    TB.textbox_output("Vous venez de passer au chapitre 8.")
    return 9, heros


def chapitre9(heros: Ett.Joueur):
    '''Lance le chapitre 9 du jeu'''
    TB.textbox_output("Vous venez de passer au chapitre 9.")
    return 10, heros


def chapitre10(heros: Ett.Joueur):
    '''Lance le chapitre 10 du jeu'''
    TB.textbox_output("Vous venez de passer au chapitre 10.")
    TB.textbox_output("Merci d'avoir joué")
    TB.textbox_output("Fin de la partie")
    return 10


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
    "sprite_joueur": "",
    "main_gauche_joueur": [],
    "main_droite_joueur": [],
    "tete_joueur": [],
    "torse_joueur": [],
    "gants_joueur": [],
    "jambes_joueur": [],
    "pieds_joueur": [],
    "avancement": 0
}
ETAT = "ecran_titre"    # Variable de sélection de menus : ecran_titre / jeu
GAME_RUNNING = False    # Variable qui indique si le jeu tourne ou non
AVANCEMENT = 0
HEROS = Ett.Joueur("", Ett.guerrier, Ett.humain)
HEROS.main_gauche = E.Equipement("épée", 5, 0, 5, "arme")

pygame.init()
pygame.mixer_music.load("./sounds/title_theme.mp3")
pygame.mixer.music.play(-1)
pygame.display.set_caption("Les Royaumes de l'Éclipse")
pygame.key.set_repeat(400, 30)
pygame.display.set_icon(ICON)
window_width, window_height = dimensions_ecran()
button_w, button_h = 350, 80
screen = pygame.display.set_mode((window_width, window_height))

fade("black_to_img", "./img/chemin_fond_flou.png")
while RUNNING:
    if ETAT == "ecran_titre":
        ecran_titre()
    elif ETAT == "jeu":
        jeu()
