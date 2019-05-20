import pygame
import config

width = config.size["width"]
height = config.size["height"]


class Message:
    text = ""
    x = 0
    y = 0
    w = 0
    h = 0

    def __init__(self, w=0.6, h=100,  text=""):
        self.text = text
        self.x = 0
        self.y = 400
        self.w = width * w
        self.h = h

    def calcTextPosition(self, textWidth, textHeight):

        x = (width / 2) - (textWidth / 2)
        y = self.y
        return (x, y)

    def render(self, screen, w, h, text):
        font = pygame.font.SysFont("lato", 28)
        text = font.render(self.text, True, config.colors["black"])

        (textX, textY) = self.calcTextPosition(
            text.get_width(), text.get_height())

        screen.blit(text, (textX,
                           textY))
