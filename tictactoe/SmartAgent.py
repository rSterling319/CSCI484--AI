# 1) get current state of board
# 2) get list of possible moves
# 3) iterate through list
# 4) making move then check for win, draw, loss  (1,0,-1) (pass through a number decriments with each recursion to add so fastest move to win)
# 5) continue through for each possible move

import copy
import random
from Const import Const
from Move import Move
from State import State
from Agent import Agent
import time
import random

class SmartAgent(Agent):
    abc = {0:'a',1:'b',2:'c'}
    def __init__(self):
        super().__init__()



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
        if len(playable) > 6:
            #pick random spot
            spot=playable[random.randint(0,len(playable)-1)]
        else:
            #lookAhead play best scoring
            playScoreList =[]
            blockWin = None
            for play in playable:
                spot=play
                #if win (for x) detected use the move that does not produce a win!:
                #FIXME make move if next move is a win
                blockWin = self.checkImmediateLoss(state,spot)
                if blockWin:
                    break
                playScoreList.append(self.lookAhead(state,spot, 100))
            if blockWin:
                spot = blockWin
            else:
                spot = playable[playScoreList.index(max(playScoreList))]


        print("make a move: ", end='', flush=True)
        time.sleep(1)
        print(self.abc[spot[0]], end='', flush=True)
        time.sleep(1/random.randint(1,5))
        print(spot[1]+1, end='', flush=True)
        time.sleep(1)
        return Move(spot[0],spot[1],mark)

    def lookAhead(self,_state,spot,level):
        mark=None
        state=copy.deepcopy(_state)

        if state.getState()==Const.STATE_WIN_X:
            return 10*level
        elif state.getState()==Const.STATE_WIN_O:
            return -10*level
        elif state.getState()==Const.STATE_DRAW:
            return 0
        else:
            if state.getState() == Const.STATE_TURN_O:
                mark = Const.MARK_O
            if state.getState() == Const.STATE_TURN_X:
                mark = Const.MARK_X
            if state.getState() == None:
                raise ValueError("state must be playable")

            state.move(spot[0],spot[1],mark)
            value = 0
            for play in state.getPlayable():
                look = self.lookAhead(state, play, level-10)
                if look == None:
                    print("look = none")
                    look=0
                value += look
            return value

    def setName(self):
        self._name = Const.AI_NAMES[random.randint(0, len(Const.AI_NAMES)-1)]
        print("You are playing against: ", end='')
        for let in self._name:
            print(let, end="",flush=True)
            time.sleep(1/random.randint(2,10))
        print()


    def checkImmediateLoss(self, _state, spot):
        state = copy.deepcopy(_state)
        mark = state.getState()
        state.move(spot[0],spot[1], mark)
        #return the move that gives a win
        if state.getState() == Const.STATE_WIN_X:
            return spot
        for play in state.getPlayable():
            state.move(play[0],play[1], state.getState())
            #return the move that gives O a win (so you block it)
            if state.getState() == Const.STATE_WIN_O:
                return play
            state.unmove(play[0],play[1])

