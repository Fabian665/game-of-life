import pygame

black = (0, 0, 0)
white = (255, 255, 255)


class TextButton:
    button_color = (245, 245, 245)
    hover_color = (230, 230, 230)
    click_color = (200, 200, 200)
    text_color = (0, 0, 0)
    width = 55
    height = 25

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.up_line = ((self.x, self.y), (self.x + self.width, self.y), 1)
        self.right_line = ((self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 1)
        self.down_line = ((self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 1)
        self.left_line = ((self.x, self.y), (self.x, self.y + self.height), 1)

    def draw(self, background):
        global black
        pygame.draw.rect(background, self.button_color, self.rect)
        pygame.draw.line(background, black, *self.up_line)
        pygame.draw.line(background, black, *self.right_line)
        pygame.draw.line(background, black, *self.down_line)
        pygame.draw.line(background, black, *self.left_line)
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(background, self.hover_color, self.rect)


def main():
    global white
    pygame.init()
    screen_size = (width, height) = (640, 665)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Conway's Game of Life")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(white)

    font = pygame.font.Font(None, 36)
    text = font.render("Conway's Game of Life - by Fabian", True, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery += 5
    background.blit(text, textpos)

    button = TextButton(30, 30, "Hello")

    screen.blit(background, (0, 0))
    button.draw(background)
    pygame.display.flip()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        if run:
            screen.blit(background, (0, 0))
            button.draw(background)
            pygame.display.flip()


if __name__ == '__main__':
    main()
