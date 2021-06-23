# CSC447 Assignment 3
# Instructor: Dr.Plaku
# Author : Lan Nguyen
# StudentID: 5152815


from random import *
from copy import *
from decimal import *


INF = 99999

class Player:

    HUMAN = 0
    RANDOM = 1
    AI = 2

    def __init__(self, playerOder, playerType, depth=0):

        self.current = playerOder
        self.oponent = 2 - playerOder + 1
        self.type = playerType
        self.depth = depth

    def __repr__(self):
        return str(self.current)

    def evaluation(self, board):
        if board.isPlayerWin(self.current):
            return 100.0
        elif board.isPlayerWin(self.oponent):
            return -100.0
        else: return 0.0

    def alphaBeta(self, board,depth,isMax,alpha,beta,com,lvl):
        oponentOrder = 0
        if com == 1 and self.type == 2:
            oponentOrder = 2
        if com == 2 and self.type == 2:
            oponentOrder = 1
        if depth == 0 or board.endGame():
            return self.evaluation(board)
        if isMax:
            value = -INF
            for i in board.legalMoves(self):
                if depth == 0 or board.endGame():
                    return self.evaluation(board)
                next1 = deepcopy(board)
                next1.makeMove(com, i)
                value = max(value, self.alphaBeta(next1,depth-1,not isMax,alpha,beta,com,lvl+1))
                alpha = max(alpha,value)
                if depth == 0 or board.endGame():
                    return self.evaluation(board)
                if alpha >= beta:
                    break
            return value
        else:
            value = INF
            for i in board.legalMoves(self):
                if depth == 0 or board.endGame():
                    return self.evaluation(board)
                next = deepcopy(board)
                next.makeMove(oponentOrder, i)
                #if next.isWin('[X]'):
                #    print("Next move:\n",next)
                value = min(value, self.alphaBeta(next,depth-1,not isMax,alpha,beta,com,lvl+1)+lvl)
            #    if next.isWin('[X]'):
                #    print("Next value:\n",value)
                beta = min(beta,value)
                if depth == 0 or board.endGame():
                    return self.evaluation(board)
                if alpha >= beta:
                    break
            return value

    def bestMove(self, board, com):
        oponentOrder = 0
        if com == 1 and self.type == 2:
            oponentOrder = 2
        if com == 2 and self.type == 2:
            oponentOrder = 1
        bestVal = -INF
        bestMove = -1
        for i in board.legalMoves(self):
            if self.depth == 0 or board.endGame():
                return self.evaluation(board)
            next = deepcopy(board)
            next.makeMove(com, i)
            #print("Next move:\n",next)
            moveVal = self.alphaBeta(next,self.depth,False,-INF,INF,com,0)
            #print("Next value:\n",moveVal)
            
            if moveVal > bestVal:
                bestMove = i
                bestVal = moveVal
        return bestMove
    def chooseMove(self, board):

        if self.type == 0:
            move = input("Enter move: ")
            while not board.legalMove(self, int(move)):
                print("Invalid move!")
                move = input("Enter move: ")
            return int(move)
        elif self.type == self.AI:
            m = self.bestMove(board,self.current)
            return int(m)
        elif self.type == self.RANDOM:
            move = choice(board.legalMoves(self))
            return int(move)
        else:
            print("Unknow!")
