import random
from Const import Const
from Move import Move
from State import State
from Agent import Agent
import time
import random

class RandomAgent(Agent):
    abc = {0:'a',1:'b',2:'c'}
    def __init__(self, _xORo):
        super().__init__(_xORo)

    def move(self,state):
        mark = None
        if state.getState() == Const.STATE_TURN_O:
            mark = Const.MARK_O
        if state.getState() == Const.STATE_TURN_X:
            mark = Const.MARK_X
        if mark == None:
            raise ValueError("state must be playable")
        board = state.getBoard()
        playable = state.getPlayable()
        print("make a move: ", end='', flush=True)
        time.sleep(1)
        spot=random.randint(0,len(playable)-1)
        print(self.abc[playable[spot][0]], end='', flush=True)
        time.sleep(1/random.randint(1,5))
        print(playable[spot][1]+1, end='', flush=True)
        time.sleep(1)

        return Move(playable[spot][0],playable[spot][1],mark)

    def setName(self):
        self._name = Const.AI_NAMES[random.randint(0, len(Const.AI_NAMES)-1)]
        print("You are playing against: ", end='')
        for let in self._name:
            print(let, end="",flush=True)
            time.sleep(1/random.randint(2,10))
        print()

