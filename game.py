import pygame as pg
from buttons import TextButton, PlayButton, GameCell


white = (255, 255, 255)

pg.init()
screen_size = (width, height) = (640, 665)
screen = pg.display.set_mode(screen_size)

background = pg.Surface(screen.get_size())
background = background.convert()
background.fill(white)

font_title = pg.font.Font(None, 36)

playing = False


def main():
    pg.display.set_caption("Conway's Game of Life")

    text = font_title.render("Conway's Game of Life - by Fabian", True, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery += 5
    background.blit(text, textpos)

    play_button = PlayButton(30, 30)
    reset_button = TextButton(90, 30, "reset")
    cell = GameCell(30, 65)

    run = True
    while run:

        screen.blit(background, (0, 0))
        pg.display.flip()

        for event in pg.event.get():
            play_button.draw(background, event)
            reset_button.draw(background, event)
            cell.draw(background, event)
            if event.type == pg.QUIT:
                run = False
                pg.quit()
                break


if __name__ == '__main__':
    main()
