import random
from Const import Const
from Move import Move
from Game import Game
from Agent import Agent

class HumanAgent(Agent):
    rowDict = {"a":0,"b":1,"c":2}
    def __init__(self, _xORo):
        super().__init__(_xORo)

    def move(self, state):
        mark = None
        if state.getState() == Const.STATE_TURN_O:
            mark = Const.MARK_O
        if state.getState() == Const.STATE_TURN_X:
            mark = Const.MARK_X
        if mark == None:
            raise ValueError("state must be playable")
        board = state.getBoard()
        playable = []
        for row in range(Const.ROWS):
            for col in range(Const.COLS):
                if board[row][col] == Const.MARK_NONE:
                    playable.append([row,col])
        spot= self.getSpot(input("make a move: "))
        return Move(spot[0],spot[1],mark)

    def getSpot(self, coords):
        return [self.rowDict[coords[0]],int(coords[1])-1]

    def setName(self):
        self._name = input("Enter your name: ")
