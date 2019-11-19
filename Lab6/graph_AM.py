# Course: CS 2302 Data Structures
# Author: Alonso Monarrez (original source code provided by Olac Fuentes)
# Assignment: Lab 6 Graphs
# Instructor: Olac Fuentes
# TA: Anindita Nath
# Date of last modification: November 18
# Purpose: The purpose of this program is to implement functions that can be
# used for a graph represented as an adjacency matrix.
import numpy as np
import matplotlib.pyplot as plt
import math
import graph_AL as al_graph
import graph_EL as el_graph
from scipy.interpolate import interp1d

class Graph:
    # Constructor
    def __init__(self, vertices, weighted=False, directed = False):
        self.am = np.zeros((vertices,vertices),dtype=int)-1
        self.weighted = weighted
        self.directed = directed
        self.representation = 'AM'
        
    def insert_edge(self,source,dest,weight=1):
        """
        Insert an edge between two vertices of a graph represented as an
        adjacency matrix. This function handles graphs of different
        combinations between direction and weight properties.
        """
        if source >= len(self.am) or dest>=len(self.am) or source <0 or dest<0:
            print('Error, vertex number out of range')
        if weight!=1 and not self.weighted:
            print('Error, inserting weighted edge to unweighted graph')
        else:
            self.am[source][dest] = weight
            if not self.directed:
                self.am[dest][source] = weight
        
    def delete_edge(self,source,dest):
        """
        Delete an edge between two veritces of a graph represented as an 
        adjacency list. This function handles graphs of different combinations
        between direction and weight properties.
        """
        if source >= len(self.am) or dest>=len(self.am) or source <0 or dest<0:
            print('Error, vertex number out of range')
        else:
            self.am[source][dest] = -1
            if not self.directed:
                self.am[dest][source] = -1
                
    def display(self):
        """
        Print the adjacency matrix representation of the graph to the terminal.
        """
        print(self.am)
     
    def draw(self):
        """
        Convert the adjacency matrix representation of a graph to an adjacency
        list and call the draw() function from the adjacency list class to 
        show the actual vertices and edges of the graph.
        """
        AL = self.as_AL()
        AL.draw()
    
    def as_EL(self):
        """
        Convert an adjacency matrix representation of a graph to an edge list
        by traversing through the original representation and calling the
        insert_edge() function from the edge list class for each edge
        connecting two vertices, which is represented by the value of the edge
        weight in the adjacency matrix.
        """
        EL = el_graph.Graph(len(self.am), weighted=self.weighted, directed=self.directed)
        for s in range(len(self.am)):
            for d in range(len(self.am[s])):
                if self.am[s][d] > 0:
                    source = s
                    dest = d
                    weight = self.am[s][d]
                    EL.insert_edge(source, dest, weight)
        return EL
    
    def as_AM(self):
        """
        Return the adjacency matrix representation of the graph.
        """
        return self
    
    def as_AL(self):
        """
        Convert an adjacency matrix representation of a graph to an adjacency
        list by traversing through the original representation and calling the
        insert_edge() function from the adjacency list class for each edge
        connecting two vertices, which is represented by the value of the edge
        weight in the adjacency matrix.
        """
        AL = al_graph.Graph(len(self.am), weighted=self.weighted, directed=self.directed)
        for s in range(len(self.am)):
            for d in range(len(self.am[s])):
                if self.am[s][d] > 0:
                    source = s
                    dest = d
                    weight = self.am[s][d]
                    AL.insert_edge(source, dest, weight)
        return AL
    
    def BFS_AM(self):
        """
        Traverse through the graph by breadth-first search and use the 
        properties of the adjacency matrix representation to access the
        vertices adjacent to the current vertex. Return a list of integers as
        the path traversed by breadth-first search.
        """
        Q = []
        known = [False for i in range(len(self.am))]
        path = [-1 for i in range(len(self.am))]
        
        # Push the start vertex (0) to the queue.
        Q.append(0)
        # Add the start vertex to the "known" list of visited vertices.
        known[0] = True
        
        while len(Q) > 0:
            # Pop a vertex from the queue.
            currV = Q.pop(0)
            # Visit the current vertex to check for its adjacent vertices.
            for adjV in range(len(self.am[currV])):
                if self.am[currV][adjV] > 0:
                    if known[adjV] == False:
                        # Push the adjacent vertex to the queue.
                        Q.append(adjV)
                        # Add the adjacent vertex to the "known" list of 
                        # visited vertices.
                        known[adjV] = True
                        # Add the adjacent vertex to the path.
                        path[adjV] = currV
        return path
    
    def DFS_AM(self):
        """
        Traverse through the graph by depth-first search and use the 
        properties of the adjacency matrix representation to access the
        vertices adjacent to the current vertex. Return a list of integers as
        the path traversed by depth-first search.
        """
        S = []
        known = [False for i in range(len(self.am))]
        path = [-1 for i in range(len(self.am))]
        
        # Push the start vertex (0) to the stack.
        S.append(0)
        
        while len(S) > 0:
            # Pop a vertex from the stack.
            currV = S.pop()
            if known[currV] == False:
                # Visit the current vertex to check for its adjacent vertices.
                # Add the current vertex to the "known" list of visited
                # vertices.
                known[currV] = True
                for adjV in range(len(self.am[currV])):
                    if self.am[currV][adjV] > 0:
                        # Push the adjacent vertex to the stack.
                        S.append(adjV)
                        if known[adjV] == False:
                            # Add the adjacent vertex to the path.
                            path[adjV] = currV
        return path