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


print(textbox_input())
