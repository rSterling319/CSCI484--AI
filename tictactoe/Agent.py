import random
from Const import Const
from Move import Move
from State import State

class Agent:
    def __init__(self, _xORo):
        self._name = None
        self.xORo = _xORo
        self.winCondition = self.setWinConst()
        self.loseCondition = self.setLoseConst()

    def move(self, state):
        pass

    def setName(self):
        pass
    def getName(self):
        return self._name

    def setWinConst(self):
        if self.xORo == Const.MARK_O:
            return Const.STATE_WIN_O
        elif self.xORo == Const.MARK_X:
            return Const.STATE_WIN_X
        else:
            raise ValueError("Must be x or o")

    def setLoseConst(self):
        if self.xORo == Const.MARK_O:
            return Const.STATE_WIN_X
        elif self.xORo == Const.MARK_X:
            return Const.STATE_WIN_O
        else:
            raise ValueError("Must be x or o")