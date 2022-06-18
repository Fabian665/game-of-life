import pygame as pg
from buttons import PlayButton, ResetButton, GameCell
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

    play_button = PlayButton(30, 30)
    reset_button = ResetButton(90, 30)

    cells = []

    pos_y = 49
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
        reset_button.draw(background)

        if play_button.toggled:
            board.update()
            pg.time.delay(30)
            for i, (_, cell) in enumerate(board.cells_generator()):
                cells[i].set_state(cell.is_alive())

        if reset_button.was_clicked:
            try:
                board.reload()
            except UnboundLocalError:
                pass
            reset_button.was_clicked = False
            for i, (_, cell) in enumerate(board.cells_generator()):
                cells[i].set_state(cell.is_alive())

        [cell.draw(background, board) for cell in cells]

        pg.display.flip()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()
                break


if __name__ == '__main__':
    main()
