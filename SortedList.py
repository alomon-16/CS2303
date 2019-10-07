# Course: CS 2302 Data Structures
# Author: Alonso Monarrez
# Assignment: Lab 3 Linked Lists
# Instructor: Olac Fuentes
# TA: Anindita Nath
# Date of last modification: October 6
# Purpose: The purpose of this program is to implement the functions that will
# be used to apply various operations on a sorted linked list.
import math

class Node(object):
    # Constructor to build the nodes of the linked list
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
class SortedList(object):
    # Constructor to build the linked list
    def __init__(self):
        self.head = None
        self.tail = None
        
    def Print(self):
        """
        Traverse through the sorted linked list to
        print the data found in each node. Add an arrow
        that points to the next element of the linked list.
        """
        curr = self.head
        while curr != None:
            print(curr.data, end=' ')
            if curr.next != None:
                print('->', end=' ')
            curr = curr.next
        print()    

    def Insert(self, i):
        """
        Insert integer i to its proper place in the
        sorted linked list. If the list is empty,
        insert the integer as a single node. Duplicates
        are allowed to be inserted.
        """
        if self.head == None:
            self.head = Node(i)
            self.tail = self.head
        else:
            # Prepend integer i to the sorted linked list
            # if its value is less than that of the list's
            # head.
            if i <= self.head.data:
                self.head = Node(i, self.head)
                return
            # Append integer i to the sorted linked list
            # if its value is greater than that of the list's
            # tail.
            elif i >= self.tail.data:
                self.tail.next = Node(i)
                self.tail = self.tail.next
                return
            # Traverse through the sorted linked list to insert
            # integer i in its proper place if its value is
            # greater than that of the list's head but less than
            # that of the list's tail.
            curr = self.head
            while curr.next != None:
                if i >= curr.data and i <= curr.next.data:
                    curr.next = Node(i, curr.next)
                    return
                curr = curr.next
                
    def Delete(self, i):
        """
        Traverse through the sorted linked list to remove all
        instances of the integer i appearing in the list. If i is
        not in the list, the list remains unaffected.
        """
        prev = None
        curr = self.head
        while curr != None:
            # Remove and update the head of the sorted linked list
            # if its value matches that of integer i.
            if self.head.data == i:
                self.head = curr.next
                curr = self.head
            elif curr.data == i:
                # Remove and update the tail of the sorted linked list
                # if its value matches that of integer i.
                if curr.next == None:
                    self.tail = prev
                    prev.next = None
                    curr = curr.next
                # Otherwise, remove the node that has the same value
                # as integer i.
                else:
                    prev.next = curr.next
                    curr = curr.next
            # If the value of the current node did not match that of
            # intger i, update the previous and current pointers to
            # continue traversing through the list.
            else:
                prev = curr
                curr = curr.next
                
    def Merge(self, M):
        """
        Traverse through a second sorted linked list to insert
        each of its elements into its proper place in the original
        sorted linked list.
        """
        curr = M.head
        while curr != None:
            self.Insert(curr.data)
            curr = curr.next
            
    def IndexOf(self, i):
        """
        Traverse through the sorted linked list and return the
        index of integer i. If the list has duplicates, return
        only the first index. If integer i is not in the list,
        return -1.
        """
        index = 0
        curr = self.head
        while curr != None:
            # If the value of the current node matches that of
            # integer i, return the current value of the index.
            if curr.data == i:
                return index
            # Otherwise, increment the value of the index for
            # the following node.
            else:
                index += 1
                curr = curr.next
        return -1
    
    def Clear(self):
        """
        Remove all elements from the sorted linked list by
        having its head point to None.
        """
        self.head = None
        
    def Min(self):
        """
        Return the value of the sorted linked list's head since
        it is the smallest element in the list. If the list is
        empty, return math.inf.
        """
        if self.head == None:
            return math.inf
        return self.head.data
    
    def Max(self):
        """
        Return the value of the sorted linked list's tail since
        it is the largest element in the list. If the list is
        empty, return -math.inf.
        """
        if self.head == None:
            return -math.inf
        return self.tail.data
    
    def HasDuplicates(self):
        """
        Traverse through the sorted linked list and compare each
        pair of adjacent nodes. If two adjacent nodes have the same
        value, return True. Otherwise, return False. If the list is
        empty or contains a single element, return False.
        """
        if self.head == None or self.head.next == None:
            return False
        curr = self.head
        while curr.next != None:
            if curr.data == curr.next.data:
                return True
            curr = curr.next
        return False
    
    def Select(self, k):
        """
        Traverse through the sorted linked list and return the
        smallest element in the list at position k. If the value
        of k is less than 0, return math.inf.
        """
        if k < 0:
            return math.inf
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