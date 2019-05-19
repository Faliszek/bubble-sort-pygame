import pygame
import config
from button import Button
from image import Image


from screen import View
from game_view import GameView
from init_view import InitView


class Game:
    carryOn = True
    clock = None
    actualView = View.START
    screen = pygame.display.set_mode(
        (config.size["width"], config.size["height"]))
    initView = None
    gameView = None
    font = None

    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont("lato", 22)
        self.clock = pygame.time.Clock()
        self.initView = InitView(self.screen)
        self.gameView = GameView(self.screen)

    def start(self, title):
        pygame.display.set_caption(title)

        while self.carryOn:
            # --- Main event loop
            events = pygame.event.get()
            self.update(events)
            for event in events:  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    carryOn = False  # Flag that we are done so we exit this loop
                    pygame.quit()

            pygame.display.flip()
            self.clock.tick(30)

    def startGame(self):
        self.actualView = View.GAME
        print("Started")

    def update(self, events):
        if self.actualView == View.START:
            return self.initView.render(self, self.screen, events)
        else:
            return self.gameView.render(self, self.screen, events)
