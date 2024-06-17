import os


def save(dict_var: dict):
    '''
    Sauvegarde des données de dict_var à la fin de chaque chapitre, écriture dans le fichier save.txt\n
    Format du fichier save.txt :\n
        nom_variable1\n
        val1_1/val1_2/.../val1_n,val2,val3,...,valN\n
        nom_variable2\n
        ...\n
        Toujours terminer par une ligne vide
    '''
    file = open("save.txt", "w", encoding="utf-8")
    for key in dict_var:
        file.write(key+"\n")
        type_dict_var = type(dict_var[key])
        if type_dict_var == str:
            file.write(dict_var[key])
        elif type_dict_var == int:
            file.write(str(dict_var[key]))
        elif type_dict_var == list:
            for elt in dict_var[key]:
                file.write(str(elt)+"/")
            if key == "inventaire_joueur" and dict_var[key] != []:
                file.write(',')
        file.write("\n")
    file.close()


def load():
    '''Chargement du fichier save.txt et attribution des valeurs du fichier dans les différentes variables du jeu'''
    if os.path.exists("save.txt"):
        file = open("save.txt", "r", encoding="utf-8")
        dict_var = {}
        f = file.readlines()
        for i in range(0, len(f), 2):
            key = f[i][:-1]
            values = f[i+1][:-1].split(',')
            print(key, ':', values)
            if key == "inventaire_joueur":
                dict_var[key] = []
                for conso in values[:-1]:
                    conso_attrs = conso.split('/')
                    conso_avec_attr = []
                    for attr in conso_attrs[:-1]:
                        conso_avec_attr.append(attr)
                    dict_var[key].append(conso_avec_attr)
            elif key in ["main_gauche_joueur", "main_droite_joueur", "tete_joueur", "torse_joueur", "gants_joueur", "jambes_joueur", "pieds_joueur"]:
                dict_var[key] = []
                equip_attrs = values[0].split('/')
                for attr in equip_attrs[:-1]:
                    dict_var[key].append(attr)
            else:
                dict_var[key] = values[0]
        file.close()
    return dict_var
