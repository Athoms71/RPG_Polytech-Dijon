import entite as Ett
import chapitre_0 as C0
import chapitre_1 as C1
import pygame
from pygame.locals import *
import pygame_widgets
from pygame_widgets.button import Button

pygame.init()
pygame.display.set_caption("Les Royaumes de l'Éclipse")
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


def fin_fenetre():
    global RUNNING
    RUNNING = False
    pygame.quit()
    quit()


def ecran_titre():
    global icon
    button_w, button_h = 300, 80
    button_font = pygame.font.Font("font/TheWildBreathOfZelda-15Lv.ttf", 50)
    title_font = pygame.font.Font("font/TheWildBreathOfZelda-15Lv.ttf", 100)
    title_text = title_font.render("Les Royaumes de l'Eclipse", True, WHITE)
    title_rect = title_text.get_rect(
        center=(window_width//2+button_w//3, window_height//4))
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
        inactiveColour=(255, 255, 255),
        hoverColour=(210, 210, 210),
        radius=10,
        onClick=changement_affichage
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
        inactiveColour=(255, 255, 255),
        hoverColour=(210, 210, 210),
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

RUNNING = True
afficher = ecran_titre

while RUNNING:
    afficher()
    events = pygame.event.get()
    for event in events:
        dicKeys = pygame.key.get_pressed()
        if event.type == QUIT or dicKeys[K_TAB]:
            RUNNING = False
            pygame.quit()
            quit()
    pygame_widgets.update(events)
    pygame.display.flip()
