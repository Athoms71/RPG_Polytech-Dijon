import pygame
from random import randint


class playlist():
    def __init__(self, liste_bruits: list):
        self.bruits = liste_bruits  # Spécifier le chemin des bruits dans listes_bruits

    def play_sound(self):
        '''Joue un bruit aléatoire d'une playlist donnée'''
        index_bruit = randint(0, len(self.bruits)-1)
        bruit = pygame.mixer.Sound(self.bruits[index_bruit])
        len_bruit = int(bruit.get_length())
        bruit.play()
        pygame.time.delay(len_bruit)

    def play_sounds(self, loopback: int = 0):
        '''Joue tous les bruits aléatoirement d'une playlist donnée'''
        while loopback >= 0:
            index_bruit = 0
            index_bruit_precedent = -1
            for i in range(len(self.bruits)):
                index_bruit = randint(0, len(self.bruits)-1)
                if index_bruit == index_bruit_precedent:
                    index_bruit = (index_bruit+1) % len(self.bruits)
                index_bruit_precedent = index_bruit
                bruit = pygame.mixer.Sound(self.bruits[index_bruit])
                bruit.play()
                duree_bruit = bruit.get_length()
                pygame.time.delay(int(duree_bruit+0.2)*1000)
            loopback -= 1


# Création des différentes playlists en fonction des bruits
sons_epee = playlist([
    "./sounds/bruit_epee_1.mp3",
    "./sounds/bruit_epee_2.mp3",
    "./sounds/bruit_epee_3.mp3",
    "./sounds/bruit_epee_4.mp3",
    "./sounds/bruit_epee_5.mp3",
    "./sounds/bruit_epee_6.mp3",
    "./sounds/bruit_epee_7.mp3",
    "./sounds/bruit_epee_8.mp3",
    "./sounds/bruit_epee_9.mp3",
    "./sounds/bruit_epee_10.mp3",
    "./sounds/bruit_combat_epee.mp3"
])
sons_arc_fleche = playlist(["./sounds/bruit_fleche_plante.mp3"])
sons_cri = playlist([
    "./sounds/bruit_cri_1.mp3",
    "./sounds/bruit_cri_2.mp3",
    "./sounds/bruit_cri_3.mp3",
    "./sounds/bruit_cri_4.mp3",
    "./sounds/bruit_cri_5.mp3",
    "./sounds/bruit_cri_6.mp3",
    "./sounds/bruit_cri_7.mp3",
    "./sounds/bruit_cri_8.mp3",
    "./sounds/bruit_cri_9.mp3",
])
sons_chute = playlist([
    "./sounds/bruit_defenestration_01.mp3",
    "./sounds/bruit_defenestration_02.mp3"
])
sons_monstre = playlist([
    "./sounds/cri_monstre_1.mp3",
    "./sounds/cri_monstre_2.mp3",
    "./sounds/cri_monstre_3.mp3",
    "./sounds/cri_monstre_4.mp3",
    "./sounds/cri_monstre_5.mp3"
])
sons_coups = playlist(["./sounds/bruit_coup_ventre.mp3"])
sons_chaine = playlist(["./sounds/bruit_chaine.mp3"])
sons_clairon = playlist(["./sounds/bruit_clairon.mp3"])
sons_marche = playlist(["./sounds/bruit_marche_militaire.mp3"])
