import os


def save(list_var: list):
    file = open("save.txt", "w")
    for var in list_var:
        file.write(var+"\n")
    file.close()


def load(list_var: list, save_file="save.txt"):
    if exists(save_file):
        file = open(save_file, "r")
        for line in file.readlines():
            list_var.append(line[:-1])


def exists(file):
    if os.path.exists(file):
        return True
    return False


'''
list_var = ["Toto", "guerrier", "humain"]
print(list_var)
save(list_var)
list_var = []
print(list_var)
load(list_var)
print(list_var)
'''
