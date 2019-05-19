
import pygame
import config
import random

from button import Button
from screen import Screen


class GameView(Screen):
    numbers = []

    def __init__(self,  screen):
        super().__init__(screen)
        self.numbers = self.initNumbers()

    def randomValue(self):
        return random.randint(1, 101)

    def initNumbers(self):
        a = []
        for i in range(10):
            a.append({"index": i, "value": self.randomValue()})
        return a

    def render(self, gameChanger, screen, events):
        events = pygame.event.get()

        startButton = Button(screen, onClick=lambda: print(
            "elo"), text="Zacznij od nowa", y=518)
        startButton.render(events)
        print(self.numbers)
