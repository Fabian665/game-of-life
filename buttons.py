import pygame as pg


pg.init()

try:
    buttons_font = pg.font.SysFont("calibri", 16)
except pg.error:
    buttons_font = pg.font.Font(None, 16)


class Clickable:
    reg_color = (230, 230, 230)
    click_color = (240, 240, 240)
    hover_color = None
    width = None
    height = None
    radius = None

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pg.Rect(x, y, self.width, self.height)
        self.pressed = False
        self.button_color = None

    def draw(self, background, additional=None):
        self.click_logic(additional)
        pg.draw.rect(background, self.button_color, self.rect, border_radius=self.radius)

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
    hover_color = (210, 210, 210)
    text_color = (0, 0, 0)
    width = 60
    height = 25
    radius = 7

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


class WrapButton(TextButton):
    toggled = False
    toggled_color = (37, 44, 174)
    untoggled_color = (250, 190, 21)
    toggled_hover = (102, 107, 200)
    untoggled_hover = (255, 217, 110)

    def __init__(self, x, y):
        super().__init__(x, y, "closed")
        self.hover_color = self.untoggled_hover
        self.reg_color = self.untoggled_color
        self.was_clicked = False

    def action(self, additional):
        if self.toggled:
            self.set_text("closed")
            self.toggled = False
            self.reg_color = self.untoggled_color
            self.hover_color = self.untoggled_hover
        else:
            self.text_color = (255, 255, 255)
            self.set_text("wrapped")
            self.toggled = True
            self.reg_color = self.toggled_color
            self.hover_color = self.toggled_hover
        self.was_clicked = True



class ResetButton(TextButton):
    def __init__(self, x, y):
        super().__init__(x, y, "reset")
        self.was_clicked = False

    def action(self, additional):
        self.was_clicked = True


class StepButton(TextButton):
    def __init__(self, x, y):
        super().__init__(x, y, "step")
        self.was_clicked = False

    def action(self, additional):
        self.was_clicked = True


class GameCell(Clickable):
    toggled = False
    alive_color = (0, 0, 0)
    dead_color = (220, 220, 220)
    alive_hover = (100, 100, 100)
    dead_hover = (170, 170, 170)
    width = 15
    height = 15
    radius = 0

    def __init__(self, pos_x, pos_y, row, column):
        super().__init__(pos_x, pos_y)
        self.hover_color = self.dead_hover
        self.row = row
        self.column = column

    def action(self, board):
        if self.toggled:
            self.toggled = False
            self.reg_color = self.dead_color
            self.hover_color = self.dead_hover
        else:
            self.toggled = True
            self.reg_color = self.alive_color
            self.hover_color = self.alive_hover
        board.flip_cell(row=self.row, column=self.column)

    def set_state(self, alive):
        if alive:
            self.toggled = True
            self.reg_color = self.alive_color
            self.hover_color = self.alive_hover
        else:
            self.toggled = False
            self.reg_color = self.dead_color
            self.hover_color = self.dead_hover
