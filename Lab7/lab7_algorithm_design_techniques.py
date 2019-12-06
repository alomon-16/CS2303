# Course: CS 2302 Data Structures
# Author: Alonso Monarrez
# Assignment: Lab 7 Algorithm Design Techniques
# Instructor: Olac Fuentes
# TA: Anindita Nath
# Date of last modification: December 6
# Purpose: The purpose of this program is to implement functions that use
# algorithm design techniques to solve two different types of problems. The
# first problem (finding a Hamiltonian cycle) is solved via randomization and
# backtracking, and the second problem (finding the edit distance from one
# word to another word using two different variations of the edit distance
# function) is solved via dynamic programming.
import graph_AL as graph
import connected_components as cc
import matplotlib.pyplot as plt
import random as rand
import numpy as np
import time

def randomized_hamiltonian(V,E):
    """
    Find a Hamiltonian cycle in a graph represented as an adjacency list by
    returning a randomly generated subset of E (the set of edges in the graph)
    of size V (the number of vertices in the graph) that forms a Hamiltonian
    cycle. If none of the randomly generated subsets formed a Hamiltonian 
    cycle, return None.
    """
    for i in range(1000):
        # For each try, generate a random subset Eh of E of size V.
        rand_val = []
        Eh = []
        j = 0
        while j < len(V):
            k = rand.randint(0, len(E)-1)
            if not k in rand_val:
                Eh.append(E[k])
                rand_val.append(k)
                j += 1
        # Build the graph g = (V,Eh) that will be used to determine if Eh forms
        # a Hamiltonian cycle.
        g = graph.Graph(len(Eh))
        for m in range(len(Eh)):
            source = Eh[m][0]
            dest = Eh[m][1]
            g.insert_edge(source, dest)
        # Determine if the graph g = (V,Eh) has 1 connected component. If it
        # has 1 connected component move on to determine if every vertex V has
        # an in-degree of 2. Otherwise, move on to the next subset of edges.
        if cc.connected_components(g) == 1:
            # Determine if the in-degree of every vertex V is 2. If every
            # vertex has an in-degree of 2, return the subset of edges Eh that
            # forms a Hamiltonian cycle.
            in_degrees_set = set(g.in_degrees())
            if len(in_degrees_set) == 1 and next(iter(in_degrees_set)) == 2:
                return Eh
    # After all tries have run out, return None to indicate that no
    # Hamiltonian cycle was found.
    return None

def backtracking_hamiltonian(V,E,Eh):
    """
    Find a Hamiltonian cycle in a graph represented as an adjacency list by
    returning a subset of E (the set of edges in the graph) of size V (the
    number of vertices in the graph) that forms a Hamiltonian cycle. The subset
    of edges that forms a Hamiltonian cycle, if there is one, will be selected
    from all possible 2^|E| subsets. If none of the subsets form a Hamiltonian
    cycle, return None.
    """
    # Base case 1: The subset of edges Eh is of size V and it forms a
    # Hamiltonian cycle.
    if len(Eh) == len(V) and isHamiltonian(len(V),Eh):
        return []
    # Base case 2: The subset of edges Eh exceeds its size V or there are no
    # more edges to choose from E.
    if len(Eh) > len(V) or len(E) == 0:
        return None
    # Take the first edge from E.
    subset = backtracking_hamiltonian(V,E[1:],Eh + [E[0]])
    if subset is not None:
        return [E[0]] + subset
    # Do not take the first edge from E.
    return backtracking_hamiltonian(V,E[1:],Eh)

def isHamiltonian(V,Eh):
    """
    Determine whether a graph g = (V,Eh) has the necessary requirements to
    have a Hamiltonian cycle from the subset of edges Eh.
    """
    # Build the graph g = (V,Eh) that will be used to determine if Eh forms
    # a Hamiltonian cycle.
    g = graph.Graph(V)
    for m in range(len(Eh)):
        source = Eh[m][0]
        dest = Eh[m][1]
        g.insert_edge(source, dest)
    # Determine if the graph g = (V,Eh) has 1 connected component. If it
    # has 1 connected component move on to determine if every vertex V has
    # an in-degree of 2.
    if cc.connected_components(g) == 1:
        # Determine if the in-degree of every vertex V is 2. If every
        # vertex has an in-degree of 2, return True to indicate that the subset
        # of edges Eh forms a Hamiltonian cycle.
        in_degrees_set = set(g.in_degrees())
        if len(in_degrees_set) == 1 and next(iter(in_degrees_set)) == 2:
            return True
    # If the graph g = (V,Eh) fails either of the two requirements to have a
    # Hamiltonian cycle, return False.
    return False

def edit_distance(s1,s2):
    """
    Return the edit distance table and the value of the edit distance that
    represents the minimum number of character operations needed to convert s1
    to s2.
    """
    d = np.zeros((len(s1)+1,len(s2)+1),dtype=int)
    d[0,:] = np.arange(len(s2)+1)
    d[:,0] = np.arange(len(s1)+1)
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1] == s2[j-1]:
                d[i,j] = d[i-1,j-1]
            else:
                n = [d[i,j-1],d[i-1,j-1],d[i-1,j]]
                d[i,j] = min(n)+1      
    return d, d[-1,-1]
            
def modified_edit_distance(s1,s2):
    """
    Return the edit distance table and the value of the edit distance that
    represents the minimum number of character operations needed to convert s1
    to s2. Replacements are allowed only if the current characters being
    interchanged are both vowels or both consonants.
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    d = np.zeros((len(s1)+1, len(s2)+1), dtype=int)
    d[0,:] = np.arange(len(s2)+1)
    d[:,0] = np.arange(len(s1)+1)
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                d[i,j] = d[i-1,j-1]
            # If both characters are vowels, allow replacement of characters.
            elif s1[i-1] in vowels and s2[j-1] in vowels:
                n = [d[i,j-1],d[i-1,j-1],d[i-1,j]]
                d[i,j] = min(n) + 1
            # If both characters are consonants, allow replacement of
            # characters.
            elif not s1[i-1] in vowels and not s2[j-1] in vowels:
                n = [d[i,j-1],d[i-1,j-1],d[i-1,j]]
                d[i,j] = min(n) + 1
            # Otherwise, do not allow replacement of characters.
            else:
                n = [d[i,j-1],d[i-1,j]]
                d[i,j] = min(n) + 1      
    return d, d[-1,-1]

def generate_graph(vertices):
    """
    Generate and return a complete graph represented as an adjacency list, in
    which every vertex V is connected to every other vertex.
    """
    g = graph.Graph(vertices)
    for source in range(vertices):
        for dest in range(vertices):
            if source != dest:
                g.insert_edge(source,dest)
    return g

def generate_vertex_and_edge_sets(G):
    """
    Generate and return the vertex and edge sets of a graph represented as an
    adjacency list. These sets are used to determine if there is a Hamiltonian
    cycle in the graph.
    """
    vertex_set = []
    edge_set = []
    for vertex in range(len(G.al)):
        # Append each vertex V to the set of vertices of the graph.
        vertex_set.append(vertex)
        for edge in G.al[vertex]:
            if vertex < edge.dest:
                new_edge = [vertex,edge.dest,edge.weight]
                if not new_edge in edge_set:
                    # Append each unique edge E to the set of edges of the
                    # graph.
                    edge_set.append([vertex,edge.dest,edge.weight])
    return vertex_set, edge_set

if __name__ == "__main__":
    plt.close("all")
    print('RANDOMIZATION AND BACKTRACKING IMPLEMENTATIONS TO FIND A ' +
          'HAMILTONIAN CYCLE IN A GRAPH')
    num_vertices = int(input('Enter a value for the number of vertices in the graph: '))
    g = generate_graph(num_vertices)
    # Show the graph containing all its vertices and all its possible edges.
    g.draw()
    
    vertices, edges = generate_vertex_and_edge_sets(g)
    print('\nSet of vertices: ' + str(vertices))
    print('Set of edges: ' + str(edges))
                
    print()
    start_time = time.time_ns()
    hamiltonian_cycle = randomized_hamiltonian(vertices, edges)
    end_time = time.time_ns()
    total_time = end_time - start_time
    if hamiltonian_cycle != None:
        print('A Hamiltonian cycle was found via randomization: ' +
              str(hamiltonian_cycle))
        g1 = graph.Graph(len(hamiltonian_cycle))
        for i in range(len(hamiltonian_cycle)):
            g1.insert_edge(hamiltonian_cycle[i][0], hamiltonian_cycle[i][1])
        # Show the graph containing the Hamiltonian cycle found via
        # randomization.
        g1.draw()
    else:
        print('No Hamiltonian cycle was found via randomization.')
    print('Running time to implement a Hamiltonian cycle via randomization: ' +
          str(total_time) + ' nanoseconds.')
 
    print()
    start_time = time.time_ns()
    hamiltonian_cycle = backtracking_hamiltonian(vertices, edges, [])
    end_time = time.time_ns()
    total_time = end_time - start_time
    if hamiltonian_cycle != None:
        print('A Hamiltonian cycle was found via backtracking: ' +
              str(hamiltonian_cycle))
        g2 = graph.Graph(len(hamiltonian_cycle))
        for i in range(len(hamiltonian_cycle)):
            g2.insert_edge(hamiltonian_cycle[i][0], hamiltonian_cycle[i][1])
        # Show the graph containing the Hamiltonian cycle found via
        # backtracking.
        g2.draw()
    else:
        print('No Hamiltonian cycle was found via backtracking.')
    print('Running time to implement a Hamiltonian cycle via backtracking: ' +
          str(total_time) + ' nanoseconds.')

    print('\nDYNAMIC PROGRAMMING IMPLEMENTATION TO FIND THE EDIT DISTANCE ' +
          'FROM ONE WORD TO ANOTHER WORD USING TWO DIFFERENT VARIATIONS OF ' +
          'THE EDIT DISTANCE FUNCTION')
    print()
    print('Enter two words')
    s1 = input('Word 1: ')
    s2 = input('Word 2: ')
    print()
    table_1, dist_1 = edit_distance(s1, s2)
    end_time = time.time_ns()
    total_time = end_time - start_time
    print(table_1)
    print('\nEdit distance from ' + s1 + ' to ' + s2 + ' = ' + str(dist_1))
    print('Running time to implement the edit distance of two words ' +
          '(original variation) via dynamic programming: ' + str(total_time) +
          ' nanoseconds.')
    print()
    start_time = time.time_ns()    
    table_2, dist_2 = modified_edit_distance(s1, s2)
    end_time = time.time_ns()
    total_time = end_time - start_time
    print(table_2)
    print('\nEdit distance from ' + s1 + ' to ' + s2 + ' = ' + str(dist_2))
    print('Running time to implement the edit distance of two words ' +
          '(modified variation) via dynamic programming: ' + str(total_time) +
          ' nanoseconds.')