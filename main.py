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
        HEROS.nom = DICT_VAR["nom_joueur"]
        HEROS.classe = DICT_VAR["classe_joueur"]
        HEROS.race = DICT_VAR["race_joueur"]
        HEROS.inventaire = DICT_VAR["inventaire_joueur"]
        HEROS.pv = int(DICT_VAR["pv_joueur"])
        HEROS.argent = int(DICT_VAR["argent_joueur"])
        HEROS.main_gauche = DICT_VAR["main_gauche_joueur"]
        HEROS.main_droite = DICT_VAR["main_droite_joueur"]
        HEROS.tete = DICT_VAR["tete_joueur"]
        HEROS.torse = DICT_VAR["torse_joueur"]
        HEROS.gants = DICT_VAR["gants_joueur"]
        HEROS.jambes = DICT_VAR["jambes_joueur"]
        HEROS.pieds = DICT_VAR["pieds_joueur"]
        AVANCEMENT = int(DICT_VAR["avancement"])
        changement_affichage()


def dict_var_update(dict_var: dict, heros: Ett.Joueur, avancement: int):
    '''Sauvegarde les valeurs des différentes variables dans le dictionnaire de sauvegarde'''
    dict_var["nom_joueur"] = heros.nom
    dict_var["classe_joueur"] = heros.classe
    dict_var["race_joueur"] = heros.race
    dict_var["inventaire_joueur"] = heros.inventaire
    dict_var["pv_joueur"] = heros.pv
    dict_var["argent_joueur"] = heros.argent
    dict_var["main_gauche_joueur"] = heros.main_gauche
    dict_var["main_droite_joueur"] = heros.main_droite
    dict_var["tete_joueur"] = heros.tete
    dict_var["torse_joueur"] = heros.torse
    dict_var["gants_joueur"] = heros.gants
    dict_var["jambes_joueur"] = heros.jambes
    dict_var["pieds_joueur"] = heros.pieds
    dict_var["avancement"] = avancement
    return dict_var


def ecran_titre():
    '''Affiche l'écran titre'''
    global ICON
    button_font = pygame.font.Font(
        "./font/VecnaBold-4YY4.ttf", 45)
    title_font = pygame.font.Font(
        "./font/VecnaBold-4YY4.ttf", 105)
    title_text = title_font.render(
        "Les Royaumes de l'Éclipse", True, WHITE)
    title_rect = title_text.get_rect(
        center=(window_width//2+button_w//3, window_height//4))
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
    screen.blit(title_text, title_rect)
    screen.blit(ICON, (button_w//3, window_height//5-button_h//2))
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
                AVANCEMENT, HEROS = chapitre0()
            case 1:
                pygame.mixer.music.load("./sounds/marchand_theme.mp3")
                pygame.mixer.music.play(-1)
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


def chapitre0():
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
    nom = TB.textbox_input("Veuillez entrer le nom de votre personnage : ")
    while not done:
        race = ""
        choix_race = TB.textbox_input(
            "Veuillez selectionner une race parmi :@- 1 : humain@- 2 : elfe@- 3 : orc")
        if (choix_race) in ["1", "2", "3"]:
            done = True
            race = int(choix_race)
    done = False
    while not done:
        classe = ""
        choix_classe = TB.textbox_input(
            "Veuillez selectionner une classe parmi :@@- 1 : guerrier@- 2 : archer@- 3 : tank@@")
        if choix_classe in ["1", "2", "3"]:
            done = True
            classe = int(choix_classe)

    # on crée un heros avec le X eme element de la liste des races/classes
    heros = Ett.Joueur(nom, Ett.liste_classe[int(
        classe)-1], Ett.liste_race[int(race)-1])
    TB.textbox_output("Vous etes : "+heros.nom+", de la race des "+heros.race+", vous etes un futur " +
                      heros.classe+" dont on racontera l'hisoire pendant des générations !")
    return (1, heros)


def chapitre1(heros: Ett.Joueur):
    '''Lance le chapitre 1 du jeu'''
    background = pygame.image.load(
        "./img/burning_village.jpg").convert_alpha()
    background = pygame.transform.scale(
        background, (window_width, window_height))
    screen.blit(background, (0, 0))
    M.obt_objet(E.Consommable("Petite potion de force",
                5, 5, 0, 10, 10, "attaque"), heros)
    M.obt_objet(E.Consommable("Petite potion de force",
                5, 5, 0, 10, 10, "attaque"), heros)
    M.ouvertureDeLaBoutique(
        heros, 1, [(E.Consommable("Petite potion de force", 5, 5, 0, 10, 10, "attaque"))])

    TB.textbox_output("Vous vous réveillez en sursaut dans votre humble demeure, l'air empli de fumée et les cris déchirant la tranquillité de la nuit. Votre village est attaqué par des créatures mystérieuses, surgies des ombres. Vous entendez les hurlements de vos voisins et le rugissement des flammes qui dévorent les maisons autour de vous.")
    TB.textbox_output("Vous vous précipitez hors de votre maison, arme en main, prêt à défendre ce qui reste de votre foyer. Mais il est déjà trop tard. Les créatures, ressemblant à des ombres animées, ont réduit votre village en cendres. Seuls les souvenirs de vos proches perdurent dans votre esprit.")
    ombreAssayante = Ett.Monstre(Ett.ombre_assayante_classe, Ett.ombre_race)
    C.bataille(heros, ombreAssayante)
    M.obt_objet(E.Consommable(
        "Petite potion de soin", 0, 0, 10, 10, 10,  "soin"), heros)
    M.obt_objet(E.Consommable(
        "Petite potion de soin", 0, 0, 10, 10, 10, "soin"), heros)
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
                    35, 0, 30, 5, "main_droite"), heros)

    if choix == "2":
        TB.textbox_output("2. Ignorer les symboles et avancer dans la forêt :@ Vous choisissez de ne pas suivre le sentier et de continuer votre chemin dans la forêt. Plus loin, vous trouvez une cachette naturelle sous un arbre colossal. En fouillant, vous découvrez un vieux sac contenant un arc en bois sombre et un carquois rempli de flèches enchantées. Vous vous équipez de l'arc, sentant une connexion immédiate avec l'arme.")
        M.obt_objet(E.Equipement("Arc", 40, 0, 15, 5, "main_droite"), heros)

    TB.textbox_output("Vous continuez votre marche, les ténèbres de la forêt vous enveloppant. Chaque pas que vous faites vous éloigne un peu plus de votre passé et vous rapproche de la vérité sur cette éclipse mystérieuse et des créatures qui ont ravagé votre village. ")
    TB.textbox_output(
        "La quête pour découvrir la source de cette malédiction et venger votre foyer commence maintenant.")
    M.ouvertureDeLaBoutique(
        heros, 1, [(E.Consommable("Petite potion de force", 5, 5, 0, 10, 10, "attaque"))])
    return 2, heros


def chapitre2():
    '''Lance le chapitre 2 du jeu'''
    TB.textbox_output("Vous venez de passer au chapitre 2.")
    return 3


def chapitre3():
    '''Lance le chapitre 3 du jeu'''
    TB.textbox_output("Vous venez de passer au chapitre 3.")
    return 4


def chapitre4():
    '''Lance le chapitre 4 du jeu'''
    TB.textbox_output("Vous venez de passer au chapitre 4.")
    return 5


def chapitre5():
    '''Lance le chapitre 5 du jeu'''
    TB.textbox_output("Vous venez de passer au chapitre 5.")
    return 6


def chapitre6():
    '''Lance le chapitre 6 du jeu'''
    TB.textbox_output("Vous venez de passer au chapitre 6.")
    return 7


def chapitre7():
    '''Lance le chapitre 7 du jeu'''
    TB.textbox_output("Vous venez de passer au chapitre 7.")
    return 8


def chapitre8():
    '''Lance le chapitre 8 du jeu'''
    TB.textbox_output("Vous venez de passer au chapitre 8.")
    return 9


def chapitre9():
    '''Lance le chapitre 9 du jeu'''
    TB.textbox_output("Vous venez de passer au chapitre 9.")
    return 10


def chapitre10():
    '''Lance le chapitre 10 du jeu'''
    TB.textbox_output("Vous venez de passer au chapitre 10.")
    TB.textbox_output("Merci d'avoir joué")
    TB.textbox_output("Fin de la partie")
    return 10


pygame.init()
pygame.mixer_music.load("./sounds/title_theme.mp3")
pygame.mixer.music.play(-1)
pygame.display.set_caption("Les Royaumes de l'Éclipse")
pygame.key.set_repeat(400, 30)
ICON = pygame.image.load("img/logo.png").convert_alpha()
pygame.display.set_icon(ICON)
window_width, window_height = dimensions_ecran()
button_w, button_h = 350, 80
screen = pygame.display.set_mode((window_width, window_height))

# Variables globales
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
    "main_gauche_joueur": None,
    "main_droite_joueur": None,
    "tete_joueur": None,
    "torse_joueur": None,
    "gants_joueur": None,
    "jambes_joueur": None,
    "pieds_joueur": None,
    "avancement": 0
}
ETAT = "ecran_titre"    # Variable de sélection de menus : ecran_titre / jeu
GAME_RUNNING = False    # Variable qui indique si le jeu tourne ou non
AVANCEMENT = 0
HEROS = Ett.Joueur("", Ett.guerrier, Ett.humain)

while RUNNING:
    if ETAT == "ecran_titre":
        ecran_titre()
    elif ETAT == "jeu":
        jeu()
