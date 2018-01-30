import random
from Const import Const
from Move import Move
from Game import Game

class Agent:
    def __init__(self, _side):
        self._name = None
        self.side = _side
        self.winCondition = self.setWinConst()
        self.loseCondition = self.setLoseConst()

    def move(self, state):
        pass

    def setName(self):
        pass
    def getName(self):
        return self._name

    def setWinConst(self):
        if self.side == Const.MARK_O:
            return Const.STATE_WIN_O
        elif self.side == Const.MARK_X:
            return Const.STATE_WIN_X
        else:
            raise ValueError("Must be x or o")

    def setLoseConst(self):
        if self.side == Const.MARK_O:
            return Const.STATE_WIN_X
        elif self.side == Const.MARK_X:
            return Const.STATE_WIN_O
        else:
            raise ValueError("Must be x or o")