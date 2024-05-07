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


window_width, window_height = dimensions_ecran()
screen = pygame.display.set_mode((window_width, window_height))
bg_titre = pygame.image.load("img/chemin_fond_flou.png").convert()
bg_titre = pygame.transform.scale(bg_titre, (window_width, window_height))

title_font = pygame.font.Font("font/TheWildBreathOfZelda-15Lv.ttf", 90)
title_text = title_font.render("Les Royaumes de l'Eclipse", True, WHITE)
title_rect = title_text.get_rect(center=(window_width//2, window_height//4))

button_w, button_h = window_width//5, 100
button_font = pygame.font.Font("font/TheWildBreathOfZelda-15Lv.ttf", 60)
button_color = pygame.Color(255, 255, 255, 128)

# button_play_text = button_font.render("Jouer", True, BLACK, button_color)
# button_play_rect = button_play_text.get_rect(
#    center=(window_width//2, window_height//2))

# button_settings_text = button_font.render(
#    "Parametres", True, BLACK, button_color)
# button_settings_rect = button_settings_text.get_rect(
#   center=(window_width//2, (window_height//2)+button_h))

# button_quit_text = button_font.render("Quitter", True, BLACK, button_color)
# button_quit_rect = button_quit_text.get_rect(
#    center=(window_width//2, (window_height//2)+2*button_h))

button_play = Button(
    screen,
    window_width//2-button_w//2,
    window_height//2,
    button_w,
    button_h,

    text='Jouer',
    font=button_font,
    textColour=(0, 0, 0),
    fontSize=60,
    margin=5,
    inactiveColour=(255, 255, 255, 128),
    hoverColour=(255, 255, 255),
    pressedColour=(192, 192, 192),
    radius=10)

keep_screen = True

while keep_screen:
    events = pygame.event.get()
    for event in events:
        dicKeys = pygame.key.get_pressed()
        if event.type == QUIT or dicKeys[K_ESCAPE]:
            pygame.quit()
            keep_screen = False
            quit()
    screen.blit(bg_titre, (0, 0))
    screen.blit(title_text, title_rect)
    pygame_widgets.update(events)
    pygame.display.flip()


'''def scenario(chapitre: int, karma: int):
    """lance la partie du scenario correspondant au chapitre en cours, et la voie empruniée jusqu'a présent"""
    if chapitre == 0:
        C0.intro()
        chapitre += 1
    if chapitre == 1:
        C1.ch1()'''
