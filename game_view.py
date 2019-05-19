
import pygame
import config
import random

from button import Button
from screen import Screen
from letter import Letter

width = config.size["width"]
height = config.size["height"]


class GameView(Screen):
    letters = []
    countNumbers = 8
    valuesToSwitch = ()

    def __init__(self,  screen):
        super().__init__(screen)
        self.setNewNumbers(screen)
        self.printValuesToSwitch()

    def randomValue(self):
        return random.randint(65, 90)

    def initNumbers(self, screen):
        w = (width - 80) / self.countNumbers
        a = []
        randomNumbers = random.sample(range(65, 90), self.countNumbers)
        for i in range(self.countNumbers):
            value = randomNumbers[i]

            l = Letter(screen, index=i, value=value, text=chr(value), x=i *
                       w + 40, y=150, w=w-8, h=120)
            a.append(l)
        return a

    def bubbleSort(self, arr):
        newArr = []
        for i in arr:
            newArr.append(i)

        for passnum in range(len(newArr)-1, 0, -1):
            for i in range(passnum):
                if newArr[i].value > newArr[i+1].value:
                    temp = newArr[i]
                    newArr[i] = newArr[i+1]
                    newArr[i+1] = temp
        return newArr

    def printNumbers(self, arr):
        newArr = []
        for el in arr:
            newArr.append(el.value)
        print(newArr)

    def printValuesToSwitch(self):
        print(self.valuesToSwitch)

    def setNewNumbers(self, screen):
        self.letters = self.initNumbers(screen)
        letters = self.letters
        self.sortedLetters = self.bubbleSort(letters)
        self.analyzeNextMove()

    def analyzeNextMove(self):
        newArr = []
        for i in self.letters:
            newArr.append(i)

        for passnum in range(len(newArr)-1, 0, -1):
            for i in range(passnum):
                if newArr[i].value > newArr[i+1].value:
                    self.setValuesToSwitch(
                        newArr[i].value, newArr[i+1].value)
                    return

    def setValuesToSwitch(self, firstNumber, secondNumber):
        self.valuesToSwitch = (firstNumber, secondNumber)

    def render(self, gameChanger, screen, events):
        screen.fill(config.colors["white"])

        for letter in self.letters:
            letter.render()

        startButton = Button(
            screen, onClick=lambda: self.setNewNumbers(screen), text="Zacznij od nowa", y=518)
        startButton.render(events)
