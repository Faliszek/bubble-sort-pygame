
import pygame
import config


width = config.size["width"]
height = config.size["height"]


class Button:
    text = "Kliknij tutaj"
    clicked = False
    disabled = False
    x = 0
    y = 0
    h = 50
    w = 200
    bg = config.colors["blue"]
    game = None,
    center = True

    def __init__(self, game, onClick, x=0, y=0, w=200, h=50, bg=config.colors["blue"], center=True, text="Kliknij tutaj"):
        self.y = y
        self.x = self.calcX()
        self.w = w
        self.h = h
        self.bg = bg
        self.game = game
        self.center = center
        self.text = text
        self.isClicked = False
        self.handleClick = onClick

    def calcX(self):
        return (width / 2) - (self.w / 2)

    def calcTextPosition(self, textWidth, textHeight):
        x = self.x + (self.w / 2) - (textWidth / 2)
        y = self.y + (self.h / 2) - (textHeight / 2)
        return (x, y)

    def onClick(self, clickX, clickY, eventType):
        print("GITARA")

        if eventType == pygame.MOUSEBUTTONUP:
            if self.x <= clickX <= (self.x + self.w) and self.y <= clickY <= (self.y + self.h):
                self.handleClick()

    def render(self, events):
        print("button", events)

        x = self.calcX()
        font = pygame.font.SysFont("lato", 22)
        text = font.render(self.text, True, config.colors["white"])

        (textX, textY) = self.calcTextPosition(
            text.get_width(), text.get_height())

        bg = self.bg if self.isClicked else config.colors["darkBlue"]

        pygame.draw.rect(self.game, bg, (self.x, self.y, self.w, self.h))
        self.game.blit(text, (textX,
                              textY))
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP or event.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = pygame.mouse.get_pos()
                self.onClick(x, y, event.type)
