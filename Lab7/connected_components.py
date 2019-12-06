# Course: CS 2302 Data Structures
# Author: Alonso Monarrez (original source code provided by Olac Fuentes)
# Assignment: Lab 7 Algorithm Design Techniques
# Instructor: Olac Fuentes
# TA: Anindita Nath
# Date of last modification: December 6
# Purpose: The purpose of this program is to implement a single function that
# finds and returns the number of connected components of a graph represented
# as an adjacency list.
import DSF as dsf

def connected_components(g):
    """
    Build a disjoint set forest of a graph represented as an adjacency list
    and return the number of connected components the graph has.
    """
    vertices = len(g.al)
    components = vertices
    s = dsf.DSF(vertices)
    for v in range(vertices):
        for edge in g.al[v]:
            components -= s.union(v,edge.dest)
    return components