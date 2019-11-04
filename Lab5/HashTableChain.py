# Course: CS 2302 Data Structures
# Author: Alonso Monarrez (original source code provided by Olac Fuentes)
# Assignment: Lab 5 Hash Tables
# Instructor: Olac Fuentes
# TA: Anindita Nath
# Date of last modification: November 3
# Purpose: The purpose of this program is to implement the necessary functions
# that calculate the corresponding hash value in order to build a hash table
# that solves collisions by chaining and holds WordEmbeddingHashTable objects,
# which contain a word and its embedding.
import WordEmbeddingHashTable as we

class HashTableChain(object):
    # Build a hash table of size 'size'
    # The table is a list of (initially empty) lists
    # Constructor
    def __init__(self,size):  
        self.bucket = [[] for i in range(size)]
            
    def h1(self, word):
        """
        Calculate the hash value of an element (either a WordEmbeddingHashTable
        object or a string) in the table by dividing the length of the string
        by the length of the table and returning the value of the remainder.
        """
        return len(word) % len(self.bucket)
    
    def h2(self, word):
        """
        Calculate the hash value of an element in the table by dividing the
        ASCII value of the first character in the string by the length of the
        table and returning the value of the remainder.
        """
        return ord(word[0]) % len(self.bucket)
    
    def h3(self, word):
        """
        Calculate the hash value of an element in the table by dividing the
        the product of the ASCII values of the first and last characters in
        the string by the length of the table and returning the value of the
        remainder.
        """
        return (ord(word[0]) * ord(word[-1])) % len(self.bucket)
    
    def h4(self, word):
        """
        Calculate the hash value of an element in the table by dividing the
        the sum of the ASCII values of the characters in the string by the
        length of the table and returning the value of the remainder.
        """
        sum_ascii = 0
        for c in word:
            sum_ascii += ord(c)
        return sum_ascii % len(self.bucket)
    
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
        return (ord(word[0]) + 255 * self.h5(word[1:])) % len(self.bucket)
    
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
        return poly_sum % len(self.bucket)
            
            
    def insert(self,k,hash_function):
        """
        Insert k (a WordEmbeddingHashTable object) in the appropriate bucket
        of the table according to the hash function chosen by the user.
        """
        # The word in the WordEmbeddingHashTable object determines its hash
        # value.
        if hash_function == '1':
            b = self.h1(k.word)
        elif hash_function == '2':
            b = self.h2(k.word)
        elif hash_function == '3':
            b = self.h3(k.word)
        elif hash_function == '4':
            b = self.h4(k.word)
        elif hash_function == '5':
            b = self.h5(k.word)
        elif hash_function == '6':
            b = self.h6(k.word)
        # Append k to the list in the appropriate bucket.
        self.bucket[b].append(k)
            
    def find(self,k,hash_function):
        """
        Return item (a WordEmbeddingHashTable object) that matches k (a string)
        in the appropriate bucket according to the hash function chosen by the
        user.
        """
        # k determines the hash value of the bucket in which it could be found.
        if hash_function == '1':
            b = self.h1(k)
        elif hash_function == '2':
            b = self.h2(k)
        elif hash_function == '3':
            b = self.h3(k)
        elif hash_function == '4':
            b = self.h4(k)
        elif hash_function == '5':
            b = self.h5(k)
        elif hash_function == '6':
            b = self.h6(k)
        # Traverse through each item in the appropriate bucket. Once k matches
        # with the word of an WordEmbeddingHashTable object, return that
        # object.
        for item in self.bucket[b]:
            if item.word == k:
                return item
        # Return -1 if k was not found in the table.
        return -1
    
    def loadFactor(self):
        """
        Calculate the load factor of the table by dividing the total number of
        elements in the table by the length of the table. To determine the
        number of elements in the table, add the length of the list in each
        bucket.
        """
        num_items = 0
        for b in self.bucket:
            num_items += len(b)
        return num_items / len(self.bucket)
        
    def percentUsage(self):
        """
        Calculate the percent usage of the table by dividing the total number
        of non-empty buckets in the table by the length of the table and
        multiplying that times 100. To determine the number of non-empty
        buckets, traverse through the table and add each bucket that contains
        a list of length greater than 0.
        """
        non_empty_buckets = 0
        for b in self.bucket:
            if len(b) > 0:
                non_empty_buckets += 1
        return (non_empty_buckets / len(self.bucket)) * 100 
    
def buildHashTableChain(H, file, hash_function):
    """
    Read through the text file to retrieve each word and its embedding. If a
    word starts with an alphabetic character, create a WordEmbeddingHashTable
    object for that word and its embedding and insert it in its proper place
    in the hash table that solves collision by chaining.
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