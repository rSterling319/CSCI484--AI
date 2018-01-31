# 1) get current state of board
# 2) get list of possible moves
# 3) iterate through list
# 4) making move then check for win, draw, loss  (1,0,-1) (pass through a number decriments with each recursion to add so fastest move to win)
# 5) continue through for each possible move

import copy
import random
from Const import Const
from Move import Move
from Game import Game
from Agent import Agent
import time
import random

class MiniMaxAgent(Agent):
    abc = {0:'a',1:'b',2:'c'}

    def __init__(self, _side):
        self._cache = {}
        super().__init__(_side)

    def value(self,game):
        ans = None
        state = game.getState()
        #Get touple of board and state
        h_val = str(game.getBoard()), state
        try:
            #see if the current board/state exists in dict
            return self._cache[h_val]

        except KeyError:

            if state == Const.STATE_WIN_O:
                if self.side == Const.MARK_O: ans = 1
                else: ans = -1
            elif state == Const.STATE_WIN_X:
                if self.side == Const.MARK_X: ans = 1
                else: ans = -1
            elif state == Const.STATE_DRAW:
                ans = 0

            if ans != None: return (ans,0)

            iside = 0
            if self.side == Const.MARK_O: iside = 1
            else: iside = -1

            iturn = 0
            if state == Const.STATE_TURN_O: iturn = 1
            else: iturn = -1

            myTurn = (iside == iturn)
            myOptions = 0

            for move in game.getMoves():
                move.play(game)
                (moveValue,moveOptions)=self.value(game)
                move.unplay(game)
                myOptions = myOptions + 1 + moveOptions
                if ans == None:
                    ans = moveValue
                else:
                    if myTurn:
                       ans = max(ans,moveValue)
                    else:
                       ans = min(ans,moveValue)
            #cache value of board/state
            self._cache[h_val] = (ans,myOptions)
            return (ans,myOptions)



    def move(self,game):
        print("make a move: ", end='', flush=True)
        (maxValue,maxOptions)=self.value(game)
        playable = []
        maxPlayableOption = 0
        for move in game.getMoves():
            move.play(game)
            (moveValue,moveOptions)=self.value(game)
            move.unplay(game)
            if moveValue == maxValue:
                playable.append((move,moveOptions))
                maxPlayableOption = max(maxPlayableOption,moveOptions)

        bestPlayable = []
        for (move,options) in playable:
            if options == maxPlayableOption:
                bestPlayable.append(move)

        spot=random.randint(0,len(bestPlayable)-1)



        time.sleep(1)
        print(self.abc[bestPlayable[spot].getRow()], end='', flush=True)
        time.sleep(1/random.randint(1,5))
        print(bestPlayable[spot].getCol()+1, end='', flush=True)
        time.sleep(1)
        return bestPlayable[spot]



    def setName(self):
        self._name = Const.AI_NAMES[random.randint(0, len(Const.AI_NAMES)-1)]
        print("You are playing against: ", end='')
        for let in self._name:
            print(let, end="",flush=True)
            time.sleep(1/random.randint(2,10))
        print()



