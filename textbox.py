import pygame


def modifStr(text: str, X: int,):
    return (text[:X] + text[X+1:])


def sepLignes(text: str):
    l1 = ''
    l2 = ''
    l3 = ''
    l4 = ''
    l5 = ''
    l6 = ''
    l7 = ''
    l8 = ''
    l9 = ''
    l10 = ''
    reste = ''
    ligne_en_cours = 1
    count_lettre_ligne = 0
    count_lettre = 0
    done = False
    if len(text) == 0:
        done = True
    while not done:

        if text[count_lettre] == "@":
            text = modifStr(text, count_lettre)  # on retire le @
            count_lettre_ligne = 0
            ligne_en_cours += 1

       # cas de base (<100 caractere par ligne ou on est au millieu d un mot)
        elif (count_lettre_ligne < 100) or text[count_lettre] != " ":

            if ligne_en_cours == 1:
                l1 += text[count_lettre]
                count_lettre_ligne += 1
                count_lettre += 1

            elif ligne_en_cours == 2:
                l2 += text[count_lettre]
                count_lettre += 1
                count_lettre_ligne += 1

            elif ligne_en_cours == 3:
                l3 += text[count_lettre]
                count_lettre += 1
                count_lettre_ligne += 1

            elif ligne_en_cours == 4:
                l4 += text[count_lettre]
                count_lettre += 1
                count_lettre_ligne += 1

            elif ligne_en_cours == 5:
                l5 += text[count_lettre]
                count_lettre += 1
                count_lettre_ligne += 1

            elif ligne_en_cours == 6:
                l6 += text[count_lettre]
                count_lettre += 1
                count_lettre_ligne += 1

            elif ligne_en_cours == 7:
                l7 += text[count_lettre]
                count_lettre += 1
                count_lettre_ligne += 1

            elif ligne_en_cours == 8:
                l8 += text[count_lettre]
                count_lettre += 1
                count_lettre_ligne += 1

            elif ligne_en_cours == 9:
                l9 += text[count_lettre]
                count_lettre += 1
                count_lettre_ligne += 1
            else:
                l9 += text[count_lettre]
                count_lettre += 1
                count_lettre_ligne += 1
        else:
            # alerte, on a plus de 100 caractere et on est a la fin d un mot !
            if text[count_lettre] == " ":
                count_lettre_ligne = 0
                ligne_en_cours += 1
                text = modifStr(text, count_lettre)  # on retire le " "

        if len(reste)+len(l1)+len(l2)+len(l3)+len(l4)+len(l5)+len(l6)+len(l7)+len(l8)+len(l9)+len(l10) == len(text):
            # as t on fini de trier ? -> travail fini
            done = True
    return (l1, l2, l3, l4, l5, l6, l7, l8, l9, l10)


def dimensions_ecran():
    pygame.init()
    screen_info = pygame.display.Info()
    screen_width = screen_info.current_w
    screen_height = screen_info.current_h
    return (screen_width, screen_height)
    pygame.quit()


window_width, window_height = dimensions_ecran()
screen = pygame.display.set_mode((window_width, window_height))


def textbox_input(texte: str):
    textbox_output(texte)
    "renvoie le text fournis dans la textbox en ayant au prealable affiché le texte mis en parametre"
    pygame.init()
    # pygame.font.Font("font/TheWildBreathOfZelda-15Lv.ttf", 32)
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(0, (dimensions_ecran(
    )[1]*2/3), (dimensions_ecran()[0]), (dimensions_ecran()[1]*1/3))
    color = pygame.Color('lightskyblue3')
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    done = True
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    if len(text) < 100:
                        # verification que le texte est pas trop long
                        text += event.unicode

        screen.fill((30, 30, 30))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
        clock.tick(30)

    return (text)
    pygame.quit()


def textbox_output(text):
    "écrit dans la textbox le text fournis en entree."
    pygame.init()
    # pygame.font.Font("font/TheWildBreathOfZelda-15Lv.ttf", 32)
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(0, (dimensions_ecran(
    )[1]*2/3), (dimensions_ecran()[0]), (dimensions_ecran()[1]*1/3))
    # color_inactive = pygame.Color('lightskyblue3')
    # color_active = pygame.Color('dodgerblue2')
    color = pygame.Color('lightskyblue3')
    text_en_cours = ''
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:  # pygame.KEYDOWN si on veut n importe quelle touche
                done = True

        if len(text_en_cours) < len(text):
            text_en_cours += text[len(text_en_cours)]
            # a chaque iteration, on ajoute un caractere a la liste a afficher jusqu'a que le texte soit complet'"
        screen.fill((30, 30, 30))

        for i in range(8):

            if i == 0:
                # Render the current text.
                txt_surface_l0 = font.render(
                    sepLignes(text_en_cours)[i], True, color)
                # Blit the text.
                screen.blit(txt_surface_l0,
                            (input_box.x+5, input_box.y+(5+(i*30))))

            if i == 1:
                # Render the current text.
                txt_surface_l1 = font.render(
                    sepLignes(text_en_cours)[i], True, color)
                # Blit the text.
                screen.blit(txt_surface_l1,
                            (input_box.x+5, input_box.y+(5+(i*30))))

            if i == 2:
                # Render the current text.
                txt_surface_l2 = font.render(
                    sepLignes(text_en_cours)[i], True, color)
                # Blit the text.
                screen.blit(txt_surface_l2,
                            (input_box.x+5, input_box.y+(5+(i*30))))

            if i == 3:
                # Render the current text.
                txt_surface_l3 = font.render(
                    sepLignes(text_en_cours)[i], True, color)
                # Blit the text.
                screen.blit(txt_surface_l3,
                            (input_box.x+5, input_box.y+(5+(i*30))))

            if i == 4:
                # Render the current text.
                txt_surface_l4 = font.render(
                    sepLignes(text_en_cours)[i], True, color)
                # Blit the text.
                screen.blit(txt_surface_l4,
                            (input_box.x+5, input_box.y+(5+(i*30))))

            if i == 5:
                # Render the current text.
                txt_surface_l5 = font.render(
                    sepLignes(text_en_cours)[i], True, color)
                # Blit the text.
                screen.blit(txt_surface_l5,
                            (input_box.x+5, input_box.y+(5+(i*30))))

            if i == 6:
                # Render the current text.
                txt_surface_l6 = font.render(
                    sepLignes(text_en_cours)[i], True, color)
                # Blit the text.
                screen.blit(txt_surface_l6,
                            (input_box.x+5, input_box.y+(5+(i*30))))

            if i == 7:
                # Render the current text.
                txt_surface_l7 = font.render(
                    sepLignes(text_en_cours)[i], True, color)
                # Blit the text.
                screen.blit(txt_surface_l7,
                            (input_box.x+5, input_box.y+(5+(i*30))))

            if i == 8:
                # Render the current text.
                txt_surface_l8 = font.render(
                    sepLignes(text_en_cours)[i], True, color)
                # Blit the text.
                screen.blit(txt_surface_l8,
                            (input_box.x+5, input_box.y+(5+(i*30))))

        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
        clock.tick(100)

    # pygame.quit()


'''
texte1 = "Bienvenue aventurier, dans les Royaumes de l'Éclipse !@Au seuil de cette aventure épique, vous êtes sur le point d'embarquer pour des terres inconnues, où le destin se tisse entre les ombres et la lumière.@@Préparez-vous à plonger dans un monde de mystère et de magie, où chaque choix que vous ferez influencera le cours de l'histoire. Des terres sauvages aux cités florissantes, des donjons oubliés aux montagnes glacées, l'aventure vous attend à chaque tournant."

texte4 = "Avant de commencer votre voyage, il est temps de forger votre propre destin. Créez votre personnage, choisissez votre race, votre classe et vos compétences, et préparez-vous à affronter les défis qui vous attendent. Votre courage, votre astuce et votre détermination seront vos meilleurs alliés dans cette quête pour la gloire et la fortune.@@L'aventure vous appelle, cher héros. Êtes-vous prêt à répondre à son appel et à laisser votre marque sur les Royaumes de l'Éclipse ?  "  # texte1 = "test1"
texte2 = "Veuillez entrer le nom de votre personnage : "
# texte2 = "test 2"
textbox_output(texte1)
textbox_output(texte4)
textbox_output(texte2)
texte3 = textbox_input()
textbox_output("Votre nom est ''"+texte3+"'' c est bien ca ?")
'''
# textbox_output("@@@@@@@Ceci est un exemple de texte qui est beaucoup plus long que cent caractères et qui sera tronqué pour ne pas dépasser la limite spécifiée.")
