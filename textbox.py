import sys
import pygame as pg


def main():
    screen = pg.display.set_mode((1020, 800))
    font = pg.font.Font(None, 32)
    clock = pg.time.Clock()
    input_box = pg.Rect(100, 100, 140, 32)
    # color_inactive = pg.Color('lightskyblue3')
    # color_active = pg.Color('dodgerblue2')
    color = pg.Color('lightskyblue3')
    text = ''
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    print(text)
                    text = ''
                elif event.key == pg.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

        screen.fill((30, 30, 30))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pg.draw.rect(screen, color, input_box, 2)

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()


'''
class Text_box :
    def __init__ (self,x=10,y=870,h=200,l=1900,text=''):
        "par défaut, la textbox est espacé de 10 px de chaque bord et a une taille de 1900 par 200."
        self.x = x
        self.y = y
        self.h = h
        self.l = l
        self.text = text
    
    def affichage (self):
        pygame.draw.rect(screen, (200,200,200), [self.x, self.y, self.h, self.l], 0)

'''
