import pygame as pg

black = (0, 0, 0)
white = (255, 255, 255)

pg.init()
screen_size = (width, height) = (640, 665)
screen = pg.display.set_mode(screen_size)

background = pg.Surface(screen.get_size())
background = background.convert()
background.fill(white)

try:
    buttons_font = pg.font.SysFont("calibri", 16)
except pg.error:
    buttons_font = pg.font.Font(None, 16)

font_title = pg.font.Font(None, 36)

class TextButton:
    reg_color = (230, 230, 230)
    hover_color = (220, 220, 220)
    click_color = (240, 240, 240)
    text_color = (0, 0, 0)
    width = 55
    height = 25

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.rect = pg.Rect(x, y, self.width, self.height)
        self.text_surf = buttons_font.render(text, True, self.text_color)
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)
        self.pressed = False
        self.button_color = (255, 0, 0)

    def draw(self):
        global black
        self.click_logic()
        pg.draw.rect(background, self.button_color, self.rect, border_radius=7)
        background.blit(self.text_surf, self.text_rect)

    def click_logic(self):
        mouse_pos = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.button_color = self.hover_color
            if pg.mouse.get_pressed()[0]:
                self.pressed = True
                self.button_color = self.click_color
            elif self.pressed:
                self.action()
                self.pressed = False
                self.button_color = self.hover_color
        else:
            self.button_color = self.reg_color

    def action(self):
        pass


def main():
    global white
    pg.display.set_caption("Conway's Game of Life")

    text = font_title.render("Conway's Game of Life - by Fabian", True, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery += 5
    background.blit(text, textpos)

    play_button = TextButton(30, 30, "play")
    pause_button = TextButton(90, 30, "pause")
    reset_button = TextButton(150, 30, "reset")

    screen.blit(background, (0, 0))
    play_button.draw()
    pause_button.draw()
    reset_button.draw()
    pg.display.flip()

    run = True
    while run:
        for event in pg.event.get():
            # button.draw()
            if event.type == pg.QUIT:
                run = False
                pg.quit()
                break
            if event.type == pg.MOUSEBUTTONDOWN:
                pass
        if run:
            screen.blit(background, (0, 0))
            play_button.draw()
            pause_button.draw()
            reset_button.draw()
            pg.display.flip()


if __name__ == '__main__':
    main()
