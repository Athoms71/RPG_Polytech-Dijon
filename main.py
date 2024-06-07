import entite as Ett
import textbox as TB
import operation_fichier as OF
import os
import pygame
from pygame.locals import *
import pygame_widgets
from pygame_widgets.button import Button


def dimensions_ecran():
    screen_info = pygame.display.Info()
    screen_width = screen_info.current_w
    screen_height = screen_info.current_h
    return (screen_width, screen_height)


def check_events():
    global ETAT
    global GAME_RUNNING
    global SAVE_LIST
    events = pygame.event.get()
    for event in events:
        dicKeys = pygame.key.get_pressed()
        if event.type == QUIT or dicKeys[K_TAB]:
            fin_fenetre()
        if dicKeys[K_ESCAPE] and ETAT == "jeu":
            changement_affichage()
            OF.save(SAVE_LIST)
            GAME_RUNNING = False
            pygame.mixer.music.load("./sounds/main_theme.mp3")
            pygame.mixer.music.play(-1)
    pygame_widgets.update(events)
    pygame.display.flip()


def fin_fenetre():
    global RUNNING
    RUNNING = False
    pygame.quit()
    pygame.mixer.quit()
    quit()


def changement_affichage():
    global ETAT
    if ETAT == "ecran_titre":
        ETAT = "jeu"
    elif ETAT == "jeu":
        ETAT = "ecran_titre"


def nouvelle_partie():
    if os.path.exists("save.txt"):
        os.remove("save.txt")
    changement_affichage()


def continuer_partie():
    global DICT_VAR
    if os.path.exists("save.txt"):
        DICT_VAR = OF.load()
        # Affectation des valeurs aux variables du jeu
        changement_affichage()


# Affichage de l'écran titre
def ecran_titre():
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
    global GAME_RUNNING
    GAME_RUNNING = True
    avancement = 0
    while GAME_RUNNING:
        match avancement:
            case 0:
                pygame.mixer.music.load("./sounds/musique_jeu.mp3")
                pygame.mixer.music.play(-1)
                background = pygame.image.load(
                    "img/chemin_fond_flou.png").convert_alpha()
                background = pygame.transform.scale(
                    background, (window_width, window_height))
                screen.blit(background, (0, 0))
                avancement = chapitre0()
            case 1:
                pygame.mixer.music.load("./sounds/marchand_theme.mp3")
                pygame.mixer.music.play(-1)
                background = pygame.image.load("./img/pont_fond.jpg")
                background = pygame.transform.scale(
                    background, (window_width, window_height))
                screen.blit(background, (0, 0))
                avancement = chapitre1()
            case _:
                check_events()
        check_events()


def chapitre0():
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
    return 1


def chapitre1():
    TB.textbox_output("Vous venez de passer au chapitre 1.")
    TB.textbox_output("Appuyez sur Tab pour quitter le jeu")


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
DICT_VAR = {}           # Dictionnaire de sauvegarde
ETAT = "ecran_titre"    # Variable de sélection de menus : ecran_titre / jeu
GAME_RUNNING = False    # Variable qui indique si le jeu tourne ou non

while RUNNING:
    if ETAT == "ecran_titre":
        ecran_titre()
    elif ETAT == "jeu":
        jeu()
    elif ETAT == "menu_pause":
        pass
