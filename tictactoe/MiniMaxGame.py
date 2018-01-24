from Const import Const
from Move import Move
from State import State
from RandomAgent import RandomAgent
from Agent import Agent
from HumanAgent import HumanAgent
from SmartAgent import SmartAgent
from MiniMaxAgent import MiniMaxAgent
import os
import time

class MiniMaxGame:
    abc ="abc"
    def __init__(self):
        self._state = State()
        self._agentX = MiniMaxAgent()
        self._agentO = HumanAgent()
        self._agentX.setName()
        self._agentO.setName()

    def turn(self):
        if self._state.getState() == Const.STATE_TURN_O:
            print("%s's turn" %self._agentO.getName())
            move = self._agentO.move(self._state)
            move.play(self._state)
        elif self._state.getState() == Const.STATE_TURN_X:
            print("%s's turn" %self._agentX.getName())
            move = self._agentX.move(self._state)
            move.play(self._state)

    def play(self):
        while self._state.getState() == Const.STATE_TURN_O or \
              self._state.getState() == Const.STATE_TURN_X:
            self.printBoard()
            self.turn()

        self.printBoard()
        print("game over")
        if self._state.getState() == Const.STATE_WIN_O:
            print("%s won!!" %self._agentO.getName())
        if self._state.getState() == Const.STATE_WIN_X:
            print("%s won!!" %self._agentX.getName())
        if self._state.getState() == Const.STATE_DRAW:
            print("draw")


    def printBoard(self):
        os.system("clear")
        print()
        board = self._state.getBoard()
        print("    1  2  3 ")
        for row in range(Const.ROWS):
            print("%s:  " %self.abc[row], end='')
            for col in range(Const.COLS):
                print(Const.PRINT_X_O[board[row][col]], "", end='')
                if col<Const.COLS-1:
                    print("|",end="")
            print()
            if row <Const.ROWS-1:
                print("   ---------")
        print()



if __name__ == '__main__':
    os.system("clear")
    game = MiniMaxGame()
    game.play()

