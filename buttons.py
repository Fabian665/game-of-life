import pygame as pg


pg.init()

try:
    buttons_font = pg.font.SysFont("calibri", 16)
except pg.error:
    buttons_font = pg.font.Font(None, 16)


class Clickable:
    reg_color = None
    hover_color = None
    click_color = None
    width = None
    height = None

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pg.Rect(x, y, self.width, self.height)
        self.pressed = False
        self.button_color = None

    def draw(self, background, additional=None):
        self.click_logic(additional)
        pg.draw.rect(background, self.button_color, self.rect, border_radius=7)

    def click_logic(self, additional):
        mouse_pos = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.button_color = self.hover_color
            if pg.mouse.get_pressed()[0]:
                self.pressed = True
                self.button_color = self.click_color
            elif self.pressed:
                self.action(additional)
                self.pressed = False
                self.button_color = self.hover_color
        else:
            self.button_color = self.reg_color

    def action(self, additional):
        pass


class TextButton(Clickable):
    reg_color = (230, 230, 230)
    hover_color = (220, 220, 220)
    click_color = (240, 240, 240)
    text_color = (0, 0, 0)
    width = 55
    height = 25

    def __init__(self, x, y, text):
        super().__init__(x, y)
        self.text_surf = None
        self.text_rect = None
        self.set_text(text)

    def draw(self, background, additional=None):
        super().draw(background, additional)
        background.blit(self.text_surf, self.text_rect)

    def set_text(self, text):
        self.text_surf = buttons_font.render(text, True, self.text_color)
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)


class PlayButton(TextButton):
    toggled = False
    toggled_color = (100, 221, 23)
    untoggled_color = (230, 230, 230)
    toggled_hover = (245, 66, 66)
    untoggled_hover = (128, 227, 64)

    def __init__(self, x, y):
        super().__init__(x, y, "play")
        self.hover_color = self.untoggled_hover

    def draw(self, background, additional=None):
        super().draw(background, additional)

    def action(self, additional):
        if self.toggled:
            self.set_text("play")
            self.toggled = False
            self.reg_color = self.untoggled_color
            self.hover_color = self.untoggled_hover
        else:
            self.set_text("pause")
            self.toggled = True
            self.reg_color = self.toggled_color
            self.hover_color = self.toggled_hover


class ResetButton(TextButton):
    def action(self, additional):
        pass


class GameCell(Clickable):
    reg_color = (240, 240, 240)
    hover_color = (220, 220, 220)
    live_hover_color = (20, 20, 20)
    click_color = (0, 0, 0)
    width = 10
    height = 10