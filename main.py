import entite as Ett
import chapitre_0 as C0
import chapitre_1 as C1
import pygame
from pygame.locals import *
import pygame_widgets
from pygame_widgets.button import Button

pygame.init()
pygame.display.set_caption("Les Royaumes de l'Éclipse")
pygame.key.set_repeat(400, 30)

# Variables globales
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def dimensions_ecran():
    screen_info = pygame.display.Info()
    screen_width = screen_info.current_w
    screen_height = screen_info.current_h
    return (screen_width, screen_height)


def start_game():
    # A coder, au clic du bouton jouer du menu d'accueil
    print("Start")
    global background
    global button_play
    global button_settings
    global button_quit
    global menu_actuel
    button_play._width, button_play._height, button_play._x, button_play._y = 0, 0, window_width+10, window_height+10
    button_settings._width, button_settings._height, button_settings._x, button_settings._y = 0, 0, window_width+10, window_height+10
    button_quit._width, button_quit._height, button_quit._x, button_quit._y = 0, 0, window_width+10, window_height+10
    menu_actuel = 1
    return menu_actuel


def fin_fenetre():
    global keep_screen
    keep_screen = False


def ecran_titre():
    button_w, button_h = window_width//5, 80
    button_font = pygame.font.Font("font/TheWildBreathOfZelda-15Lv.ttf", 50)
    title_font = pygame.font.Font("font/TheWildBreathOfZelda-15Lv.ttf", 125)
    title_text = title_font.render("Les Royaumes de l'Eclipse", True, WHITE)
    title_rect = title_text.get_rect(
        center=(window_width//2, window_height//4))
    button_play = Button(
        screen,
        window_width//2-button_w//2,
        2*window_height//5,
        button_w,
        button_h,

        text="Jouer",
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
    button_settings = Button(
        screen,
        window_width//2-button_w//2,
        2*window_height//5+button_h+50,
        button_w,
        button_h,

        text="Parametres",
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
    icon = pygame.transform.scale(icon, (window_height//5, window_height//5))
    screen.blit(background, (0, 0))
    screen.blit(title_text, title_rect)
    screen.blit(icon, (2*button_w//3, window_height//5-button_h//2))
    pygame_widgets.update(pygame.event.get())
    pygame.display.flip()


window_width, window_height = dimensions_ecran()
screen = pygame.display.set_mode((window_width, window_height))
background = pygame.image.load("img/chemin_fond_flou.png").convert()
background = pygame.transform.scale(background, (window_width, window_height))


keep_screen = True
menu_actuel = 0

while keep_screen:
    events = pygame.event.get()
    for event in events:
        dicKeys = pygame.key.get_pressed()
        if event.type == QUIT or dicKeys[K_TAB]:
            pygame.quit()
            quit()
    pygame_widgets.update(events)
    pygame.display.flip()


'''def scenario(chapitre: int, karma: int):
    """lance la partie du scenario correspondant au chapitre en cours, et la voie empruniée jusqu"a présent"""
    if chapitre == 0:
        C0.intro()
        chapitre += 1
    if chapitre == 1:
        C1.ch1()'''
