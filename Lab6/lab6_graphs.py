# Course: CS 2302 Data Structures
# Author: Alonso Monarrez
# Assignment: Lab 6 Graphs
# Instructor: Olac Fuentes
# TA: Anindita Nath
# Date of last modification: November 18
# Purpose: The purpose of this program is to implement a solution to the fox,
# chicken, and grain riddle using a graph (the graph will be undirected and
# unweighted). The graph will be represented as an adjacency list, an adjacency
# matrix, or an edge list, and the solution to the riddle will be represented
# as a path found by breadth-first search and depth-first search.
import matplotlib.pyplot as plt
import graph_AL as graph
#import graph_AM as graph
#import graph_EL as graph
import time

plt.close("all")  
def printPath(path, dest):
    """
    Recursively traverse through a path and return a list containing the
    vertices that are visited in order to reach the destination vertex.
    """
    if path[dest] != -1:
        return printPath(path, path[dest]) + [dest]
    return [dest]

def pathToGraph(vertices, path):
    """
    Traverse through a path found either by breadth-first search or by
    depth-first search and insert an edge between two adjacent vertices in the
    path into the graph.
    """
    G = graph.Graph(len(vertices))
    for i in range(len(path)-1):
        source = path[i]
        dest = path[i+1]
        G.insert_edge(source, dest)
    return G

start_time = time.time_ns()
g = graph.Graph(16)
g.insert_edge(0,5)
g.insert_edge(2,7)
g.insert_edge(2,11)
g.insert_edge(4,5)
g.insert_edge(4,7)
g.insert_edge(4,13)
g.insert_edge(8,11)
g.insert_edge(8,13)
g.insert_edge(10,11)
g.insert_edge(10,15)
end_time = time.time_ns()
total_time = end_time - start_time

g.display()

print("Total time to build graph: " + str(total_time) + " nanoseconds.\n")

g.draw()

if g.representation == 'AL':
    start_time = time.time_ns()
    BFS_path = g.BFS_AL()
    end_time = time.time_ns()
    total_time = end_time - start_time
    path = printPath(BFS_path, 15)
    print("Solution 1 (path found by breadth-first search): " + str(path))
    g1 = pathToGraph(BFS_path, path)
    g1.display()
    g1.draw()
    print("Total time to build path by breadth-first search: " + str(total_time) +
          " nanoseconds.\n")
    start_time = time.time_ns()
    DFS_path = g.DFS_AL()
    end_time = time.time_ns()
    total_time = end_time - start_time
    path = printPath(DFS_path, 15)
    print("Solution 2 (path found by depth-first search): " + str(path))
    g2 = pathToGraph(DFS_path, path)
    g2.display()
    g2.draw()
    print("Total time to build path by depth-first search: " + str(total_time) +
          " nanoseconds.")
elif g.representation == 'AM':
    start_time = time.time_ns()
    BFS_path = g.BFS_AM()
    end_time = time.time_ns()
    total_time = end_time - start_time
    path = printPath(BFS_path, 15)
    print("Solution 1 (path found by breadth-first search): " + str(path))
    g1 = pathToGraph(BFS_path, path)
    g1.display()
    g1.draw()
    print("Total time to build path by breadth-first search: " + str(total_time) +
          " nanoseconds.\n")
    start_time = time.time_ns()
    DFS_path = g.DFS_AM()
    end_time = time.time_ns()
    total_time = end_time - start_time
    path = printPath(DFS_path, 15)
    print("Solution 2 (path found by depth-first search): " + str(path))
    g2 = pathToGraph(DFS_path, path)
    g2.display()
    g2.draw()
    print("Total time to build path by depth-first search: " + str(total_time) +
          " nanoseconds.")
elif g.representation == 'EL':
    start_time = time.time_ns()
    BFS_path = g.BFS_EL()
    end_time = time.time_ns()
    total_time = end_time - start_time
    path = printPath(BFS_path, 15)
    print("Solution 1 (path found by breadth-first search): " + str(path))
    g1 = pathToGraph(BFS_path, path)
    g1.display()
    g1.draw()
    print("Total time to build path by breadth-first search: " + str(total_time) +
          " nanoseconds.\n")
    start_time = time.time_ns()
    DFS_path = g.DFS_EL()
    end_time = time.time_ns()
    total_time = end_time - start_time
    path = printPath(DFS_path, 15)
    print("Solution 2 (path found by depth-first search): " + str(path))
    g2 = pathToGraph(DFS_path, path)
    g2.display()
    g2.draw()
    print("Total time to build path by depth-first search: " + str(total_time) +
          " nanoseconds.")