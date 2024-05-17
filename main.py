import entite as Ett
import chapitre_0 as C0
import chapitre_1 as C1
import pygame
from pygame.locals import *
import pygame_widgets
from pygame_widgets.button import Button

pygame.init()
pygame.mixer_music.load("./sounds/main_theme.mp3")
pygame.mixer.music.play(loops=-1)
pygame.display.set_caption("Les Royaumes de l'Éclipse")
pygame.key.set_repeat(400, 30)
icon = pygame.image.load("img/logo.png").convert_alpha()
pygame.display.set_icon(icon)

# Variables globales
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def dimensions_ecran():
    screen_info = pygame.display.Info()
    screen_width = screen_info.current_w
    screen_height = screen_info.current_h
    return (screen_width, screen_height)


def changement_affichage():
    global afficher
    if afficher == ecran_titre:
        afficher = game
        game()
    if afficher == game:
        afficher = ecran_titre
        ecran_titre()


def game():
    C0.intro()
    events = pygame.event.get()
    for event in events:
        dicKeys = pygame.key.get_pressed()
        if event.type == QUIT or dicKeys[K_ESCAPE]:
            fin_fenetre()
    pygame_widgets.update(events)
    pygame.display.flip()


def check_events():
    events = pygame.event.get()
    for event in events:
        dicKeys = pygame.key.get_pressed()
        if event.type == QUIT or dicKeys[K_TAB]:
            fin_fenetre()
    pygame_widgets.update(events)
    pygame.display.flip()


def fin_fenetre():
    global RUNNING
    RUNNING = False
    pygame.quit()
    pygame.mixer.quit()
    quit()


def ecran_titre():
    global ICON
    global RUNNING
    button_w, button_h = 350, 80
    button_font = pygame.font.Font("font/TheWildBreathOfZelda-15Lv.ttf", 50)
    title_font = pygame.font.Font("font/TheWildBreathOfZelda-15Lv.ttf", 125)
    title_text = title_font.render("Les Royaumes de l'Eclipse", True, WHITE)
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
        onClick=start_game
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
        radius=10
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
        onClick=fin_fenetre)
    background = pygame.image.load("img/chemin_fond_flou.png").convert_alpha()
    background = pygame.transform.scale(
        background, (window_width, window_height))
    ICON = pygame.transform.scale(ICON, (window_height//5, window_height//5))
    screen.blit(background, (0, 0))
    screen.blit(title_text, title_rect)
    screen.blit(ICON, (2*button_w//3, window_height//5-button_h//2))
    check_events()


window_width, window_height = dimensions_ecran()
screen = pygame.display.set_mode((window_width, window_height))
background = pygame.image.load("img/chemin_fond_flou.png").convert()
background = pygame.transform.scale(background, (window_width, window_height))


keep_screen = True
menu_actuel = 0

while RUNNING:
    afficher()
