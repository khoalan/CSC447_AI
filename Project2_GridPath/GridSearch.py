# CSC447 Assignment 2
# Instructor: Dr.Plaku
# Author : Lan Nguyen
# StudentID: 5152815
# main file
import argparse
from collections import defaultdict
import collections
from QueueClass import Queue
from Search import Search

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('method', type=str, default=5, help="Method")
    parser.add_argument('grid', type=str, default="grid.txt", help="Input")
    parser.add_argument('rstart', type=int, default=0, help="Start row")
    parser.add_argument('cstart', type=int, default=0, help="Star collumn")
    parser.add_argument('rend', type=int, default=1, help="End row")
    parser.add_argument('cend', type=int, default=1, help="End collumn")
    parser.add_argument('output', type=str,default="path",
                        help="Output")

    args = parser.parse_args()
    f=open(args.output,'w')
    problem = Search(args.grid, args.rstart, args.cstart, args.rend, args.cend, args.method)
    print("Processing...")
    if args.method == "BFS":
        result = problem.BFS()
        if result!=False:
            path = problem.constructPath(result)
            for i in path:
                print(i[0],i[1],file = f)
        else:
            print("Cannot find any path to goal!")
            print("Cannot find any path to goal!", file=f)
    if args.method == "DFS":
        result = problem.DFS()
        if result!=False:
            path = problem.constructPath(result)
            for i in path:
                print(i[0],i[1],file = f)
        else:
            print("Cannot find any path to goal!")
            print("Cannot find any path to goal!", file=f)
    if args.method == "AStarZero":
        result = problem.AStarZero()
        if result!=False:
            path = problem.constructPath(result[0])
            for i in path:
                print(i[0],i[1],file = f)
        else:
            print("Cannot find any path to goal!")
            print("Cannot find any path to goal!", file=f)
    if args.method == "AStarManhattan" or args.method == "AStarEuclidean":
        result = problem.AStarHeuristic()
        if result!=False:
            path = problem.constructPath(result[0])
            for i in path:
                print(i[0],i[1],file = f)
        else:
            print("Cannot find any path to goal!")
            print("Cannot find any path to goal!", file=f)
    print("Finished!")
