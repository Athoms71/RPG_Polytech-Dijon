import entite as Ett
import chapitre_0 as C0
import chapitre_1 as C1
import pygame
from pygame.locals import *

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

keep_screen = True

while keep_screen:
    for event in pygame.event.get():
        dicKeys = pygame.key.get_pressed()
        if event.type == QUIT or dicKeys[K_ESCAPE]:
            keep_screen = False
    screen.blit(bg_titre, (0, 0))
    screen.blit(title_text, title_rect)
    pygame.display.update()
    pygame.time.wait(10)
pygame.quit()


'''def scenario(chapitre: int, karma: int):
    """lance la partie du scenario correspondant au chapitre en cours, et la voie empruniée jusqu'a présent"""
    if chapitre == 0:
        C0.intro()
        chapitre += 1
    if chapitre == 1:
        C1.ch1()'''
