# CSC447 Assignment 2
# Instructor: Dr.Plaku
# Author : Lan Nguyen
# StudentID: 5152815
# Queue for A* search
import heapq

class PriorityQ:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]
