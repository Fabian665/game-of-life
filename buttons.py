import pygame as pg


# Initialize pygame to use it in classes
pg.init()

# Initialize a font object from pygame
try:
    buttons_font = pg.font.SysFont("calibri", 16)
except pg.error:
    buttons_font = pg.font.Font(None, 16)


class Clickable:
    """
    An abstract class for clickable buttons
    """
    reg_color = (230, 230, 230)
    click_color = (240, 240, 240)
    hover_color = None
    width = None
    height = None
    radius = None

    def __init__(self, x, y):
        """
        Initialize a Clickable.

        Parameters
        ----------
        x : int
            The x_pos value of the Clickable in relation to the screen.
        y : int
            The y_pos value of the Clickable in relation to the screen

        """
        self.x = x
        self.y = y
        self.rect = pg.Rect(x, y, self.width, self.height)
        self.pressed = False
        self.button_color = None

    def draw(self, background, **kwargs):
        """
        Draw a the pygame object on screen and.

        Parameters
        ----------
        background : pygame.Surface
            The surface on which to draw

        Returns
        -------
        None

        """
        self.click_logic(**kwargs)
        pg.draw.rect(background, self.button_color, self.rect, border_radius=self.radius)

    def click_logic(self, **kwargs):
        """
        The click logic for a regular clickable.

        Returns
        -------
        None

        """
        mouse_pos = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.button_color = self.hover_color
            if pg.mouse.get_pressed()[0]:
                self.pressed = True
                self.button_color = self.click_color
            elif self.pressed:
                self.action(**kwargs)
                self.pressed = False
                self.button_color = self.hover_color
        else:
            self.button_color = self.reg_color

    def action(self, **kwargs):
        """
        Perform an action, this is supposed to be an abstract method.

        Returns
        -------
        None

        """
        pass


class TextButton(Clickable):
    """
    An abstract class that inherits from Clickable. A clickable text button.
    """
    hover_color = (210, 210, 210)
    text_color = (0, 0, 0)
    width = 60
    height = 25
    radius = 7

    def __init__(self, x, y, text):
        """
        Initialize Text Button

        Parameters
        ----------
        x : int
            The x_pos value of the Clickable in relation to the screen.
        y : int
            The y_pos value of the Clickable in relation to the screen
        text : str
            The Button's name

        """
        super().__init__(x, y)
        self.text_surf = None
        self.text_rect = None
        self.text = text
        self.set_text()

    def draw(self, background, **kwargs):
        """
        Draw a the pygame object on screen and.

        Parameters
        ----------
        background : pygame.Surface
            The surface on which to draw

        Returns
        -------
        None

        """
        super().draw(background)
        background.blit(self.text_surf, self.text_rect)

    def set_text(self):  # , text):
        """
        Set the text for the button.

        Returns
        -------
        None
        """
        self.text_surf = buttons_font.render(self.text, True, self.text_color)
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)


class PlayButton(TextButton):
    """
    A class that inherits from TextButton and represents a toggleable PlayButton.
    """
    toggled = False
    toggled_hover_text = "pause"
    untoggled_text = "play"
    toggled_text = "playing"
    toggled_color = (100, 221, 23)
    untoggled_color = (230, 230, 230)
    toggled_hover = (245, 66, 66)
    untoggled_hover = (128, 227, 64)

    def __init__(self, x, y):
        """
        Initialize a Play button

        Parameters
        ----------
        x : int
            The x_pos value of the Clickable in relation to the screen.
        y : int
            The y_pos value of the Clickable in relation to the screen

        """
        super().__init__(x, y, self.untoggled_text)
        self.hover_color = self.untoggled_hover

    def click_logic(self):
        """
        The click logic for a regular clickable.

        Returns
        -------
        None

        """
        mouse_pos = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.button_color = self.hover_color
            self.text = self.toggled_hover_text if self.toggled else self.untoggled_text
            if pg.mouse.get_pressed()[0]:
                self.pressed = True
                self.button_color = self.click_color
            elif self.pressed:
                self.action()
                self.pressed = False
                self.button_color = self.hover_color
        else:
            self.text = self.toggled_text if self.toggled else self.untoggled_text
            self.button_color = self.reg_color
        self.set_text()

    def action(self):
        """
        Change the toggled and attribute and set colors and text.

        Returns
        -------
        None
        """
        if self.toggled:
            self.text = self.untoggled_text
            self.toggled = False
            self.reg_color = self.untoggled_color
            self.hover_color = self.untoggled_hover
        else:
            self.text = self.toggled_text
            self.toggled = True
            self.reg_color = self.toggled_color
            self.hover_color = self.toggled_hover


class WrapButton(TextButton):
    """
    A class that inherits from TextButton and represents a toggleable button to control the wrap option.
    """
    toggled = False
    toggled_color = (37, 44, 174)
    untoggled_color = (250, 190, 21)
    toggled_hover = (102, 107, 200)
    untoggled_hover = (255, 217, 110)

    def __init__(self, x, y):
        """
        Initialize the wrap button

        Parameters
        ----------
        x : int
            The x_pos value of the Clickable in relation to the screen.
        y : int
            The y_pos value of the Clickable in relation to the screen
        """
        super().__init__(x, y, "closed")
        self.hover_color = self.untoggled_hover
        self.reg_color = self.untoggled_color
        self.was_clicked = False

    def action(self):
        """
        Change the toggled and attribute and set colors and text.

        Returns
        -------
        None
        """
        if self.toggled:
            self.text_color = (0, 0, 0)
            self.text = "closed"
            self.toggled = False
            self.reg_color = self.untoggled_color
            self.hover_color = self.untoggled_hover
        else:
            self.text_color = (255, 255, 255)
            self.text = "wrapped"
            self.toggled = True
            self.reg_color = self.toggled_color
            self.hover_color = self.toggled_hover
        self.set_text()
        self.was_clicked = True


class ResetButton(TextButton):
    """
    A class that inherits from TextButton and represents a reset button
    """
    def __init__(self, x, y):
        """
        Initialize the reset button

        Parameters
        ----------
        x : int
            The x_pos value of the Clickable in relation to the screen.
        y : int
            The y_pos value of the Clickable in relation to the screen

        """
        super().__init__(x, y, "reset")
        self.was_clicked = False

    def action(self):
        """
        Set the was clicked attribute to True

        Returns
        -------
        None
        """
        self.was_clicked = True


class StepButton(TextButton):
    """
    A class that inherits from TextButton and represents a step button
    """
    def __init__(self, x, y):
        """
        Initialize the reset button

        Parameters
        ----------
        x : int
            The x_pos value of the Clickable in relation to the screen.
        y : int
            The y_pos value of the Clickable in relation to the screen

        """
        super().__init__(x, y, "step")
        self.was_clicked = False

    def action(self):
        """
        Set the was clicked attribute to True

        Returns
        -------
        None
        """
        self.was_clicked = True


class GameCell(Clickable):
    """
    A class that inherits the Clickable class and represents a game cell
    """
    toggled = False
    alive_color = (0, 0, 0)
    dead_color = (220, 220, 220)
    alive_hover = (100, 100, 100)
    dead_hover = (170, 170, 170)
    width = 15
    height = 15
    radius = 0

    def __init__(self, pos_x, pos_y, row, column):
        """
        Initialize a game cell

        Parameters
        ----------
        pos_x : int
            The x_pos value of the Clickable in relation to the screen.
        pos_y : int
            The y_pos value of the Clickable in relation to the screen.
        row : int
            The row of the cell
        column : int
            The column of the cell
        """
        super().__init__(pos_x, pos_y)
        self.reg_color = self.dead_color
        self.hover_color = self.dead_hover
        self.row = row
        self.column = column

    def action(self, board):
        """
        Set the toggled attribute to True and flip cell in the given board.

        Parameters
        ----------
        board : board.Board
            A game of life Board object

        Returns
        -------
        None

        """
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
        """
        Sets the state of the cell to a given bool.

        Parameters
        ----------
        alive : bool
            The desired state

        Returns
        -------
        None

        """
        if alive:
            self.toggled = True
            self.reg_color = self.alive_color
            self.hover_color = self.alive_hover
        else:
            self.toggled = False
            self.reg_color = self.dead_color
            self.hover_color = self.dead_hover
