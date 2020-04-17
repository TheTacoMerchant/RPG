import pygame

class Button:

    def __init__(self, caption, link, rect, position):
        super().__init__()
        self.caption = caption
        self.link = link
        self.position = position
        self.rect = rect

    def render(self, screen, font):
        pygame.draw.rect(screen, (0,0,0), self.rect)
        caption = font.render(self.caption, True, (0, 128, 0))
        screen.blit(caption, self.position)


