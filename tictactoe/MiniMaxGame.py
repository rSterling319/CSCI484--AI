from Const import Const
from Move import Move
from Game import Game
from Agent import Agent
from HumanAgent import HumanAgent
from MiniMaxAgent import MiniMaxAgent
from SmartAgent import SmartAgent
import os
import time
import random

class MiniMaxGame:
    abc ="abc"
    def __init__(self):
        self._state = Game()
        self._agentX = None
        self._agentO = None
        self.chooseFirstPlay()
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

        #print the cache size
        #if self._agentO.__class__.__name__ == "MiniMaxAgent":
        print(len(self._agentO._cache))
        #else:
        print(len(self._agentX._cache))



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

    def chooseFirstPlay(self):
        rand = random.randint(1,2)
        # if rand % 2 == 0:
        #     self._agentX = MiniMaxAgent(Const.MARK_X)
        #     self._agentO = HumanAgent(Const.MARK_O)
        # else:
        #     self._agentO = MiniMaxAgent(Const.MARK_O)
        #     self._agentX = HumanAgent(Const.MARK_X)

        self._agentX = MiniMaxAgent(Const.MARK_X)
        self._agentO = MiniMaxAgent(Const.MARK_O)



if __name__ == '__main__':
    os.system("clear")
    game = MiniMaxGame()
    game.play()

