# Course: CS 2302 Data Structures
# Author: Alonso Monarrez
# Assignment: Lab 2 Algorithm Efficiency
# Instructor: Olac Fuentes
# TA: Anindita Nath
# Date of last modification: September 22
# Purpose: The purpose of this program is to locate the kth smallest element
# in a list by implementing five different sorting algorithms.
import random
import time

num_comparisons = 0

class quickSortStack(object):
    def __init__(self, L, first, last):
        self.L = L
        self.first = first
        self.last = last
        
def generate_list(start, end, n):
    """
    Generate a list of random integers of size n.
    The randomly generated integers will range from 1
    to n as decided by the user (e.g. if the user enters
    100, each integer will range from 1 to 100).
    Duplicates are allowed.
    """
    L = []
    for num in range(n):
        L.append(random.randint(start, end))
    return L

def bubble_sort(L):
    """
    Sort a list of integers L by swapping adjacent elements
    if they are in the wrong order.
    The list is considered sorted only if there is a whole
    pass without any swaps.
    """
    global num_comparisons
    isSorted = False
    while not isSorted:
        isSorted = True
        # Traverse through all the list elements except the last one.
        for i in range(len(L)-1):
            # Swap the current and next elements if they are in the
            # wrong order.
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                num_comparisons += 1
                isSorted = False
            else:
                num_comparisons += 1
    
def partition(L, first, last):
    """
    Set the pivot as the last element of the list and place
    it at its correct position in the sorted list.
    Place all elements smaller than the pivot to the left and
    all elements larger than the pivot to the right.
    Return the value for the index of the pivot.
    """
    global num_comparisons
    # Set the pivot as the last element of the list.
    pivot = L[last]
    # Set the index of the pivot as the index of the smaller
    # element.
    pivot_index = first - 1
    # Traverse through the list from the first element to the
    # second-to-last element of the list/sublist.
    for i in range(first, last):
        # If the current element is less than the pivot, increment
        # the index of the pivot and swap the element at the index
        # of the pivot with the current element.
        if L[i] < pivot:
            pivot_index += 1
            L[pivot_index], L[i] = L[i], L[pivot_index]
            num_comparisons += 1
        else:
            num_comparisons += 1
    # Swap the element next to the one at the index of the pivot
    # with the last element to place the pivot at its correct
    # position in the sorted list.
    L[pivot_index+1], L[last] = L[last], L[pivot_index+1]
    return pivot_index + 1
    
def quick_sort(L, first, last):
    """
    Partition the elements in a list of integers and recursively
    sort both the left and right sublists.
    """
    global num_comparisons
    if first < last:
        num_comparisons += 1
        # Partition the elements in the list/sublist.
        pivot_index = partition(L, first, last)
        # Call the function to sort the elements smaller than
        # the pivot.
        quick_sort(L, first, pivot_index-1)
        # Call the function to sort the elements greater than
        # the pivot.
        quick_sort(L, pivot_index+1, last)
    else:
        num_comparisons += 1
        
def modified_quick_sort(L, k, first, last):
    """
    Partition the elements in a list of integers and recursively
    sort the sublist where the kth element is found. 
    Continue sorting the corresponding sublist until the selected
    element becomes the pivot of the sublist.
    """
    global num_comparisons
    if first < last:
        num_comparisons += 1
        # Partition the elements in the list/sublist.
        pivot_index = partition(L, first, last)
        # If the value of k is equal to the index of the pivot,
        # the selected element has been found.
        if k == pivot_index:
            num_comparisons += 1
            return
        # Else, if the value of k is within the smaller sublist,
        # call the function to sort only the elements smaller than
        # the pivot.
        elif k < len(L[:pivot_index]):
            num_comparisons += 1
            modified_quick_sort(L, k, first, pivot_index-1)
        # Else, if the value of k is within the larger sublist,
        # call the function to sort only the elements greater than
        # the pivot.
        elif k >= (len(L) - len(L[pivot_index+1:])):
            num_comparisons += 1
            modified_quick_sort(L, k, pivot_index+1, last)
    else:
        num_comparisons += 1
        
def quick_sort_stack(L, first, last):
    """
    Implement a stack that stores the necessary information to
    sort a list of integers by quicksort.
    """
    global num_comparisons
    # Create a stack to store the initial list of integers and
    # the indices of the ends of the list.
    stack = [quickSortStack(L, first, last)]
    while len(stack) > 0:
        num_comparisons += 1
        # Pop the top of the stack to have access to the
        # list/sublist that will be sorted.
        h = stack.pop(-1)
        if h.first < h.last:
            num_comparisons += 1
            # Partition the elements in the list/sublist.
            pivot_index = partition(h.L, h.first, h.last)
            # Append to the stack the necessary information to
            # sort the smaller sublist by quicksort.
            stack.append(quickSortStack(h.L, h.first, pivot_index-1))
            # Append to the stack the necessary information to
            # sort the larger sublist by quicksort.
            stack.append(quickSortStack(h.L, pivot_index+1, h.last))
        else:
            num_comparisons += 1
    num_comparisons += 1
            
def modified_quick_sort_iterative(L, k, first, last):
    """
    Implement a while loop that sorts the sublist where the kth
    element is found.
    Continue sorting the corresponding sublist until the selected
    element becomes the pivot of the sublist.
    """
    global num_comparisons
    while first < last:
        num_comparisons += 1
        # Partition the elements in the list/sublist.
        pivot_index = partition(L, first, last)
        # If the value of k is equal to the index of the pivot,
        # the selected element has been found.
        if k == pivot_index:
            num_comparisons += 1
            return
        # Else, if the value of k is within the smaller sublist,
        # update the index of the last element of the smaller
        # sublist.
        elif k < len(L[:pivot_index]):
            num_comparisons += 1
            last = pivot_index-1
        # Else, if the value of k is within the larger sublist,
        # update the index of the first element of the larger
        # sublist.
        elif k >= (len(L) - len(L[pivot_index+1:])):
            num_comparisons += 1
            first = pivot_index+1
    num_comparisons += 1

# Part 1
            
def select_bubble(L,k):
    """
    Sort a list of integers L using bubble sort.
    Return the element in position k.
    """
    bubble_sort(L)
    return L[k]

def select_quick(L,k):
    """
    Sort a list of integers L using quicksort.
    Return the element in position k.
    """
    quick_sort(L, 0, len(L)-1)
    return L[k]

def select_modified_quick(L,k):
    """
    Sort a list of integers L using a modified version of quicksort.
    Return the element in position k.
    """
    modified_quick_sort(L, k, 0, len(L)-1)
    return L[k]

# Part 2

def select_quick_stack(L,k):
    """
    Sort a list of integers L using quicksort implemented as a stack.
    Return the element in position k.
    """
    quick_sort_stack(L, 0, len(L)-1)
    return L[k]
        
def select_modified_quick_iterative(L,k):
    """
    Sort a list of integers L using the modified version of quicksort
    implemented with a while loop.
    Return the element in position k.
    """
    modified_quick_sort_iterative(L, k, 0, len(L)-1)
    return L[k]

size = int(input("Enter a number to create a list of integers of that size: "))
k = int(input("Enter a number to find the kth smallest element in a list: "))
print()

if size >= 1 and (k >= 0 and k < size):
    L_1 = generate_list(1, size, size)
    L_2 = L_1.copy()
    L_3 = L_1.copy()
    L_4 = L_1.copy()
    L_5 = L_1.copy()
    
    print("BUBBLE SORT IMPLEMENTATION")
    print("Unsorted list: " + str(L_1))
    start = time.time()
    k_element = select_bubble(L_1, k)
    end = time.time()
    print("Number of comparisons: " + str(num_comparisons))
    print("Running time: " + str(round(end-start, 6)) + " seconds.")
    print("Sorted list: " + str(L_1))
    print("Smallest element at position " + str(k) + ": " + str(k))
    num_comparisons = 0
    print()
    
    print("QUICKSORT IMPLEMENTATION")
    print("Unsorted list: " + str(L_2))
    start = time.time()
    k_element = select_quick(L_2, k)
    end = time.time()
    print("Number of comparisons: " + str(num_comparisons))
    print("Running time: " + str(round(end-start, 6)) + " seconds.")
    print("Sorted list: " + str(L_2))
    print("Smallest element at position " + str(k) + ": " + str(k))
    num_comparisons = 0
    print()
    
    print("MODIFIED QUICKSORT IMPLEMENTATION")
    print("Unsorted list: " + str(L_3))
    start = time.time()
    k_element = select_modified_quick(L_3, k)
    end = time.time()
    print("Number of comparisons: " + str(num_comparisons))
    print("Running time: " + str(round(end-start, 6)) + " seconds.")
    print("Sorted list: " + str(L_3))
    print("Smallest element at position " + str(k) + ": " + str(k))
    num_comparisons = 0
    print()
    
    print("QUICKSORT IMPLEMENTATION WITH A STACK")
    print("Unsorted list: " + str(L_4))
    start = time.time()
    k_element = select_quick_stack(L_4, k)
    end = time.time()
    print("Number of comparisons: " + str(num_comparisons))
    print("Running time: " + str(round(end-start, 6)) + " seconds.")
    print("Sorted list: " + str(L_4))
    print("Smallest element at position " + str(k) + ": " + str(k))
    num_comparisons = 0
    print()
    
    print("MODIFIED QUICKSORT IMPLEMENTATION WITH A WHILE LOOP")
    print("Unsorted list: " + str(L_5))
    start = time.time()
    k_element = select_modified_quick_iterative(L_5, k)
    end = time.time()
    print("Number of comparisons: " + str(num_comparisons))
    print("Running time: " + str(round(end-start, 6)) + " seconds.")
    print("Sorted list: " + str(L_5))
    print("Smallest element at position " + str(k) + ": " + str(k))
else:
    print("ERROR: Input for size of list or index of the smallest element " +
          "is invalid. Please run the program again.")