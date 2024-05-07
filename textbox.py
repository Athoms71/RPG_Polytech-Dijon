import sys
import pygame


def sepLignes(text: str):
    l1 = text[:100]
    l2 = text[100:200]
    l3 = text[200:300]
    l4 = text[300:400]
    l5 = text[400:500]
    l6 = text[500:600]
    l7 = text[600:700]
    l8 = text[700:800]
    l9 = text[800:]
    return (l1, l2, l3, l4, l5, l6, l7, l8, l9)


def dimensions_ecran():
    pygame.init()
    screen_info = pygame.display.Info()
    screen_width = screen_info.current_w
    screen_height = screen_info.current_h
    return (screen_width, screen_height)
    pygame.quit()


window_width, window_height = dimensions_ecran()
screen = pygame.display.set_mode((window_width, window_height))


def textbox_input():
    "renvoie le text fournis dans la textbox"
    pygame.init()
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(0, (dimensions_ecran(
    )[1]*2/3), (dimensions_ecran()[0]), (dimensions_ecran()[1]*1/3))
    # color_inactive = pygame.Color('lightskyblue3')
    # color_active = pygame.Color('dodgerblue2')
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
        # Resize the box if the text is too long.
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
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(0, (dimensions_ecran(
    )[1]*2/3), (dimensions_ecran()[0]), (dimensions_ecran()[1]*1/3))
    # color_inactive = pygame.Color('lightskyblue3')
    # color_active = pygame.Color('dodgerblue2')
    color = pygame.Color('lightskyblue3')

    screen.fill((30, 30, 30))
    text_en_cours = ''

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                done = True

        if len(text_en_cours) < len(text):
            text_en_cours += text[len(text_en_cours)]
            # a chaque iteration, on ajoute un caractere a la liste a afficher jusqu'a que le texte soit complet'"
        screen.fill((30, 30, 30))

        iterations = (int(len(text)/100))+1

        for i in range(8):

            if i == 0:
                # Render the current text.
                txt_surface_l0 = font.render(
                    sepLignes(text_en_cours)[i], True, color)
                # Blit the text.
                screen.blit(txt_surface_l0, (input_box.x+5, input_box.y+5))

            if i == 1:
                # Render the current text.
                txt_surface_l1 = font.render(
                    sepLignes(text_en_cours)[i], True, color)
                # Blit the text.
                screen.blit(txt_surface_l1,
                            (input_box.x+5, input_box.y+(i*30)))

            if i == 2:
                # Render the current text.
                txt_surface_l2 = font.render(
                    sepLignes(text_en_cours)[i], True, color)
                # Blit the text.
                screen.blit(txt_surface_l2,
                            (input_box.x+5, input_box.y+(i*30)))

            if i == 3:
                # Render the current text.
                txt_surface_l3 = font.render(
                    sepLignes(text_en_cours)[i], True, color)
                # Blit the text.
                screen.blit(txt_surface_l3,
                            (input_box.x+5, input_box.y+(i*30)))

            if i == 4:
                # Render the current text.
                txt_surface_l4 = font.render(
                    sepLignes(text_en_cours)[i], True, color)
                # Blit the text.
                screen.blit(txt_surface_l4,
                            (input_box.x+5, input_box.y+(i*30)))

            if i == 5:
                # Render the current text.
                txt_surface_l5 = font.render(
                    sepLignes(text_en_cours)[i], True, color)
                # Blit the text.
                screen.blit(txt_surface_l5,
                            (input_box.x+5, input_box.y+(i*30)))

            if i == 6:
                # Render the current text.
                txt_surface_l6 = font.render(
                    sepLignes(text_en_cours)[i], True, color)
                # Blit the text.
                screen.blit(txt_surface_l6,
                            (input_box.x+5, input_box.y+(i*30)))

            if i == 7:
                # Render the current text.
                txt_surface_l7 = font.render(
                    sepLignes(text_en_cours)[i], True, color)
                # Blit the text.
                screen.blit(txt_surface_l7,
                            (input_box.x+5, input_box.y+(i*30)))

            if i == 8:
                # Render the current text.
                txt_surface_l8 = font.render(
                    sepLignes(text_en_cours)[i], True, color)
                # Blit the text.
                screen.blit(txt_surface_l8,
                            (input_box.x+5, input_box.y+(i*30)))

        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
        clock.tick(100)

    pygame.quit()


texte = "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"


textbox_output(texte)
