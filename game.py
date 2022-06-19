import pygame as pg
from buttons import PlayButton, StepButton, WrapButton, ResetButton, GameCell
from board import Board


white = (255, 255, 255)

pg.init()
screen_size = (width, height) = (640, 665)
screen = pg.display.set_mode(screen_size)

background = pg.Surface(screen.get_size())
background = background.convert()
background.fill(white)

font_title = pg.font.Font(None, 36)


def main():
    pg.display.set_caption("Conway's Game of Life")

    text = font_title.render("Conway's Game of Life - by Fabian", True, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery += 5
    background.blit(text, textpos)

    board = Board()

    play_button = PlayButton(40, 35)
    step_button = StepButton(105, 35)
    wrap_button = WrapButton(170, 35)
    reset_button = ResetButton(235, 35)

    cells = []

    pos_y = 54
    pos_x = 40
    for (y, x), _ in board.cells_generator():
        if x == 0:
            pos_x = 40
            pos_y += 16
        cells.append(GameCell(pos_x, pos_y, row=y, column=x))
        pos_x += 16

    run = True
    while run:

        screen.blit(background, (0, 0))
        play_button.draw(background)
        step_button.draw(background)
        wrap_button.draw(background)
        reset_button.draw(background)

        if play_button.toggled:
            board.update()
            pg.time.delay(30)
            for i, (_, cell) in enumerate(board.cells_generator()):
                cells[i].set_state(cell.is_alive())

        if reset_button.was_clicked:
            if play_button.toggled:
                play_button.action(None)
            board.reload()
            reset_button.was_clicked = False
            for i, (_, cell) in enumerate(board.cells_generator()):
                cells[i].set_state(cell.is_alive())

        if wrap_button.was_clicked:
            board.change_wrap_setting()
            wrap_button.was_clicked = False

        if step_button.was_clicked and not play_button.toggled:
            board.update()
            for i, (_, cell) in enumerate(board.cells_generator()):
                cells[i].set_state(cell.is_alive())
            step_button.was_clicked = False

        [cell.draw(background, board) for cell in cells]

        pg.display.flip()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()
                break


if __name__ == '__main__':
    main()
