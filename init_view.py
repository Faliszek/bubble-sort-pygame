import pygame
import config


from button import Button
from image import Image


class InitView:

    def __init__(self,  screen):
        screen.fill(config.colors["white"])

        bg = Image(screen, name="bubbles-bg.png", y=-100)
        bg.render()

    def render(self, gameChanger, screen, events):

        startButton = Button(
            screen,  onClick=lambda: gameChanger.startGame(), text="Start", y=300)
        startButton.render(events)

        exitButton = Button(screen,  onClick=lambda: pygame.quit(),
                            text="Zakoncz", y=400)
        exitButton.render(events)
