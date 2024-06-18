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
            for obj in dict_var[key]:
                for elt in obj:
                    file.write(str(elt)+"/")
                if dict_var[key] != []:
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
            if key == "inventaire_joueur":
                dict_var[key] = []
                for conso in values[:-1]:
                    conso_attrs = conso.split('/')
                    conso_avec_attr = []
                    for attr in conso_attrs[:-1]:
                        conso_avec_attr.append(attr)
                    dict_var[key].append(conso_avec_attr)
            else:
                dict_var[key] = values[0]
        file.close()
    return dict_var


'''dict_var = {
    "nom_joueur": "toto",
    "classe_joueur": "guerrier",
    "race_joueur": "humain",
    "pv_joueur": 0,
    "argent_joueur": 0,
    "avancement": 0,
    "inventaire_joueur": [['Petite potion de soin', 0, 0, 30, 10, 'soin'], ['Arc', 30, 0, 15, 'main_droite'], ['Petite potion de force', 5, 5, 0, 10, 'attaque'], ['Petite potion de soin', 0, 0, 30, 10, 'soin'], ['Petite potion de force', 5, 5, 0, 10, 'attaque'], ['Heaume Basique', 0, 5, 10, 'tete'], ['Plastron Basique', 0, 7, 10, 'torse'], ['Jambières Basique', 0, 5, 10, 'jambes'], ['Bottes Basique', 0, 3, 10, 'pieds'], ['épé de cristal', 40, 0, 15, 'main_droite']]
}

save(dict_var)
dict_var = load()
print(dict_var)
'''
