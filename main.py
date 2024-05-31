import chapitre_0 as C0
import chapitre_1 as C1
import operation_fichier as OF
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
        print("Nouvelle partie")
    elif ETAT == "ecran_titre" and OF.exists("save.txt"):
        ETAT = "jeu"
        print("Partie chargée")
    elif ETAT == "jeu":
        ETAT = "ecran_titre"


pygame.init()
pygame.mixer_music.load("./sounds/main_theme.mp3")
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
WHITE = (255, 255, 255)
ETAT = "ecran_titre"    # Variable de sélection de menus : ecran_titre / jeu
GAME_RUNNING = False    # Variable qui indique si le jeu tourne ou non
SAVE_LIST = []


# Affichage de l'écran titre
def ecran_titre():
    global ICON
    button_font = pygame.font.Font(
        "font/TheWildBreathOfZelda-15Lv.ttf", 50)
    title_font = pygame.font.Font(
        "font/TheWildBreathOfZelda-15Lv.ttf", 125)
    title_text = title_font.render(
        "Les Royaumes de l'Eclipse", True, WHITE)
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
        onClick=changement_affichage
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
        onClick=changement_affichage
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
    pygame.mixer.music.load("./sounds/musique_jeu.mp3")
    pygame.mixer.music.play(-1)
    while GAME_RUNNING:
        screen.fill((255, 0, 0))
        check_events()


while RUNNING:
    if ETAT == "ecran_titre":
        ecran_titre()
    elif ETAT == "jeu":
        jeu()
    elif ETAT == "menu_pause":
        pass
