# Course: CS 2302 Data Structures
# Author: Alonso Monarrez (original source code provided by Olac Fuentes)
# Assignment: Lab 6 Graphs
# Instructor: Olac Fuentes
# TA: Anindita Nath
# Date of last modification: November 18
# Purpose: The purpose of this program is to implement functions that can be
# used for a graph represented as an edge list.
import numpy as np
import matplotlib.pyplot as plt
import math
import graph_AL as al_graph
import graph_AM as am_graph
from scipy.interpolate import interp1d

class Edge:
    # Constructor
    def __init__(self, source, dest, weight=1):
        self.source = source
        self.dest = dest
        self.weight = weight
        
class Graph:
    # Constructor
    def __init__(self, vertices, weighted=False, directed = False):
        self.vertices = vertices
        self.el = []
        self.weighted = weighted
        self.directed = directed
        self.representation = 'EL'
        
    def insert_edge(self,source,dest,weight=1):
        """
        Insert an edge between two vertices of a graph represented as an
        edge list. This function handles graphs of different combinations
        between direction and weight properties.
        """
        if source >= self.vertices or dest>=self.vertices or source <0 or dest<0:
            print('Error, vertex number out of range')
        if weight!=1 and not self.weighted:
            print('Error, inserting weighted edge to unweighted graph')
        else:
            for edge in self.el:
                if edge.source == source and edge.dest == dest:
                    return
                elif edge.source == dest and edge.dest == source:
                    return
                else:
                    continue
            self.el.append(Edge(source, dest, weight))
        
    def delete_edge(self,source,dest):
        """
        Delete an edge between two veritces of a graph represented as an 
        adjacency list. This function handles cases where an edge might not
        exist because the vertices are out of bounds.
        """
        if source >= self.vertices or dest>=self.vertices or source <0 or dest<0:
            print('Error, vertex number out of range')
        else:
            for i in range(len(self.el)):
                if self.el[i].source == source and self.el[i].dest == dest:
                    self.el.pop(i)
                    return
                
    def display(self):
        """
        Print the edge list representation of the graph to the terminal by
        traversing through it.
        """
        print('[',end='')
        for i in range(len(self.el)):
            source = self.el[i].source
            dest = self.el[i].dest
            weight = self.el[i].weight
            print('('+str(source)+','+str(dest)+','+str(weight)+')',end='')
        print(']')
     
    def draw(self):
        """
        Convert the edge list representation of a graph to an adjacency
        list and call the draw() function from the adjacency list class to 
        show the actual vertices and edges of the graph.
        """
        AL = self.as_AL()
        AL.draw()
            
    def as_EL(self):
        """
        Return the edge list representation of the graph.
        """
        return self
    
    def as_AM(self):
        """
        Convert an edge list representation of a graph to an adjacency
        matrix by traversing through the original representation and calling
        the insert_edge() function from the adjacency matrix class for each
        Edge object in the edge list.
        """
        AM = am_graph.Graph(self.vertices, weighted=self.weighted, directed=self.directed)
        for i in range(len(self.el)):
            source = self.el[i].source
            dest = self.el[i].dest
            weight = self.el[i].weight
            AM.insert_edge(source, dest, weight)
        return AM
    
    def as_AL(self):
        """
        Convert an edge list representation of a graph to an adjacency
        list by traversing through the original representation and calling
        the insert_edge() function from the adjacency list class for each
        Edge object in the edge list.
        """
        AL = al_graph.Graph(self.vertices, weighted=self.weighted, directed=self.directed)
        for i in range(len(self.el)):
            source = self.el[i].source
            dest = self.el[i].dest
            weight = self.el[i].weight
            AL.insert_edge(source, dest, weight)
        return AL
    
    def BFS_EL(self):
        """
        Traverse through the graph by breadth-first search and use the 
        properties of the edge list representation to access the vertices
        adjacent to the current vertex. Return a list of integers as the path
        traversed by breadth-first search.
        """
        Q = []
        known = [False for i in range(self.vertices)]
        path = [-1 for i in range(self.vertices)]
        
        # Push the start vertex (0) to the queue.
        Q.append(0)
        # Add the start vertex to the "known" list of visited vertices.
        known[0] = True
        
        while len(Q) > 0:
            # Pop a vertex from the queue.
            currV = Q.pop(0)
            # Visit the current vertex to check for its adjacent vertices.
            for adjV in self.el:
                if adjV.source == currV:
                    if known[adjV.dest] == False:
                        # Push the adjacent vertex to the queue.
                        Q.append(adjV.dest)
                        # Add the adjacent vertex to the "known" list of 
                        # visited vertices.
                        known[adjV.dest] = True
                        # Add the adjacent vertex to the path.
                        path[adjV.dest] = currV
                if adjV.dest == currV:
                    if known[adjV.source] == False:
                        # Push the adjacent vertex to the queue.
                        Q.append(adjV.source)
                        # Add the adjacent vertex to the "known" list of 
                        # visited vertices.
                        known[adjV.source] = True
                        # Add the adjacent vertex to the path.
                        path[adjV.source] = currV
        return path
        
    def DFS_EL(self):
        """
        Traverse through the graph by depth-first search and use the 
        properties of the edge list representation to access the vertices
        adjacent to the current vertex. Return a list of integers as the path
        traversed by depth-first search.
        """
        S = []
        known = [False for i in range(self.vertices)]
        path = [-1 for i in range(self.vertices)]
        
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
                for adjV in self.el:
                    if adjV.source == currV:
                        # Push the adjacent vertex to the stack.
                        S.append(adjV.dest)
                        if known[adjV.dest] == False:
                            # Add the adjacent vertex to the path.
                            path[adjV.dest] = currV
                    if adjV.dest == currV:
                        # Push the adjacent vertex to the stack.
                        S.append(adjV.source)
                        if known[adjV.source] == False:
                            # Add the adjacent vertex to the path.
                            path[adjV.source] = currV
        return path