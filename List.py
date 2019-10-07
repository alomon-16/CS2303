# Course: CS 2302 Data Structures
# Author: Alonso Monarrez
# Assignment: Lab 3 Linked Lists
# Instructor: Olac Fuentes
# TA: Anindita Nath
# Date of last modification: October 6
# Purpose: The purpose of this program is to implement the functions that will
# be used to apply various operations on a linked list.
from SortedList import Node, SortedList
import math
    
class List(SortedList):
    # The List class inherits the constructor to build the linked
    # list and the following functions: Print(), Delete(i), IndexOf(i),
    # and Clear().
    pass
                    
    def Insert(self, i):
        """
        Append integer i to the linked list. If the list is
        empty, insert the integer as a single node. Duplicates
        are allowed to be inserted.
        """
        if self.head == None:
            self.head = Node(i)
            self.tail = self.head
        else:
            self.tail.next = Node(i)
            self.tail = self.tail.next
            
    def Merge(self, M):
        """
        Append a second linked list to the original linked list.
        If the original list is empty, the second linked list is
        considered as a single linked list.
        """
        if self.head == None:
            self.head = M.head
            self.tail = M.tail
        else:
            self.tail.next = M.head
            self.tail = M.tail
            
    def Min(self):
        """
        Traverse through the linked list and return the smallest
        element in the list. If the list is empty, return math.inf.
        """
        if self.head == None:
            return math.inf
        curr = self.head
        minimum = curr.data
        while curr != None:
            # If the value of the current node is less than the
            # current value of minimum, update the value of
            # minimum.
            if curr.data < minimum:
                minimum = curr.data
            curr = curr.next
        return minimum
    
    def Max(self):
        """
        Traverse through the linked list and return the largest
        element in the list. If the list is empty, return -math.inf.
        """
        if self.head == None:
            return -math.inf
        curr = self.head
        maximum = curr.data
        while curr != None:
            # If the value of the current node is greater than the
            # current value of maximum, update the value of
            # maximum.
            if curr.data > maximum:
                maximum = curr.data
            curr = curr.next
        return maximum
    
    def HasDuplicates(self):
        """
        Traverse through the linked list and compare the current
        node with the rest of the nodes in the list. If any of the
        following nodes have the same value as the current node,
        return True. If the list is empty or contains a single element,
        return False.
        """
        if self.head == None or self.head.next == None:
            return False
        curr = self.head
        while curr.next != None:
            nxt = curr.next
            while nxt != None:
                if curr.data == nxt.data:
                    return True
                nxt = nxt.next
            # Update the current pointer to the next node in the
            # linked list and repeat the process until a pair of
            # duplicates is found, or the current pointer reaches
            # the last element of the list.
            curr = curr.next
        return False
    
    def BubbleSort(self):
        """
        Sort a linked list of integers by swapping adjacent elements
        if they are in the wrong order. The list is considered sorted
        only if there is a whole traversal without any swaps.
        """
        isSorted = False
        while not isSorted:
            isSorted = True
            curr = self.head
            # Traverse through the linked list until its last element.
            while curr.next != None:
                # Swap the values of the current and next nodes if they
                # are in the wrong order.
                if curr.data > curr.next.data:
                    curr.data, curr.next.data = curr.next.data, curr.data
                    isSorted = False
                curr = curr.next
                
    def Select(self, k):
        """
        Use bubble sort to sort the linked list in order to
        traverse through it and return the smallest element in
        the list at position k. If the value of k is less than 0,
        return math.inf.
        """
        if k < 0:
            return math.inf
        self.BubbleSort()
        curr = self.head
        while curr != None:
            # If the value of k reaches 0, return the value
            # of the current node.
            if k == 0:
                return curr.data
            # Otherwise, decrement the value of k for the
            # following node.
            else:
                k -= 1
                curr = curr.next
        # If the has less than k-1 elements, return math.inf.
        if k >= 0:
            return math.inf