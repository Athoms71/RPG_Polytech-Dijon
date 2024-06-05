import os
import entite as Ett


def save(dict_var: dict):
    '''
    Sauvegarde des données de dict_var à la fin de chaque chapitre, écriture dans le fichier save.txt
    Format du fichier save.txt :
        nom_variable1
        val1,val2,val3,...,valN
        nom_variable2
        ...
    '''
    file = open("save.txt", "w")
    for key in dict_var:
        file.write(key+"\n")
        type_dict_var = type(dict_var[key])
        if type_dict_var == str:
            file.write(dict_var[key])
        elif type_dict_var == int:
            file.write(int(dict_var[key]))
        elif type_dict_var == list or type_dict_var == tuple:
            for elt in dict_var[key]:
                file.write(str(elt)+",")
        else:
            print("Erreur")
        file.write("\n")
    file.close()


def load(save_file="save.txt"):
    '''Chargement du fichier save_file et attribution des valeurs du fichier dans les différentes variables du jeu'''
    if os.path.exists(save_file):
        dict_var = {}
        file = open(save_file, "r")
        f = file.readlines()
        for i in range(1, len(f), 2):
            key = f[i-1][:-1]
            values = f[i][:-1].split(',')
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
    - inventaire_joueur : str
    - avancement : int
    - 
'''
