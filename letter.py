import random
import pygame
import config


class Number:
    value = 0
    x = 0
    y = 0
    height = 80
    width = 40

    def __init__(self, value):
        self.value = value

    # def render(self):

    #     font = pygame.font.SysFont("lato", 22)
    #     x = self.calcX()
    #     text = font.render(self.text, True, config.colors["white"])

    #     (textX, textY) = self.calcTextPosition(
    #         text.get_width(), text.get_height())
