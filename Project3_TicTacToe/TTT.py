# CSC447 Assignment 3
# Instructor: Dr.Plaku
# Author : Lan Nguyen
# StudentID: 5152815

from board import Board
from player import Player
import argparse

if __name__ == "__main__":

    #TTT nrRows nrCols nrToWin player1Type player2Type depth
    parser = argparse.ArgumentParser()
    parser.add_argument('Row', type=int, default=3, help="Number of rows!")
    parser.add_argument('Col', type=int, default=3, help="Number of column!")
    parser.add_argument('W', type=int, default=3, help="Number to win!")
    parser.add_argument('P1', type=str, default="RANDOM", help="Player1 type!")
    parser.add_argument('P2', type=str, default="AI", help="Player2 type!")
    parser.add_argument('D', type=int, default=2, help="Depth!")
    args = parser.parse_args()
    B = Board(args.Row,args.W)
    B.print()


    def gamePlay(pl1, pl2):
        if pl1 == "human" and pl2 == "human":
            player1 = Player(1, 0)
            player2 = Player(2, 0)
        elif pl1 == "human" and pl2 == "ai":
            player1 = Player(1, 0)
            player2 = Player(2, 2, args.D)
        elif pl1 == "ai" and pl2 == "human":
            player1 = Player(1, 2, args.D)
            player2 = Player(2, 0)
        elif pl1 == "random" and pl2 =="ai":
            player1 = Player(1, 1)
            player2 = Player(2, 2, args.D)
        elif pl1 == "ai" and pl2 =="random":
            player1 = Player(1, 2, args.D)
            player2 = Player(1, 1)
        while B.endGame()==False:
            print("================")
            print("Player 1! ")
            p1 = player1.chooseMove(B)
            B.makeMove(1,p1)
            B.print()
            print("================")
            if B.endGame():
                break
            print("Player 2! ")
            p2 = player2.chooseMove(B)
            B.makeMove(2,p2)
            B.print()
        if B.isWin('[X]'):
            print(pl1,"win!")
        elif B.isWin('[O]'):
            print (pl2,"win!")
        else: print("Tie!")

    gamePlay(args.P1.lower(),args.P2.lower())
    print("Game over!")
