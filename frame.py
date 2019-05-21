import pygame
import config


class Frame:
    x = 0
    y = 0
    h = 0
    w = 0

    def __init__(self, x, y, h, w):
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.position = 1

    def render(self, screen, events):
        pygame.draw.rect(screen, config.colors["darkBlue"], [
                         self.x, self.y, self.w, self.h], 2)
