import pygame
import config

width = config.size["width"]
height = config.size["height"]


class Image:
    x = 0
    y = 0
    img = None

    def __init__(self, game, name, x=0, y=0):
        img = pygame.image.load(name)

        self.name = name
        self.x = self.calcX(img)
        self.y = y
        self.game = game
        self.img = img

    def calcX(self, img):
        if img is None:
            return 0
        else:
            return (width / 2) - (img.get_width() / 2)

    def render(self):

        logorect = (self.x, self.y)
        self.game.blit(self.img, logorect)
