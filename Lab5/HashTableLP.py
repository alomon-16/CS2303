# Course: CS 2302 Data Structures
# Author: Alonso Monarrez (original source code provided by Olac Fuentes)
# Assignment: Lab 5 Hash Tables
# Instructor: Olac Fuentes
# TA: Anindita Nath
# Date of last modification: November 3
# Purpose: The purpose of this program is to implement the necessary functions
# that calculate the corresponding hash value in order to build a hash table
# that solves collisions by linear probing and holds WordEmbeddingHashTable
# objects, which contain a word and its embedding.
import WordEmbeddingHashTable as we
import numpy as np

class HashTableLP(object):
    # Build a hash table of size 'size' that accepts objects as its elements
    # Initialize each bucket to -1 (which means empty)
    # Constructor
    def __init__(self,size):  
        self.item = np.zeros(size,dtype=object)-1
        
    def h1(self, word):
        """
        Calculate the hash value of an element (either a WordEmbeddingHashTable
        object or a string) in the table by dividing the length of the string
        by the length of the table and returning the value of the remainder.
        """
        return len(word) % len(self.item)
    
    def h2(self, word):
        """
        Calculate the hash value of an element in the table by dividing the
        ASCII value of the first character in the string by the length of the
        table and returning the value of the remainder.
        """
        return ord(word[0]) % len(self.item)
    
    def h3(self, word):
        """
        Calculate the hash value of an element in the table by dividing the
        the product of the ASCII values of the first and last characters in
        the string by the length of the table and returning the value of the
        remainder.
        """
        return (ord(word[0]) * ord(word[-1])) % len(self.item)
    
    def h4(self, word):
        """
        Calculate the hash value of an element in the table by dividing the
        the sum of the ASCII values of the characters in the string by the
        length of the table and returning the value of the remainder.
        """
        sum_ascii = 0
        for c in word:
            sum_ascii += ord(c)
        return sum_ascii % len(self.item)
    
    def h5(self, word):
        """
        Calculate the hash value of an element in the table by dividing the
        the sum of the ASCII values of the characters in the string obtained
        through a recursive formulation by the length of the table and
        returning the value of the remainder.
        """
        if len(word) == 0:
            # Return 1 if the current string contains no characters
            return 1
        # Otherwise, add the ASCII value of the first character in the string
        # to the product of 255 and the returned value of the recursive call.
        return (ord(word[0]) + 255 * self.h5(word[1:])) % len(self.item)
    
    def h6(self, word):
        """
        Calculate the hash value of an element in the table by dividing the
        the sum of the ASCII values of the characters in the string obtained
        through a polynomial formulation by the length of the table and
        returning the value of the remainder.
        """
        poly_sum = 0
        # The coefficient used in this hash function was chosen arbitrarily
        # until 41 was found that it yielded efficient load factor to percent
        # usage ratios.
        coefficient = 41
        # The highest order exponent of this polynomial expression is the
        # length of the string minus 1.
        exponent = len(word) - 1
        # Traverse through each character in the string and add the value of
        # the product of the ASCII value of the current character and the
        # coefficient raised to the current value of the exponent.
        for i in range(len(word)):
            poly_sum += ord(word[i]) * (coefficient ** exponent)
            exponent -= 1
        return poly_sum % len(self.item)
        
    def insert(self, k, hash_function):
        """
        Insert k (a WordEmbeddingHashTable object) in the table according to
        the hash function chosen by the user. The insert function continues
        traversing through the table until it finds an empty bucket (i.e. a -1)
        where it can insert k in the table.
        """
        for i in range(len(self.item)):
            # The word in the WordEmbeddingHashTable object determines its
            # hash value.
            if hash_function == '1':
                pos = self.h1(k.word) + i
            elif hash_function == '2':
                pos = self.h2(k.word) + i
            elif hash_function == '3':
                pos = self.h3(k.word) + i
            elif hash_function == '4':
                pos = self.h4(k.word) + i
            elif hash_function == '5':
                pos = self.h5(k.word) + i
            elif hash_function == '6':
                pos = self.h6(k.word) + i
            # Insert k in the table if the element in the current position is
            # -1 (i.e. if the bucket is empty). Return the position of k in the
            # table.
            if self.item[pos] == -1:
                self.item[pos] = k
                return pos
        # Return -1 if k could not be inserted in the table. 
        return -1
    
    def find(self,k,hash_function):
        """
        Return item (a WordEmbeddingHashTable object) that matches k (a string)
        in the appropriate position in the table according to the hash
        function chosen by the user. The find function continues traversing
        through the table until it finds the matching item or a bucket that
        contains a -1 (i.e. an empty-since-start bucket).
        """
        # k determines the hash value of the bucket in which it could be found.
        for i in range(len(self.item)):
            if hash_function == '1':
                pos = self.h1(k) + i
            elif hash_function == '2':
                pos = self.h2(k) + i
            elif hash_function == '3':
                pos = self.h3(k) + i
            elif hash_function == '4':
                pos = self.h4(k) + i
            elif hash_function == '5':
                pos = self.h5(k) + i
            elif hash_function == '6':
                pos = self.h6(k) + i
            # Return the item at the position dictated by the hash value if k
            # matches with the word of the WordEmbeddingHashTable object in
            # that position.
            if self.item[pos].word == k:
                return self.item[pos]
            # Return -1 if the function encounters an empty-since-start
            # bucket.
            if self.item[pos] == -1:
                return -1
        # Return -1 if k is not in the table.
        return -1
    
    def loadFactor(self):
        """
        Calculate the load factor of the table by dividing the total number of
        elements in the table by the length of the table. To determine the
        number of elements in the table, traverse through the table and add
        each bucket that contains an elements that is not a -1.
        """
        num_items = 0
        for item in self.item:
            if item != -1:
                num_items += 1
        return num_items / len(self.item)
    
    def percentUsage(self):
        """
        Calculate the percent usage of the table by dividing the total number
        of non-empty buckets in the table by the length of the table and
        multiplying that times 100. To determine the number of non-empty
        buckets, traverse through the table and add each bucket that contains
        an elements that is not a -1.
        """
        non_empty_buckets = 0
        for item in self.item:
            if item != -1:
                non_empty_buckets += 1
        return (non_empty_buckets / len(self.item)) * 100
    
def buildHashTableLP(H, file, hash_function):
    """
    Read through the text file to retrieve each word and its embedding. If a
    word starts with an alphabetic character, create a WordEmbeddingHashTable
    object for that word and its embedding and insert it in its proper place
    in the hash table that solves collision by linear probing.
    """
    file.seek(0)
    for line in file:
        word_line = line.split(' ')
        word = word_line[0]
        embedding = word_line[1:]
        embedding = [float(i) for i in embedding]
        if word[0].isalpha():
            word_emb_object = we.WordEmbeddingHashTable(word, embedding)
            H.insert(word_emb_object, hash_function)
    return H