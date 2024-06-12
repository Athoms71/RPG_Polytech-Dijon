import os


def save(dict_var: dict):
    '''
    Sauvegarde des données de dict_var à la fin de chaque chapitre, écriture dans le fichier save.txt\n
    Format du fichier save.txt :\n
        nom_variable1\n
        val1,val2,val3,...,valN\n
        nom_variable2\n
        ...\n
        Toujours terminer par une ligne vide
    '''
    file = open("save.txt", "w")
    for key in dict_var:
        file.write(key+"\n")
        type_dict_var = type(dict_var[key])
        if type_dict_var == str:
            file.write(dict_var[key])
        elif type_dict_var == int:
            file.write(str(dict_var[key]))
        elif type_dict_var == list:
            for elt in dict_var[key]:
                file.write(str(elt)+",")
        else:
            print("Erreur")
        file.write("\n")
    file.close()


def load():
    '''Chargement du fichier save_file et attribution des valeurs du fichier dans les différentes variables du jeu'''
    if os.path.exists("save.txt"):
        file = open("save.txt", "r")
        dict_var = {}
        f = file.readlines()
        for i in range(0, len(f), 2):
            key = f[i][:-1]
            values = f[i+1][:-1].split(',')
            if len(values) > 1:
                dict_var[key] = []
                for elt in values[:-1]:
                    dict_var[key].append(elt)
            else:
                dict_var[key] = values[0]
        file.close()
    return dict_var


'''
Variables à sauvegarder :
    - nom_joueur : str
    - classe_joueur : str
    - race_joueur : str
    - inventaire_joueur : list
    - pv_joueur : int
    - argent_joueur : int
    - main_gauche_joueur : Equipement
    - main_droite_joueur : Equipement
    - tete_joueur : Equipement
    - torse_joueur : Equipement
    - gants_joueur : Equipement
    - jambes_joueur : Equipement
    - pieds_joueur : Equipement
    - avancement : int
'''
DICT_VAR = {            # Dictionnaire de sauvegarde
    "nom_joueur": "Toto",
    "classe_joueur": "guerrier",
    "race_joueur": "humain",
    "inventaire_joueur": ["Grosse potion", "Petite potion"],
    "pv_joueur": 0,
    "argent_joueur": 0,
    "main_gauche_joueur": None,
    "main_droite_joueur": None,
    "tete_joueur": None,
    "torse_joueur": None,
    "gants_joueur": None,
    "jambes_joueur": None,
    "pieds_joueur": None,
    "avancement": 0
}
print(DICT_VAR)
save(DICT_VAR)
dict_var = load()
print(dict_var)
