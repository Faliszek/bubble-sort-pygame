import random
import pygame
import config


class Letter:
    index = 1
    value = 0
    text = ""
    x = 0
    y = 0
    h = 80
    w = 40
    bg = config.colors["blue"]

    def __init__(self, screen, index, value, text, x, y, w, h):
        self.index = index
        self.value = value
        self.text = text
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.screen = screen

    def calcTextPosition(self, textWidth, textHeight):
        x = self.x + (self.w / 2) - (textWidth / 2)
        y = self.y + (self.h / 2) - (textHeight / 2)
        return (x, y)

    def render(self):

        font = pygame.font.SysFont("lato", 48)
        text = font.render(self.text, True, config.colors["white"])

        (textX, textY) = self.calcTextPosition(
            text.get_width(), text.get_height())

        pygame.draw.rect(self.screen, self.bg,
                         (self.x, self.y, self.w, self.h))
        self.screen.blit(text, (textX,
                                textY))
