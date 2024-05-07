import sys
import pygame


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
            l1 = text_en_cours[:100]
            l2 = text_en_cours[100:200]
            # a chaque iteration, on ajoute un caractere a la liste a afficher jusqu'a que le texte soit complet'"

        screen.fill((30, 30, 30))
        for i in range((int(len(text_en_cours)/100))+1):
            if i == 0:
                # Render the current text.
                txt_surface_l1 = font.render(l1, True, color)
                # Blit the text.
                screen.blit(txt_surface_l1, (input_box.x+5, input_box.y+5))
            if i == 1:
                # Render the current text.
                txt_surface_l2 = font.render(l2, True, color)
                # Blit the text.
                screen.blit(txt_surface_l2, (input_box.x+5, input_box.y+30))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
        clock.tick(100)

    return (text)
    pygame.quit()


textbox_output("le CACABOUDIN c trop bienle CACABOUDIN c trop bienle CACABOUDIN c trop bienle CACABOUDIN c trop bienle CACABOUDIN c trop bienle CACABOUDIN c trop bienle CACABOUDIN c trop bienle CACABOUDIN c trop bienle CACABOUDIN c trop bienle CACABOUDIN c trop bienle CACABOUDIN c trop bienle CACABOUDIN c trop bienle CACABOUDIN c trop bienle CACABOUDIN c trop bienle CACABOUDIN c trop bien")
