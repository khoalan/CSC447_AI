# CSC447 Assignment 2
# Instructor: Dr.Plaku
# Author : Lan Nguyen
# StudentID: 5152815
# Search class
import collections
from QueueClass import Queue
from QueueClassForA import PriorityQ
from StackClass import Stack
import math

class Search:
    def __init__(self, grid, rstart, cstart, rend, cend, method):
        self.rstart = rstart
        self.cstart = cstart
        self.rend   = rend
        self.cend   = cend
        self.grid   = grid
        self.method = method

    def initial(self):
        f = open(self.grid,"r")
        size = []
        size = f.readline()
        size = size.split(' ')
        nRow = int(size[0])
        nCol = int(size[1])
        values = f.readline()
        values = values.split(' ')
        for i in range(len(values)):
            if values[len(values)-1] == '':
                values = values[:-1]
        for i in range(len(values)):
            values[i] = float(values[i])
            if values[i] != 0:
                values[i] = round(1/values[i],2)
            else :
                values[i] = 999
        #print(values[:nCol])
        #for i in range(nRow+1):
        #    i = i+1
        #    print(values[i*nCol:i*nCol+4])
        self.all_nodes = []
        for x in range(nRow):
            for y in range(nCol):
                self.all_nodes.append([x, y])
        for i in range(len(self.all_nodes)):
            self.all_nodes[i] = tuple(self.all_nodes[i])
        obj = zip(self.all_nodes, values)
        self.graph = dict(obj)
        return self.graph

    def neighbors(self, node):
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        result = []
        for dir in dirs:
            neighbor = [node[0] + dir[0], node[1] + dir[1]]
            if tuple(neighbor) in self.all_nodes:
                result.append(neighbor)
        return result

    def cost(self, node):
        return self.graph[tuple(node)]

    def BFS(self):
        start = (self.rstart, self.cstart)
        end = (self.rend, self.cend)
        graph = self.initial()
        frontier = Queue()
        frontier.put(start)
        visited = {}
        visited[start] = None

        while not frontier.empty():
            current = frontier.get()
            if tuple(current) == end:
                return visited
            for next in self.neighbors(current):
                if tuple(next) == end:
                    visited[tuple(next)] = tuple(current)
                    return visited
                if tuple(next) not in visited and graph[tuple(next)] != 999:
                    frontier.put(next)
                    visited[tuple(next)] = tuple(current)
        return False

    def DFS(self):
        start = (self.rstart, self.cstart)
        end = (self.rend, self.cend)
        graph = self.initial()
        frontier = Stack()
        frontier.push(start)
        visited = {}
        visited[start] = None

        while not frontier.empty():
            current = frontier.pop()
            if tuple(current) == end:
                return visited
            for next in self.neighbors(current):
                if tuple(next) == end:
                    visited[tuple(next)] = tuple(current)
                    return visited
                if tuple(next) not in visited and graph[tuple(next)] != 999:
                    frontier.push(next)
                    visited[tuple(next)] = tuple(current)
        return False

    def AStarZero(self):
        start = (self.rstart, self.cstart)
        end = (self.rend, self.cend)
        graph = self.initial()
        frontier = PriorityQ()
        frontier.put(start, 0)
        visited = {}
        visited[start] = None
        cost = {}
        cost[start] = 0
        while not frontier.empty():
            current = frontier.get()
            if tuple(current) == end:
                return visited, cost
            for next in self.neighbors(current):
                newCost = cost[current] + self.cost(next)
                if tuple(next) == end:
                    cost[tuple(next)] = newCost
                    visited[tuple(next)] = tuple(current)
                    return visited, cost
                if (tuple(next) not in cost or newCost < cost[tuple(next)]) and graph[tuple(next)] != 999:
                    cost[tuple(next)] = newCost
                    priority = newCost
                    frontier.put(tuple(next), priority)
                    visited[tuple(next)] = tuple(current)
        return False

    def manhattanHeuristic(self, endNode, fromNode):
        (x1,y1) = endNode
        (x2,y2) = fromNode
        return abs(x1 - x2) + abs(y1 - y2)

    def euclidHeuristic(self, endNode, fromNode):
        (x1,y1) = endNode
        (x2,y2) = fromNode
        return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

    def AStarHeuristic(self):
        start = (self.rstart, self.cstart)
        end = (self.rend, self.cend)
        graph = self.initial()
        frontier = PriorityQ()
        frontier.put(start, 0)
        visited = {}
        visited[start] = None
        cost = {}
        cost[start] = 0
        while not frontier.empty():
            current = frontier.get()
            if tuple(current) == end:
                return visited, cost
            for next in self.neighbors(current):
                newCost = cost[current] + self.cost(next)
                if tuple(next) == end:
                    cost[tuple(next)] = newCost
                    visited[tuple(next)] = tuple(current)
                    return visited, cost
                if (tuple(next) not in cost or newCost < cost[tuple(next)]) and graph[tuple(next)] != 999:
                    cost[tuple(next)] = newCost
                    if self.method == "AStarManhattan":
                        priority = newCost + self.manhattanHeuristic(end, tuple(next))
                    if self.method == "AStarEuclidean":
                        priority = newCost + self.euclidHeuristic(end, tuple(next))
                    frontier.put(tuple(next), priority)
                    visited[tuple(next)] = tuple(current)
        return False


    def constructPath(self, visited):
        start = (self.rstart, self.cstart)
        end = (self.rend, self.cend)
        current = end
        path = []
        while current != start:
            path.append(current)
            current = visited[current]
        path.append(start)
        path.reverse()
        return path
