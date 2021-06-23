# CSC447 Assignment 2
# Instructor: Dr.Plaku
# Author : Lan Nguyen
# StudentID: 5152815
# Stack class
import collections

class Stack:
     def __init__(self):
         self.elements = []

     def empty(self):
         return self.elements == []

     def push(self, x):
         self.elements.append(x)

     def pop(self):
         return self.elements.pop()
