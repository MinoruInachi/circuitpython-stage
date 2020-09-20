"""
A helper module that initializes the display and buttons for the uGame
game console. See https://hackaday.io/project/27629-game
"""

import board
import digitalio
import analogio
import gamepad
import stage


K_X = 0x01
K_DOWN = 0x02
K_LEFT = 0x04
K_RIGHT = 0x08
K_UP = 0x10
K_O = 0x20
K_START = 0x40
K_SELECT = 0x80


display = board.DISPLAY
buttons = gamepad.GamePad(
    digitalio.DigitalInOut(board.SWITCH_PRESS),
    digitalio.DigitalInOut(board.SWITCH_DOWN),
    digitalio.DigitalInOut(board.SWITCH_LEFT),
    digitalio.DigitalInOut(board.SWITCH_RIGHT),
    digitalio.DigitalInOut(board.SWITCH_UP),
    digitalio.DigitalInOut(board.BUTTON_1),
    digitalio.DigitalInOut(board.BUTTON_2),
    digitalio.DigitalInOut(board.BUTTON_3)
)

class DummyAudio:
    def play(self, f, loop=False):
        pass

    def stop(self):
        pass

    def mute(self, mute):
        pass

audio = DummyAudio()

