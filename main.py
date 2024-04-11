import entite as Ett
import chapitre_0 as C0


def scenario(chapitre: int, karma: int):
    """lance la partie du scenario correspondant au chapitre en cours, et la voie empruniée jusqu'a présent"""
    if chapitre == 0:
        C0.intro()
