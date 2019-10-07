# Course: CS 2302 Data Structures
# Author: Alonso Monarrez
# Assignment: Lab 3 Linked Lists
# Instructor: Olac Fuentes
# TA: Anindita Nath
# Date of last modification: October 6
# Purpose: The purpose of this program is to implement various operations
# and compare their implementations for a linked list and a sorted linked list.
from SortedList import SortedList
from List import List
import random, time

class GenerateList(object):
    # Constructor to build a native list to be inserted into a linked list.
    def __init__(self, n, high, low=1):
        self.n = n
        self.high = high
        self.low = low
        
    def ListWithDuplicates(self):
        """
        Generate and return a native list of random integers
        of size n. The randomly generated integers range from 1
        to n (e.g. if n is 100, each integer will range from
        1 to 100). Duplicates are allowed.
        """
        L = []
        for i in range(self.n):
            L.append(random.randint(self.low, self.high))
        return L

    def ListWithoutDuplicates(self):
        """
        Generate and return a native list of random integers
        of size n. The randomly generated integers range from 1
        to 2n (e.g. if n is 100, each integer will range from
        1 to 200). Duplicates are not allowed, and the list will only
        be returned once it is full.
        """
        L = []
        while len(L) < self.n:
            num = random.randint(self.low, self.high*2)
            if num not in L:
                L.append(num)
        return L
    
L1 = List()
L2 = SortedList()
L3 = List()
L4 = SortedList()

size = int(input("Enter a value for the size of the lists to be generated: "))
add_duplicates = input("Would you like your lists to have duplicates? (y/n): ")
if add_duplicates == 'y':
    list_object = GenerateList(size, size)
    native_list = list_object.ListWithDuplicates()
elif add_duplicates == 'n':
    list_object = GenerateList(size, size)
    native_list = list_object.ListWithoutDuplicates()
    
list_time = 0
sorted_list_time = 0
for num in native_list:
    start_time = time.time()
    L1.Insert(num)
    end_time = time.time()
    list_time += (end_time - start_time)
    start_time = time.time()
    L2.Insert(num)
    end_time = time.time()
    sorted_list_time += (end_time - start_time)
print("Running time to insert integers in the linked list: " +
      str(round(list_time, 6)) + " seconds.")
print("Running time to insert integers in the sorted linked list: " +
      str(round(sorted_list_time, 6)) + " seconds.")
print()

print("List:")
start_time = time.time()
L1.Print()
end_time = time.time()
list_time = end_time - start_time
print("Sorted list:")
start_time = time.time()
L2.Print()
end_time = time.time()
sorted_list_time = end_time - start_time
print("Running time to print the linked list: " + str(round(list_time, 6)) +
      " seconds.")
print("Running time to print the sorted linked list: " + 
      str(round(sorted_list_time, 6)) + " seconds.")

deleted_int = int(input("Enter an integer to be removed from the lists: "))
start_time = time.time()
L1.Delete(deleted_int)
end_time = time.time()
list_time = end_time - start_time
start_time = time.time()
L2.Delete(deleted_int)
end_time = time.time()
sorted_list_time = end_time - start_time
print("List:")
L1.Print()
print("Sorted list:")
L2.Print()
print("Running time to delete integers from the linked list: " +
      str(round(list_time, 6)) + " seconds.")
print("Running time to delete integers from the sorted linked list: " +
      str(round(sorted_list_time, 6)) + " seconds.")

size = int(input("Enter a value for the size of the lists to be merged " +
                 "with the original lists: "))
add_duplicates = input("Would you like your list to have duplicates? (y/n): ")
if add_duplicates == 'y':
    list_object = GenerateList(size, size)
    native_list = list_object.ListWithDuplicates()
elif add_duplicates == 'n':
    list_object = GenerateList(size, size)
    native_list = list_object.ListWithoutDuplicates()
for num in native_list:
    L3.Insert(num)
    L4.Insert(num)
print()
print("List to be merged with the linked list:")
L3.Print()
print("Sorted list to be merged with the sorted linked list:")
L4.Print()
print()

start_time = time.time()
L1.Merge(L3)
end_time = time.time()
list_time = end_time - start_time
start_time = time.time()
L2.Merge(L4)
end_time = time.time()
sorted_list_time = end_time - start_time
print("List:")
L1.Print()
print("Sorted list:")
L2.Print()
print("Running time to merge linked lists: " + str(round(list_time, 6)) +
      " seconds.")
print("Running time to merge sorted linked lists: " + 
      str(round(sorted_list_time, 6)) + " seconds.")

indexed_int = int(input("Enter an integer in the list of which the index " +
                        "will be returned: "))
start_time = time.time()
index_L1 = L1.IndexOf(indexed_int)
end_time = time.time()
list_time = end_time - start_time
start_time = time.time()
index_L2 = L2.IndexOf(indexed_int)
end_time = time.time()
sorted_list_time = end_time - start_time
print("Index of " + str(indexed_int) + " in the linked list: " + str(index_L1))
print("Index of " + str(indexed_int) + " in the sorted linked list: " +
      str(index_L2))
print("Running time to return the index of the integer in the linked list: " +
      str(round(list_time, 6)) + " seconds.")
print("Running time to return the index of the integer in the sorted linked " +
      "list: " + str(round(sorted_list_time, 6)) + " seconds.")
print()

start_time = time.time()
min_L1 = L1.Min()
end_time = time.time()
list_time = end_time - start_time
start_time = time.time()
min_L2 = L2.Min()
end_time = time.time()
sorted_list_time = end_time - start_time
print("Minimum of linked list: " + str(min_L1))
print("Minimum of sorted linked list: " + str(min_L2))
print("Running time to return the minimum of the linked list: " +
      str(round(list_time, 6)) + " seconds.")
print("Running time to return the minimum of the sorted linked list: " +
      str(round(sorted_list_time, 6)) + " seconds.")
print()

start_time = time.time()
max_L1 = L1.Max()
end_time = time.time()
list_time = end_time - start_time
start_time = time.time()
max_L2 = L2.Max()
end_time = time.time()
sorted_list_time = end_time - start_time
print("Maximum of linked list: " + str(max_L1))
print("Maximum of sorted linked list: " + str(max_L2))
print("Running time to return the maximum of the linked list: " +
      str(round(list_time, 6)) + " seconds.")
print("Running time to return the maximum of the sorted linked list: " +
      str(round(sorted_list_time, 6)) + " seconds.")
print()

start_time = time.time()
duplicates_L1 = L1.HasDuplicates()
end_time = time.time()
list_time = end_time - start_time
start_time = time.time()
duplicates_L2 = L2.HasDuplicates()
end_time = time.time()
sorted_list_time = end_time - start_time
print("Linked list has duplicates: " + str(duplicates_L1))
print("Sorted linked list has duplicates: " + str(duplicates_L2))
print("Running time to determine if the linked list has duplicates: " +
      str(round(list_time, 6)) + " seconds.")
print("Running time to determine if the sorted linked list has duplicates: " +
      str(round(sorted_list_time, 6)) + " seconds.")

k_value = int(input("Enter a value for the position of the smallest " +
                    "element of the lists: "))
start_time = time.time()
smallest_elem_L1 = L1.Select(k_value)
end_time = time.time()
list_time = end_time - start_time
start_time = time.time()
smallest_elem_L2 = L2.Select(k_value)
end_time = time.time()
sorted_list_time = end_time - start_time
print("Smallest element in the linked list at position " + str(k_value) +
      ": " + str(smallest_elem_L1))
print("Smallest element in the sorted linked list at position " +
      str(k_value) + ": " + str(smallest_elem_L2))
print("Running time to return the k-th smallest integer in the linked " +
      "list: " + str(round(list_time, 6)) + " seconds.")
print("Running time to return the k-th smallest integer in the sorted " +
      "linked list: " + str(round(sorted_list_time, 6)) + " seconds.")
print()

start_time = time.time()
L1.Clear()
end_time = time.time()
list_time = end_time - start_time
start_time = time.time()
L2.Clear()
end_time = time.time()
sorted_list_time = end_time - start_time
print("List:")
L1.Print()
print("Sorted list:")
L2.Print()
print("Running time to clear the linked list: " + str(round(list_time, 6)) +
      " seconds.")
print("Running time to clear the sorted linked list: " +
      str(round(sorted_list_time, 6)) + " seconds.")