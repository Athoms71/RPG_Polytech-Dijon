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
                    "img/chemin_fond.jpg").convert_alpha()
                background = pygame.transform.scale(
                    background, (window_width, window_height))
                screen.blit(background, (0, 0))
                avancement, hero = chapitre0()
            case 1:
                pygame.mixer.music.load("./sounds/marchand_theme.mp3")
                pygame.mixer.music.play(-1)
                background = pygame.image.load("./img/pont_fond.jpg")
                background = pygame.transform.scale(
                    background, (window_width, window_height))
                screen.blit(background, (0, 0))
                avancement = chapitre1(hero)
            case 2:
                pygame.mixer.music.load("./sounds/musique_jeu.mp3")
                pygame.mixer.music.play(-1)
                background = pygame.image.load(
                    "img/chemin_fond.jpg").convert_alpha()
                background = pygame.transform.scale(
                    background, (window_width, window_height))
                screen.blit(background, (0, 0))
                avancement = chapitre2()
            case 3:
                pygame.mixer.music.load("./sounds/marchand_theme.mp3")
                pygame.mixer.music.play(-1)
                background = pygame.image.load("./img/pont_fond.jpg")
                background = pygame.transform.scale(
                    background, (window_width, window_height))
                screen.blit(background, (0, 0))
                avancement = chapitre3()
            case 4:
                pygame.mixer.music.load("./sounds/musique_jeu.mp3")
                pygame.mixer.music.play(-1)
                background = pygame.image.load(
                    "img/chemin_fond.jpg").convert_alpha()
                background = pygame.transform.scale(
                    background, (window_width, window_height))
                screen.blit(background, (0, 0))
                avancement = chapitre4()
            case 5:
                pygame.mixer.music.load("./sounds/marchand_theme.mp3")
                pygame.mixer.music.play(-1)
                background = pygame.image.load("./img/pont_fond.jpg")
                background = pygame.transform.scale(
                    background, (window_width, window_height))
                screen.blit(background, (0, 0))
                avancement = chapitre5()
            case 6:
                pygame.mixer.music.load("./sounds/musique_jeu.mp3")
                pygame.mixer.music.play(-1)
                background = pygame.image.load(
                    "img/chemin_fond.jpg").convert_alpha()
                background = pygame.transform.scale(
                    background, (window_width, window_height))
                screen.blit(background, (0, 0))
                avancement = chapitre6()
            case 7:
                pygame.mixer.music.load("./sounds/marchand_theme.mp3")
                pygame.mixer.music.play(-1)
                background = pygame.image.load("./img/pont_fond.jpg")
                background = pygame.transform.scale(
                    background, (window_width, window_height))
                screen.blit(background, (0, 0))
                avancement = chapitre7()
            case 8:
                pygame.mixer.music.load("./sounds/musique_jeu.mp3")
                pygame.mixer.music.play(-1)
                background = pygame.image.load(
                    "img/chemin_fond.jpg").convert_alpha()
                background = pygame.transform.scale(
                    background, (window_width, window_height))
                screen.blit(background, (0, 0))
                avancement = chapitre8()
            case 9:
                pygame.mixer.music.load("./sounds/marchand_theme.mp3")
                pygame.mixer.music.play(-1)
                background = pygame.image.load("./img/pont_fond.jpg")
                background = pygame.transform.scale(
                    background, (window_width, window_height))
                screen.blit(background, (0, 0))
                avancement = chapitre9()
            case 10:
                pygame.mixer.music.load("./sounds/musique_jeu.mp3")
                pygame.mixer.music.play(-1)
                background = pygame.image.load(
                    "img/chemin_fond.jpg").convert_alpha()
                background = pygame.transform.scale(
                    background, (window_width, window_height))
                screen.blit(background, (0, 0))
                avancement = chapitre10()
            case -1:
                print("Fin du jeu")
                check_events()
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

    # on crée un hero avec le X eme element de la liste des races/classes
    hero = Ett.Joueur(nom, Ett.liste_classe[int(
        classe)-1], Ett.liste_race[int(race)-1])
    TB.textbox_output("Vous etes : "+hero.nom+", de la race des "+hero.race+", vous etes un futur " +
                      hero.classe+" dont on racontera l'hisoire pendant des générations !")
    return (1, hero)


def chapitre1(hero: Ett.Joueur):
    M.ouvertureDeLaBoutique(
        hero, 1, [E.Equipement("Arc", 40, 0, 15, 5, "main_droite"),
                  E.Equipement("Petite potion de soin", 0, 0, 5, 5, "soin")])
    TB.textbox_output("Vous vous réveillez en sursaut dans votre humble demeure, l'air empli de fumée et les cris déchirant la tranquillité de la nuit. Votre village est attaqué par des créatures mystérieuses, surgies des ombres. Vous entendez les hurlements de vos voisins et le rugissement des flammes qui dévorent les maisons autour de vous.")
    TB.textbox_output("Vous vous précipitez hors de votre maison, arme en main, prêt à défendre ce qui reste de votre foyer. Mais il est déjà trop tard. Les créatures, ressemblant à des ombres animées, ont réduit votre village en cendres. Seuls les souvenirs de vos proches perdurent dans votre esprit.")
    ombreAssayante = Ett.Monstre(Ett.ombre_assayante_classe, Ett.ombre_race)
    C.bataille(hero, ombreAssayante)
    TB.textbox_output("Après un combat acharné, vous parvenez à abattre l'une des créatures, mais vous réalisez que vous ne pouvez pas sauver ce qui reste du village. Vous devez fuir et trouver un endroit sûr.")
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
                    35, 0, 30, 5, "main_droite"), hero)

    if choix == "2":
        TB.textbox_output("2. Ignorer les symboles et avancer dans la forêt :@ Vous choisissez de ne pas suivre le sentier et de continuer votre chemin dans la forêt. Plus loin, vous trouvez une cachette naturelle sous un arbre colossal. En fouillant, vous découvrez un vieux sac contenant un arc en bois sombre et un carquois rempli de flèches enchantées. Vous vous équipez de l'arc, sentant une connexion immédiate avec l'arme.")
        M.obt_objet(E.Equipement("Arc", 40, 0, 15, 5, "main_droite"), hero)

    TB.textbox_output("Vous continuez votre marche, les ténèbres de la forêt vous enveloppant. Chaque pas que vous faites vous éloigne un peu plus de votre passé et vous rapproche de la vérité sur cette éclipse mystérieuse et des créatures qui ont ravagé votre village. ")
    TB.textbox_output(
        "La quête pour découvrir la source de cette malédiction et venger votre foyer commence maintenant.")
    M.ouvertureDeLaBoutique(hero, 1)
    return 2, hero


def chapitre2():
    TB.textbox_output("Vous venez de passer au chapitre 2.")
    return 3


def chapitre3():
    TB.textbox_output("Vous venez de passer au chapitre 3.")
    return 4


def chapitre4():
    TB.textbox_output("Vous venez de passer au chapitre 4.")
    return 5


def chapitre5():
    TB.textbox_output("Vous venez de passer au chapitre 5.")
    return 6


def chapitre6():
    TB.textbox_output("Vous venez de passer au chapitre 6.")
    return 7


def chapitre7():
    TB.textbox_output("Vous venez de passer au chapitre 7.")
    return 8


def chapitre8():
    TB.textbox_output("Vous venez de passer au chapitre 8.")
    return 9


def chapitre9():
    TB.textbox_output("Vous venez de passer au chapitre 9.")
    return 10


def chapitre10():
    TB.textbox_output("Vous venez de passer au chapitre 10.")
    TB.textbox_output("Appuyez sur Tab pour quitter le jeu")
    return -1


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
