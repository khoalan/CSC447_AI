# CSC447 Assignment 1
# Instructor: Dr.Plaku
# Author : Lan Nguyen
# StudentID: 5152815
# main file
import argparse
from QueensSearch import QueensSearch

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('N', type=int, default=5, help="Number of rows!")
    parser.add_argument('M', type=int, default=4, help="Number of column!")
    parser.add_argument('W', type=int, default=4, help="Number of white queens!")
    parser.add_argument('B', type=int, default=2, help="Number of black queens!")
    parser.add_argument('tmax', type=int, default=100, help="Upper bound of runtime(seconds)!")
    parser.add_argument('output',type=str,default="solution.txt",
    help="Output file name!")
    args = parser.parse_args()
    f=open(args.output+'.txt','w')

    problem = QueensSearch(args.N, args.M, args.W, args.B, args.tmax)

    board = problem.search()
    if problem.violationCount(board)==0:
        print("Solution found:")
        problem.printB(board)
        for i in range(args.N):
            for j in range(args.M):
                print(board[i][j],end ="",file=f)
            print('|',file=f)
        print('YES',file=f)
        print("Check out the output file for requirement result!")
    else:
        print("Not found")
        print("Check out the output file for requirement result!")
        print('NO',file=f)
