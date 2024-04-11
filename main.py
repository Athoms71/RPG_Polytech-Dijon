import entite as Ett
import chapitre_0 as C0
import chapitre_1 as C1


def scenario(chapitre: int, karma: int):
    """lance la partie du scenario correspondant au chapitre en cours, et la voie empruniée jusqu'a présent"""
    if chapitre == 0:
        C0.intro()
        chapitre = + 1
    if chapitre == 1:
        C1.ch1()


scenario(0, 0)

scenario(1, 0)
