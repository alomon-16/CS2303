# Course: CS 2302 Data Structures
# Author: Alonso Monarrez (original source code provided by Olac Fuentes)
# Assignment: Lab 6 Graphs
# Instructor: Olac Fuentes
# TA: Anindita Nath
# Date of last modification: November 18
# Purpose: The purpose of this program is to implement functions that can be
# used for a graph represented as an adjacency list.
import numpy as np
import matplotlib.pyplot as plt
import math
import graph_AM as am_graph
import graph_EL as el_graph
from scipy.interpolate import interp1d

class Edge:
    # Constructor
    def __init__(self, dest, weight=1):
        self.dest = dest
        self.weight = weight
        
class Graph:
    # Constructor
    def __init__(self, vertices, weighted=False, directed = False):
        self.al = [[] for i in range(vertices)]
        self.weighted = weighted
        self.directed = directed
        self.representation = 'AL'
        
    def insert_edge(self,source,dest,weight=1):
        """
        Insert an edge between two vertices of a graph represented as an
        adjacency list. This function handles graphs of different combinations
        between direction and weight properties.
        """
        if source >= len(self.al) or dest>=len(self.al) or source <0 or dest<0:
            print('Error, vertex number out of range')
        if weight!=1 and not self.weighted:
            print('Error, inserting weighted edge to unweighted graph')
        else:
            self.al[source].append(Edge(dest,weight)) 
            if not self.directed:
                self.al[dest].append(Edge(source,weight))
                
    def delete_edge_(self,source,dest):
        """
        Helper function used to find and delete an edge between two vertices
        of a graph represented as an adjacency list.
        """
        i = 0
        for edge in self.al[source]:
            if edge.dest == dest:
                self.al[source].pop(i)
                return True
            i+=1    
        return False
    
    def delete_edge(self,source,dest):
        """
        Delete an edge between two veritces of a graph represented as an 
        adjacency list. This function handles graphs of different combinations
        between direction and weight properties.
        """
        if source >= len(self.al) or dest>=len(self.al) or source <0 or dest<0:
            print('Error, vertex number out of range')
        else:
            deleted = self.delete_edge_(source,dest)
            if not self.directed:
                deleted = self.delete_edge_(dest,source)
        if not deleted:        
            print('Error, edge to delete not found')
                
    def display(self):
        """
        Print the adjacency list representation of the graph to the terminal
        by traversing through it.
        """
        print('[',end='')
        for i in range(len(self.al)):
            print('[',end='')
            for edge in self.al[i]:
                print('('+str(edge.dest)+','+str(edge.weight)+')',end='')
            print(']',end=' ')    
        print(']')
                
    def draw(self):
        """
        Show the actual vertices and edges of the graph, along with its
        directed edges and/or edge weights, if applicable.
        """
        scale = 30
        fig, ax = plt.subplots()
        for i in range(len(self.al)):
            for edge in self.al[i]:
                d,w = edge.dest, edge.weight
                if self.directed or d>i:
                    x = np.linspace(i*scale,d*scale)
                    x0 = np.linspace(i*scale,d*scale,num=5)
                    diff = np.abs(d-i)
                    if diff == 1:
                        y0 = [0,0,0,0,0]
                    else:
                        y0 = [0,-6*diff,-8*diff,-6*diff,0]
                    f = interp1d(x0, y0, kind='cubic')
                    y = f(x)
                    s = np.sign(i-d)
                    #if part of path 
                    ax.plot(x,s*y,linewidth=1,color='k')
                    #else 
                    if self.directed:
                        xd = [x0[2]+2*s,x0[2],x0[2]+2*s]
                        yd = [y0[2]-1,y0[2],y0[2]+1]
                        yd = [y*s for y in yd]
                        ax.plot(xd,yd,linewidth=1,color='k')
                    if self.weighted:
                        xd = [x0[2]+2*s,x0[2],x0[2]+2*s]
                        yd = [y0[2]-1,y0[2],y0[2]+1]
                        yd = [y*s for y in yd]
                        ax.text(xd[2]-s*2,yd[2]+3*s, str(w), size=12,ha="center", va="center")
            ax.plot([i*scale,i*scale],[0,0],linewidth=1,color='k')        
            ax.text(i*scale,0, str(i), size=20,ha="center", va="center",
             bbox=dict(facecolor='w',boxstyle="circle"))
        ax.axis('off') 
        ax.set_aspect(1.0)
            
    def as_EL(self):
        """
        Convert an adjacency list representation of a graph to an edge list by
        traversing through the original representation and calling the
        insert_edge() function from the edge list class for each Edge object
        in the adjacency list.
        """
        EL = el_graph.Graph(len(self.al), weighted=self.weighted, directed=self.directed)
        for i in range(len(self.al)):
            for edge in self.al[i]:
                source = i
                dest = edge.dest
                weight = edge.weight
                EL.insert_edge(source, dest, weight)
        return EL
    
    def as_AM(self):
        """
        Convert an adjacency list representation of a graph to an adjacency
        matrix by traversing through the original representation and calling
        the insert_edge() function from the adjacency matrix class for each
        Edge object in the adjacency list.
        """
        AM = am_graph.Graph(len(self.al), weighted=self.weighted, directed=self.directed)
        for i in range(len(self.al)):
            for edge in self.al[i]:
                source = i
                dest = edge.dest
                weight = edge.weight
                AM.insert_edge(source, dest, weight)
        return AM
    
    def as_AL(self):
        """
        Return the adjacency list representation of the graph.
        """
        return self
    
    def BFS_AL(self):
        """
        Traverse through the graph by breadth-first search and use the 
        properties of the adjacency list representation to access the vertices
        adjacent to the current vertex. Return a list of integers as the path
        traversed by breadth-first search.
        """
        Q = []
        known = [False for i in range(len(self.al))]
        path = [-1 for i in range(len(self.al))]
        
        # Push the start vertex (0) to the queue.
        Q.append(0)
        # Add the start vertex to the "known" list of visited vertices.
        known[0] = True
        
        while len(Q) > 0:
            # Pop a vertex from the queue.
            currV = Q.pop(0)
            # Visit the current vertex to check for its adjacent vertices.
            for adjV in self.al[currV]:
                if known[adjV.dest] == False:
                    # Push the adjacent vertex to the queue.
                    Q.append(adjV.dest)
                    # Add the adjacent vertex to the "known" list of visited
                    # vertices.
                    known[adjV.dest] = True
                    # Add the adjacent vertex to the path.
                    path[adjV.dest] = currV
        return path
    
    def DFS_AL(self):
        """
        Traverse through the graph by depth-first search and use the 
        properties of the adjacency list representation to access the vertices
        adjacent to the current vertex. Return a list of integers as the path
        traversed by depth-first search.
        """
        S = []
        known = [False for i in range(len(self.al))]
        path = [-1 for i in range(len(self.al))]
        
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
                for adjV in self.al[currV]:
                    # Push the adjacent vertex to the stack.
                    S.append(adjV.dest)
                    if known[adjV.dest] == False:
                        # Add the adjacent vertex to the path.
                        path[adjV.dest] = currV
        return path