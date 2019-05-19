import pygame

from button import Button
from image import Image
from screen import Screen


class InitView(Screen):

    def __init__(self, screen):
        super().__init__(screen)

    def render(self, gameChanger, screen, events):

        logo = Image(screen, name="logo.bmp", y=50)
        logo.render()

        startButton = Button(
            screen,  onClick=lambda: gameChanger.startGame(), text="Start", y=518)
        startButton.render(events)

        exitButton = Button(screen,  onClick=lambda: pygame.quit(),
                            text="Zakoncz", y=618)
        exitButton.render(events)
