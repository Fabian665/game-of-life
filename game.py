import pygame as pg
from buttons import TextButton


black = (0, 0, 0)
white = (255, 255, 255)

pg.init()
screen_size = (width, height) = (640, 665)
screen = pg.display.set_mode(screen_size)

background = pg.Surface(screen.get_size())
background = background.convert()
background.fill(white)

font_title = pg.font.Font(None, 36)


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
    play_button.draw(background)
    pause_button.draw(background)
    reset_button.draw(background)
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
            play_button.draw(background)
            pause_button.draw(background)
            reset_button.draw(background)
            pg.display.flip()


if __name__ == '__main__':
    main()
