import pygame as pg
from buttons import PlayButton, StepButton, WrapButton, ResetButton, GameCell
from board import Board


# initialize pygame and screen
pg.init()
screen_size = (width, height) = (640, 665)
screen = pg.display.set_mode(screen_size)

# initialize background object
background = pg.Surface(screen.get_size())
background = background.convert()
background.fill((255, 255, 255))

font_title = pg.font.Font(None, 36)


def main():
    pg.display.set_caption("Conway's Game of Life")

    # make text object and blit it
    text = font_title.render("Conway's Game of Life - by Fabian", True, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery += 5
    background.blit(text, textpos)

    board = Board()  # initialize a Game of Life board

    # initialize buttons from buttons.py
    play_button = PlayButton(40, 35)
    step_button = StepButton(105, 35)
    wrap_button = WrapButton(170, 35)
    reset_button = ResetButton(235, 35)

    # create game cells array
    cells = []

    pos_y = 54
    pos_x = 40
    for (y, x), _ in board.cells_generator():
        if x == 0:
            pos_x = 40
            pos_y += 16
        cells.append(GameCell(pos_x, pos_y, row=y, column=x))
        pos_x += 16

    # start game loop
    run = True
    while run:

        # blit and draw all the objects
        screen.blit(background, (0, 0))
        play_button.draw(background)
        step_button.draw(background)
        wrap_button.draw(background)
        reset_button.draw(background)

        # update the game board if the play button is toggled
        if play_button.toggled:
            board.update()
            pg.time.delay(30)
            for i, (_, cell) in enumerate(board.cells_generator()):
                cells[i].set_state(cell.is_alive())

        # reset the board if the reset button is clicked
        if reset_button.was_clicked:
            if play_button.toggled:
                play_button.action()
            board.reload()
            reset_button.was_clicked = False
            for i, (_, cell) in enumerate(board.cells_generator()):
                cells[i].set_state(cell.is_alive())

        # change the wrap setting
        if wrap_button.was_clicked:
            board.change_wrap_setting()
            wrap_button.was_clicked = False

        # do one update of the board
        if step_button.was_clicked and not play_button.toggled:
            board.update()
            for i, (_, cell) in enumerate(board.cells_generator()):
                cells[i].set_state(cell.is_alive())
            step_button.was_clicked = False

        # draw all cells
        [cell.draw(background, board=board) for cell in cells]

        pg.display.flip()

        # quit the game
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()
                break


if __name__ == '__main__':
    main()
