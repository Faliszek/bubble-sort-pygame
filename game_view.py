
import pygame
import config
import random

from button import Button
from screen import Screen
from letter import Letter
from frame import Frame
from message import Message
from enum import Enum

width = config.size["width"]
height = config.size["height"]


class Move(Enum):
    START = 1
    SUCCESS = 2
    FAILURE = 3
    VICTORY = 4


class GameView(Screen):
    letters = []
    countNumbers = 8
    valuesToSwitch = []
    win = False
    buttonY = 150
    buttonH = 120
    buttonW = w = (width - 80) / countNumbers
    buttonX = 40
    selectedValues = []
    frameX = buttonX
    frameY = 150
    frameW = buttonW * 2
    frameH = buttonH
    framePosition = 0
    message = """Zmieniaj elementy, w takiej kolejności jakiej zrobiłby to algorytm sortowania bąbelkowego!"""
    lastMove = Move.START
    switches = 0
    frames = []
    letterBg = config.colors["darkBlue"]

    def __init__(self,  screen):
        super().__init__(screen)
        self.setNewNumbers(screen)
        self.printValuesToSwitch()

    def randomValue(self):
        return random.randint(65, 90)

    def initNumbers(self, screen):
        w = self.buttonW
        a = []
        randomNumbers = random.sample(range(65, 90), self.countNumbers)
        # randomNumbers = range(66, 90)
        for i in range(self.countNumbers):
            value = randomNumbers[i]

            l = Letter(screen, index=i, value=value, text=chr(
                value), x=self.buttonX, y=self.buttonY, w=w, h=120)
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

    def toNumbers(self, arr):
        newArr = []
        for el in arr:
            newArr.append(el.value)
        return newArr

    def toLetters(self, arr):
        newArr = []
        for el in arr:
            newArr.append(el.text)
        return newArr

    def printNumbers(self, arr):
        newArr = self.toNumbers(arr)
        print(newArr)

    def printLetters(self, arr):
        newArr = self.toLetters(arr)
        print(newArr)

    def __str__(self):
        newArr = []
        for el in self.letters:
            newArr.append(el.text)
        return ",".join(newArr)

    def printValuesToSwitch(self):
        if len(self.valuesToSwitch) == 2:
            f = self.valuesToSwitch[0]
            s = self.valuesToSwitch[1]
        else:
            print("Nie poprawna tupla")
            self.win = True

    def setNewNumbers(self, screen):
        self.letters = self.initNumbers(screen)
        letters = self.letters
        self.sortedLetters = self.bubbleSort(letters)
        self.analyzeNextMove()
        self.printValuesToSwitch()

        if len(letters) > 2:
            self.setSelectedValues(letters[0], letters[1])

    def restartGame(self, screen):
        self.setNewNumbers(screen)
        self.lastMove = Move.START
        self.message = """Zmieniaj elementy, w takiej kolejności jakiej zrobiłby to algorytm sortowania bąbelkowego!"""
        self.setLetterBg()

    def analyzeNextMove(self):
        newArr = []
        frames = []
        framePosition = 0
        loop = 0
        for i in self.letters:
            newArr.append(i)
        switched = False
        for passnum in range(len(newArr)-1, 0, -1):
            framePosition = 0
            for i in range(passnum):
                if newArr[i].value > newArr[i+1].value:
                    frames.append(framePosition)
                    temp = newArr[framePosition]
                    newArr[framePosition] = newArr[framePosition+1]
                    newArr[framePosition + 1] = temp
                framePosition += 1

        self.frames = frames
        print(self.frames)

    def setValuesToSwitch(self, firstNumber, secondNumber):
        self.valuesToSwitch = [firstNumber, secondNumber]

    def setSelectedValues(self, firstNumber, secondNumber):
        self.selectedValues = [firstNumber, secondNumber]

    def updateFramePosition(self, event):
        if self.framePosition <= 5 and event == pygame.K_RIGHT:
            self.framePosition = self.framePosition + 1
        if self.framePosition >= 1 and event == pygame.K_LEFT:
            self.framePosition = self.framePosition - 1

    def switchElements(self):
        if self.framePosition <= 6 and self.framePosition >= 0:
            # We switch whole element but in the end we want
            # index stame the same, so we swap those again
            framePosition = self.framePosition
            arr = self.letters
            temp = arr[framePosition]
            arr[framePosition] = arr[framePosition+1]
            arr[framePosition + 1] = temp

            tempIndex = arr[framePosition].index
            arr[framePosition].index = arr[framePosition+1].index
            arr[framePosition + 1].index = tempIndex

            self.letters = arr
            self.setLastMove()
            self.moveToText()
            self.switches = +1
            print(self.frames)

    def setLastMove(self):
        if len(self.frames) != 0:
            nextMove = self.frames.pop(0)
            if nextMove == self.framePosition:
                self.lastMove = Move.SUCCESS
            else:
                self.lastMove = Move.FAILURE

        if len(self.frames) == 0:
            self.lastMove = Move.VICTORY

        self.setLetterBg()

    def moveToText(self):
        if self.lastMove == Move.START:
            self.message = """Zmieniaj elementy, w takiej kolejności jakiej zrobiłby to algorytm sortowania bąbelkowego!"""
        elif self.lastMove == Move.FAILURE:
            self.message = """UPS! Niestety nie udało się, kliknij Zacznij od nowa i spróbój ponownie!"""
        elif self.lastMove == Move.SUCCESS:
            self.message = """YAY! Oby tak dalej!"""
        elif self.lastMove == Move.VICTORY:
            self.message = """Gratulacje! Chcesz zagrać jeszcze raz, kliknij Zacznij od nowa"""
        print(self.message)

    def setLetterBg(self):
        if self.lastMove == Move.START or self.lastMove == Move.SUCCESS:
            self.letterBg = config.colors["darkBlue"]
        elif self.lastMove == Move.FAILURE:
            self.letterBg = config.colors["red"]
        elif self.lastMove == Move.VICTORY:
            self.letterBg = config.colors["green"]

    def render(self, gameChanger, screen, events):
        screen.fill(config.colors["white"])

        for letter in self.letters:
            letter.render(screen=screen, index=letter.index, value=letter.value,
                          text=letter.text, x=letter.x, y=letter.y, w=letter.w, h=letter.h, bg=self.letterBg)

        startButton = Button(
            screen, onClick=lambda: self.restartGame(screen), text="Zacznij od nowa", y=518)
        startButton.render(events)

        message = Message(h=100, w=0.6, text=self.message)
        message.render(screen=screen, h=100, w=0.6, text=self.message)

        if self.lastMove == Move.SUCCESS or self.lastMove == Move.START:
            frame = Frame(x=self.buttonX + (self.framePosition * self.buttonW), y=self.frameY,
                          h=self.frameH, w=self.frameW)
            frame.render(screen, events)

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.updateFramePosition(event.key)
                    print(self.framePosition)
                if event.key == pygame.K_SPACE:
                    self.switchElements()
