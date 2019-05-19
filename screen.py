
import pygame
import config

from enum import Enum
from button import Button
from image import Image


class View(Enum):
    START = 1
    GAME = 2


class Screen:
    def __init__(self, screen):
        screen.fill(config.colors["white"])
