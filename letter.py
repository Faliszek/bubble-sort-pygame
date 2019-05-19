import random
import pygame
import config
# import scipy.interpolate


class Letter:
    index = 1
    value = 0
    text = ""
    x = 0
    y = 0
    h = 80
    w = 40
    bg = config.colors["blue"]
    screen = None

    def __init__(self, screen, index, value, text, x, y, w, h):
        self.index = index
        self.value = value
        self.text = text
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.screen = screen

    def calcTextPosition(self, x, y, w, h, textWidth, textHeight):
        x = x + (w / 2) - (textWidth / 2)
        y = y + (h / 2) - (textHeight / 2)
        return (x, y)

    def render(self, screen, index, value, text, x, y, w, h):
        x = (index * w) + x

        font = pygame.font.SysFont("lato", 48)

        textRenderer = font.render(text, True, config.colors["white"])

        (textX, textY) = self.calcTextPosition(x, y, w, h,
                                               textRenderer.get_width(), textRenderer.get_height())

        pygame.draw.rect(screen, config.colors["darkBlue"],
                         (x, y, w, h))
        screen.blit(textRenderer, (textX,
                                   textY))
        pygame.draw.rect(screen,  config.colors["white"], [
                         x, y, w, h], 10)
