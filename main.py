import entite as Ett
import chapitre_0 as C0
import chapitre_1 as C1
import pygame
from pygame.locals import *

pygame.init()
pygame.key.set_repeat(400, 30)

screen = pygame.display.set_mode((640, 480))
bg = pygame.image.load("img/chemin_fond.jpg").convert()
bg = pygame.transform.scale(bg, (640, 480))

keep_screen = True

while keep_screen:
    for event in pygame.event.get():
        if event.type == QUIT:
            keep_screen = False
    screen.blit(bg, (0, 0))
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
