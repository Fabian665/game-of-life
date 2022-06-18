import pygame as pg


pg.init()

try:
    buttons_font = pg.font.SysFont("calibri", 16)
except pg.error:
    buttons_font = pg.font.Font(None, 16)

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

    def draw(self, background):
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


class PlayButton(TextButton):
    pass
