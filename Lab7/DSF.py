# Course: CS 2302 Data Structures
# Author: Alonso Monarrez (original source code provided by Olac Fuentes)
# Assignment: Lab 7 Algorithm Design Techniques
# Instructor: Olac Fuentes
# TA: Anindita Nath
# Date of last modification: December 6
# Purpose: The purpose of this program is to create a disjoint set forest of a
# graph represented as an adjacency list in order to find the number of 
# connected components of the graph.
import numpy as np

class DSF:
    # Constructor
    def __init__(self, sets):
        self.parent = np.zeros(sets,dtype=int)-1
      
    def find(self,i):
        """
        Return the root of the tree that i belongs to
        """
        if self.parent[i]<0:
            return i
        return self.find(self.parent[i])

    def union(self,i,j):
        """
        Make the root of the tree of j point to the root of the tree of i if
        the two roots are different. Return 1 if a parent reference is changed.
        Otherwise, return 0.
        """
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_j] = root_i
            return 1
        return 0 