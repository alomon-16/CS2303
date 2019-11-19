# Course: CS 2302 Data Structures
# Author: Alonso Monarrez (original source code provided by Olac Fuentes)
# Assignment: Lab 6 Graphs
# Instructor: Olac Fuentes
# TA: Anindita Nath
# Date of last modification: November 18
# Purpose: The purpose of this program is to test the functions implemented in
# the three graph classes (graph_AL, graph_AM, and graph_EL) and compare their
# performance by testing their insert_edge, display, and delete_edge functions.
import matplotlib.pyplot as plt
import numpy as np
import graph_AL as graph
#import graph_AM as graph
#import graph_EL as graph
import time

if __name__ == "__main__":   
    plt.close("all")
    start_time = time.time_ns()
    g = graph.Graph(6)
    g.insert_edge(0,1)
    g.insert_edge(0,2)
    g.insert_edge(1,2)
    g.insert_edge(2,3)
    g.insert_edge(3,4)
    g.insert_edge(4,1)
    end_time = time.time_ns()
    total_time = end_time - start_time
    print("Running time to build unweighted, undirected graph: " + str(total_time) +
          " nanoseconds.\n")
    start_time = time.time_ns()
    g.display()
    end_time = time.time_ns()
    total_time = end_time - start_time
    print("Running time to display unweighted, undirected graph: " + str(total_time) +
          " nanoseconds.\n")
    g.draw()
    start_time = time.time_ns()
    g.delete_edge(1,2)
    end_time = time.time_ns()
    total_time = end_time - start_time
    g.display()
    print("Running time to delete edge from unweighted, undirected graph: " +
          str(total_time) + " nanoseconds.\n")
    g.draw()
    
    start_time = time.time_ns()
    g = graph.Graph(12)
    g.insert_edge(0,1)
    g.insert_edge(0,2)
    g.insert_edge(1,2)
    g.insert_edge(2,3)
    g.insert_edge(3,4)
    g.insert_edge(4,1)
    g.insert_edge(5,1)
    g.insert_edge(5,2)
    g.insert_edge(6,2)
    g.insert_edge(7,3)
    g.insert_edge(8,4)
    g.insert_edge(10,1)
    end_time = time.time_ns()
    total_time = end_time - start_time
    print("Running time to build unweighted, undirected graph: " + str(total_time) +
          " nanoseconds.\n")
    start_time = time.time_ns()
    g.display()
    end_time = time.time_ns()
    total_time = end_time - start_time
    print("Running time to display unweighted, undirected graph: " + str(total_time) +
          " nanoseconds.\n")
    g.draw()
    start_time = time.time_ns()
    g.delete_edge(1,2)
    end_time = time.time_ns()
    total_time = end_time - start_time
    g.display()
    print("Running time to delete edge from unweighted, undirected graph: " +
          str(total_time) + " nanoseconds.\n")
    g.draw()
    
    start_time = time.time_ns()
    g = graph.Graph(18)
    g.insert_edge(0,1)
    g.insert_edge(0,2)
    g.insert_edge(1,2)
    g.insert_edge(2,3)
    g.insert_edge(3,4)
    g.insert_edge(4,1)
    g.insert_edge(5,1)
    g.insert_edge(5,2)
    g.insert_edge(6,2)
    g.insert_edge(7,3)
    g.insert_edge(8,4)
    g.insert_edge(10,1)
    g.insert_edge(11,5)
    g.insert_edge(12,5)
    g.insert_edge(13,7)
    g.insert_edge(14,8)
    g.insert_edge(16,10)
    g.insert_edge(16,12)
    end_time = time.time_ns()
    total_time = end_time - start_time
    print("Running time to build unweighted, undirected graph: " + str(total_time) +
          " nanoseconds.\n")
    start_time = time.time_ns()
    g.display()
    end_time = time.time_ns()
    total_time = end_time - start_time
    print("Running time to display unweighted, undirected graph: " + str(total_time) +
          " nanoseconds.\n")
    g.draw()
    start_time = time.time_ns()
    g.delete_edge(1,2)
    end_time = time.time_ns()
    total_time = end_time - start_time
    g.display()
    print("Running time to delete edge from unweighted, undirected graph: " +
          str(total_time) + " nanoseconds.\n")
    g.draw()
    
    start_time = time.time_ns()
    g = graph.Graph(6,directed = True)
    g.insert_edge(0,1)
    g.insert_edge(0,2)
    g.insert_edge(1,2)
    g.insert_edge(2,3)
    g.insert_edge(3,4)
    g.insert_edge(4,1)
    end_time = time.time_ns()
    total_time = end_time - start_time
    print("Running time to build unweighted, directed graph: " + str(total_time) +
          " nanoseconds.\n")
    start_time = time.time_ns()
    g.display()
    end_time = time.time_ns()
    total_time = end_time - start_time
    print("Running time to display unweighted, directed graph: " + str(total_time) +
          " nanoseconds.\n")
    g.draw()
    start_time = time.time_ns()
    g.delete_edge(1,2)
    end_time = time.time_ns()
    total_time = end_time - start_time
    g.display()
    print("Running time to delete edge from unweighted, directed graph: " +
          str(total_time) + " nanoseconds.\n")
    g.draw()
    
    start_time = time.time_ns()
    g = graph.Graph(12,directed = True)
    g.insert_edge(0,1)
    g.insert_edge(0,2)
    g.insert_edge(1,2)
    g.insert_edge(2,3)
    g.insert_edge(3,4)
    g.insert_edge(4,1)
    g.insert_edge(5,1)
    g.insert_edge(5,2)
    g.insert_edge(6,2)
    g.insert_edge(7,3)
    g.insert_edge(8,4)
    g.insert_edge(10,1)
    end_time = time.time_ns()
    total_time = end_time - start_time
    print("Running time to build unweighted, directed graph: " + str(total_time) +
          " nanoseconds.\n")
    start_time = time.time_ns()
    g.display()
    end_time = time.time_ns()
    total_time = end_time - start_time
    print("Running time to display unweighted, directed graph: " + str(total_time) +
          " nanoseconds.\n")
    g.draw()
    start_time = time.time_ns()
    g.delete_edge(1,2)
    end_time = time.time_ns()
    total_time = end_time - start_time
    g.display()
    print("Running time to delete edge from unweighted, directed graph: " +
          str(total_time) + " nanoseconds.\n")
    g.draw()
    
    start_time = time.time_ns()
    g = graph.Graph(18,directed = True)
    g.insert_edge(0,1)
    g.insert_edge(0,2)
    g.insert_edge(1,2)
    g.insert_edge(2,3)
    g.insert_edge(3,4)
    g.insert_edge(4,1)
    g.insert_edge(5,1)
    g.insert_edge(5,2)
    g.insert_edge(6,2)
    g.insert_edge(7,3)
    g.insert_edge(8,4)
    g.insert_edge(10,1)
    g.insert_edge(11,5)
    g.insert_edge(12,5)
    g.insert_edge(13,7)
    g.insert_edge(14,8)
    g.insert_edge(16,10)
    g.insert_edge(16,12)
    end_time = time.time_ns()
    total_time = end_time - start_time
    print("Running time to build unweighted, directed graph: " + str(total_time) +
          " nanoseconds.\n")
    start_time = time.time_ns()
    g.display()
    end_time = time.time_ns()
    total_time = end_time - start_time
    print("Running time to display unweighted, directed graph: " + str(total_time) +
          " nanoseconds.\n")
    g.draw()
    start_time = time.time_ns()
    g.delete_edge(1,2)
    end_time = time.time_ns()
    total_time = end_time - start_time
    g.display()
    print("Running time to delete edge from unweighted, directed graph: " +
          str(total_time) + " nanoseconds.\n")
    g.draw()
    
    start_time = time.time_ns()
    g = graph.Graph(6,weighted=True)
    g.insert_edge(0,1,4)
    g.insert_edge(0,2,3)
    g.insert_edge(1,2,2)
    g.insert_edge(2,3,1)
    g.insert_edge(3,4,5)
    g.insert_edge(4,1,4)
    end_time = time.time_ns()
    total_time = end_time - start_time
    print("Running time to build weighted, undirected graph: " + str(total_time) +
          " nanoseconds.\n")
    start_time = time.time_ns()
    g.display()
    end_time = time.time_ns()
    total_time = end_time - start_time
    print("Running time to display weighted, undirected graph: " + str(total_time) +
          " nanoseconds.\n")
    g.draw()
    start_time = time.time_ns()
    g.delete_edge(1,2)
    end_time = time.time_ns()
    total_time = end_time - start_time
    g.display()
    print("Running time to delete edge from weighted, undirected graph: " +
          str(total_time) + " nanoseconds.\n")
    g.draw()
    
    start_time = time.time_ns()
    g = graph.Graph(12,weighted=True)
    g.insert_edge(0,1,4)
    g.insert_edge(0,2,3)
    g.insert_edge(1,2,2)
    g.insert_edge(2,3,1)
    g.insert_edge(3,4,5)
    g.insert_edge(4,1,4)
    g.insert_edge(5,1,5)
    g.insert_edge(5,2,6)
    g.insert_edge(6,2,4)
    g.insert_edge(7,3,8)
    g.insert_edge(8,4,9)
    g.insert_edge(10,1,7)
    end_time = time.time_ns()
    total_time = end_time - start_time
    print("Running time to build weighted, undirected graph: " + str(total_time) +
          " nanoseconds.\n")
    start_time = time.time_ns()
    g.display()
    end_time = time.time_ns()
    total_time = end_time - start_time
    print("Running time to display weighted, undirected graph: " + str(total_time) +
          " nanoseconds.\n")
    g.draw()
    start_time = time.time_ns()
    g.delete_edge(1,2)
    end_time = time.time_ns()
    total_time = end_time - start_time
    g.display()
    print("Running time to delete edge from weighted, undirected graph: " +
          str(total_time) + " nanoseconds.\n")
    g.draw()
    
    start_time = time.time_ns()
    g = graph.Graph(18,weighted=True)
    g.insert_edge(0,1,4)
    g.insert_edge(0,2,3)
    g.insert_edge(1,2,2)
    g.insert_edge(2,3,1)
    g.insert_edge(3,4,5)
    g.insert_edge(4,1,4)
    g.insert_edge(5,1,5)
    g.insert_edge(5,2,6)
    g.insert_edge(6,2,4)
    g.insert_edge(7,3,8)
    g.insert_edge(8,4,9)
    g.insert_edge(10,1,7)
    g.insert_edge(11,5,9)
    g.insert_edge(12,5,10)
    g.insert_edge(13,7,4)
    g.insert_edge(14,8,5)
    g.insert_edge(16,10,6)
    g.insert_edge(16,12,15)
    end_time = time.time_ns()
    total_time = end_time - start_time
    print("Running time to build weighted, undirected graph: " + str(total_time) +
          " nanoseconds.\n")
    start_time = time.time_ns()
    g.display()
    end_time = time.time_ns()
    total_time = end_time - start_time
    print("Running time to display weighted, undirected graph: " + str(total_time) +
          " nanoseconds.\n")
    g.draw()
    start_time = time.time_ns()
    g.delete_edge(1,2)
    end_time = time.time_ns()
    total_time = end_time - start_time
    g.display()
    print("Running time to delete edge from weighted, undirected graph: " +
          str(total_time) + " nanoseconds.\n")
    g.draw()
    
    start_time = time.time_ns()
    g = graph.Graph(6,weighted=True,directed = True)
    g.insert_edge(0,1,4)
    g.insert_edge(0,2,3)
    g.insert_edge(1,2,2)
    g.insert_edge(2,3,1)
    g.insert_edge(3,4,5)
    g.insert_edge(4,1,4)
    end_time = time.time_ns()
    total_time = end_time - start_time
    print("Running time to build weighted, directed graph: " + str(total_time) +
          " nanoseconds.\n")
    start_time = time.time_ns()
    g.display()
    end_time = time.time_ns()
    total_time = end_time - start_time
    print("Running time to display weighted, directed graph: " + str(total_time) +
          " nanoseconds.\n")
    g.draw()
    start_time = time.time_ns()
    g.delete_edge(1,2)
    end_time = time.time_ns()
    total_time = end_time - start_time
    g.display()
    print("Running time to delete edge from weighted, directed graph: " +
          str(total_time) + " nanoseconds.\n")
    g.draw()
    
    start_time = time.time_ns()
    g = graph.Graph(12,weighted=True,directed = True)
    g.insert_edge(0,1,4)
    g.insert_edge(0,2,3)
    g.insert_edge(1,2,2)
    g.insert_edge(2,3,1)
    g.insert_edge(3,4,5)
    g.insert_edge(4,1,4)
    g.insert_edge(5,1,5)
    g.insert_edge(5,2,6)
    g.insert_edge(6,2,4)
    g.insert_edge(7,3,8)
    g.insert_edge(8,4,9)
    g.insert_edge(10,1,7)
    end_time = time.time_ns()
    total_time = end_time - start_time
    print("Running time to build weighted, directed graph: " + str(total_time) +
          " nanoseconds.\n")
    start_time = time.time_ns()
    g.display()
    end_time = time.time_ns()
    total_time = end_time - start_time
    print("Running time to display weighted, directed graph: " + str(total_time) +
          " nanoseconds.\n")
    g.draw()
    start_time = time.time_ns()
    g.delete_edge(1,2)
    end_time = time.time_ns()
    total_time = end_time - start_time
    g.display()
    print("Running time to delete edge from weighted, directed graph: " +
          str(total_time) + " nanoseconds.\n")
    g.draw()
    
    start_time = time.time_ns()
    g = graph.Graph(18,weighted=True,directed = True)
    g.insert_edge(0,1,4)
    g.insert_edge(0,2,3)
    g.insert_edge(1,2,2)
    g.insert_edge(2,3,1)
    g.insert_edge(3,4,5)
    g.insert_edge(4,1,4)
    g.insert_edge(5,1,5)
    g.insert_edge(5,2,6)
    g.insert_edge(6,2,4)
    g.insert_edge(7,3,8)
    g.insert_edge(8,4,9)
    g.insert_edge(10,1,7)
    g.insert_edge(11,5,9)
    g.insert_edge(12,5,10)
    g.insert_edge(13,7,4)
    g.insert_edge(14,8,5)
    g.insert_edge(16,10,6)
    g.insert_edge(16,12,15)
    end_time = time.time_ns()
    total_time = end_time - start_time
    print("Running time to build weighted, directed graph: " + str(total_time) +
          " nanoseconds.\n")
    start_time = time.time_ns()
    g.display()
    end_time = time.time_ns()
    total_time = end_time - start_time
    print("Running time to display weighted, directed graph: " + str(total_time) +
          " nanoseconds.\n")
    g.draw()
    start_time = time.time_ns()
    g.delete_edge(1,2)
    end_time = time.time_ns()
    total_time = end_time - start_time
    g.display()
    print("Running time to delete edge from weighted, directed graph: " +
          str(total_time) + " nanoseconds.\n")
    g.draw()