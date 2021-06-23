# CSC447 Assignment 3
# Instructor: Dr.Plaku
# Author : Lan Nguyen
# StudentID: 5152815

class Board:
    def __init__(self, size, nrToWin):
        self.Size = size
        self.board = [' ']*(self.Size*self.Size)
        self.nrToWin = nrToWin

    def __repr__(self):
        value=''
        for i in range(len(self.board)):
            if self.board[i] == " ":
                value += str(i) + "  "
            else:
                value+=self.board[i]
            if (i+1) % self.Size == 0:
                value += "\n"
        return value

    def legalMove(self, player, move):
        return move in self.legalMoves(player)

    def legalMoves(self, player):
        moves = []
        for i in range( len(self.board)):
            if self.board[i] == ' ':
                moves += [i]
        return moves

    def makeMove(self, player, position):
        move = position
        if move not in range(len(self.board)) or self.board[move] != ' ':
            return False
        if player == 1:
            self.board[move] = '[X]'
        else:
            self.board[move] = '[O]'
        return True

    def isRowWin(self, token):
        for i in range(self.Size):
            for j in range(self.Size-self.nrToWin+1):
                if self.board[j+i*self.Size:self.nrToWin+j+i*self.Size] == [token]*self.nrToWin:
                    return True
        return False

    def isColWin(self, token):
        for i in range(self.Size):
            col = []
            for j in range(self.Size):
                col += [self.board[j*self.Size+i]]
            for j in range(self.Size-self.nrToWin+1):
                if col[j:self.nrToWin+j] == [token]*self.nrToWin:
                    return True
        return False

    def isDiaWin(self, token):
        diagUp = []
        diagDown = []
        for i in range(self.Size):
            diagRight = []
            diagLeft = []
            j = i
            k = 0
            while j < self.Size:
                diagRight += [self.board[j*self.Size+j-i]]
                diagLeft += [self.board[(j+1)*self.Size-j-1+i]]
                j += 1
            diagUp.append(diagRight)
            diagDown.append(diagLeft)
            diagRight = []
            diagLeft = []
            while k < self.Size-i:
                diagRight += [self.board[k*self.Size+k+i]]
                diagLeft += [self.board[(k+1)*self.Size-k-1-i]]
                k += 1
            diagUp.append(diagRight)
            diagDown.append(diagLeft)
        for i in diagUp:
            for j in range(self.Size-self.nrToWin+1):
                if i[j:self.nrToWin+j] == [token]*self.nrToWin:
                    return True
        for i in diagDown:
            for j in range(self.Size-self.nrToWin+1):
                if i[j:self.nrToWin+j] == [token]*self.nrToWin:
                    return True
        return False

    def isWin(self, token):
        return self.isRowWin(token) or self.isColWin(token) or self.isDiaWin(token)

    def isPlayerWin(self, playerOrder):
        if playerOrder == 1:
            return self.isWin('[X]')
        else:
            return self.isWin('[O]')

    def endGame(self):
        if self.isWin('[X]') or self.isWin('[O]'):
            return True
        else:
            for i in self.board:
                if i == ' ':
                    return False
            return True

    def print(self):
        for i in range(len(self.board)):
            print('%2s'%i,end='')
            if self.board[i] == ' ':
                print('[ ]',end='')
            else: print(self.board[i],end='')
            if (i+1) % self.Size == 0:
                print('\n')
