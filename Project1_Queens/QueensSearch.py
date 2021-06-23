# CSC447 Assignment 1
# Instructor: Dr.Plaku
# Author : Lan Nguyen
# StudentID: 5152815
# QueensSearch class

from random import choice
from collections import Counter
from random import randrange
import copy
import random
from time import time

class QueensSearchIni:
    def __init__(self, initial = None):
        pass
    def initial(self):
        pass
    def violationCount(self,board):
        pass
    def findNeighbor(self):
        pass
    def hillClimb(self,board):
        pass
    def search(self,board):
        pass
    def printB(self):
        pass
    def convert2D(self,board):
        pass

class QueensSearch(QueensSearchIni):
    def __init__(self, N, M, W, B,tmax):
        self.N=N
        self.M=M
        self.W=W
        self.B=B
        self.tmax=tmax
    def initial(self):
        self.board = [['| ' for x in range(self.M)] for y in range(self.N)]
        self.list = random.sample(range(0,self.N*self.M), self.W+self.B)
        count=0
        for i in range(self.N):
            for j in range(self.M):
                for x in range(len(self.list)):
                    if count==self.list[x] and x < self.W:
                        self.board[i][j] = '|W'
                    elif count==self.list[x] and x >= self.W:
                        self.board[i][j] = '|B'
                count+=1

        return self.board
    def violationCount(self,boardC):
        cost=0
        board=boardC
        for i in range(self.N):
            for j in range(self.M):
                if board[i][j] == '|W':
                    for x in range(self.N):
                        for y in range(self.M):
                            if board[x][y] == '|B' and (x==i or y==j
                            or abs(i-x)==abs(j-y)):
                                cost = cost+1
        return cost
    def convert2D(self,board):
        boardConverted= [['| ' for x in range(self.M)] for y in range(self.N)]
        index = 0
        for i in range(self.N):
            for j in range(self.M):
                boardConverted[i][j] = board[index]
                index=index+1
        return boardConverted
    def findNeighbor(self,board):
        count=0
        neigh = copy.deepcopy(board)
        currentVal=self.violationCount(board)
        neigh1d=[]
        for element in neigh:
            for sub in element:
                neigh1d.append(sub)
        for i in range(len(neigh1d)):
            if neigh1d[i]!='| ':
                t1=i
                for j in range(len(neigh1d)):
                    if neigh1d[j]=='| ':
                        neigh1d[j],neigh1d[t1]=neigh1d[t1],neigh1d[j]
                        t1=j
                    neigh=self.convert2D(neigh1d)
                    if self.violationCount(neigh)<currentVal:
                        return neigh
        neigh = self.convert2D(neigh1d)

        return neigh
    def hillClimb(self):
        state = self.initial()
        current = copy.deepcopy(state)
        count=0
        limit = ((self.N*self.M)-(self.W+self.B))*(self.W+self.B)

        while self.violationCount(current) != 0 or count<(limit/4):
            neighbour = self.findNeighbor(current)
            if self.violationCount(neighbour) < self.violationCount(current):
                current = copy.deepcopy(neighbour)
                count = count +1
            else:
                break
        return current
    def search(self):
        print("Processing...")
        start = time()
        timeLimit = 0
        result = self.hillClimb()
        while self.violationCount(result) != 0 and timeLimit < self.tmax:
            result = self.hillClimb()
            end=time()
            timeLimit=end-start
        if timeLimit < self.tmax :
            print("Time =",round(timeLimit,2))
        else: print("Time out!")
        return result
    def printB(self,board):
        for i in range(self.N):
            for j in range(self.M):
                print(board[i][j],end ="")
            print('|\n')
