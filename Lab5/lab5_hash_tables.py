# Course: CS 2302 Data Structures
# Author: Alonso Monarrez
# Assignment: Lab 5 Hash Tables
# Instructor: Olac Fuentes
# TA: Anindita Nath
# Date of last modification: November 3
# Purpose: The purpose of this program is to implement a hash table that
# solves collisions by either chaining or linear probing along with a hash
# function selected by the user in order to retrieve word embeddings that
# allow the comparison of two words and compare the running times of these
# two implementations of the data stucture.
import HashTableChain as htc
import HashTableLP as htlp
import WordEmbeddingHashTable as we
import time

print('Choose table implementation')
print('Type 1 for hash table with chaining or 2 for hash table with linear ' +
      'probing')
hash_table_implement = input('Choice: ')

print('\nChoose hash function (n is the length of the table)')
print('1. Length of the word % n')
print('2. ASCII value of the first character in the word % n')
print('3. Product of the ASCII values of the first and last characters in ' +
      'the word % n')
print('4. Sum of the ASCII values of the characters in the word % n')
print('5. Recursive formulation')
print('6. Polynomial formulation')
h_function = input('Choice: ')

compare_words = input('Would you like to enter two words to find their ' +
                      'similarity? (y/n): ')
if compare_words == 'y':
    user_words = []
    for i in range(2):
        user_word = input('Enter word ' + str(i+1) + ': ')
        user_words.append(user_word)

words_file = open('glove.6B.50d.txt', 'r', encoding="utf-8-sig")
word_pairs = open('word.pairs.txt', 'r')
            
# Size of the hash table is determined by the size of the file containing the
# words and their corresponding embedding.
table_size = 0
for line in words_file:
    table_size += 1
    
if hash_table_implement == '1':
    print('\nBuilding hash table with chaining\n')
    # Size of the hash table remains the same as previously determined to
    # allow every word and its embedding in the file to be inserted in the hash
    # table that solves collisions by chaining according to the hash function
    # provided by the user.
    h_table = htc.HashTableChain(table_size)
    start_time = time.time()
    h_table = htc.buildHashTableChain(h_table, words_file, h_function)
    end_time = time.time()
    print('Hash Table with Chaining stats:')
    load_factor = h_table.loadFactor()
    print('Load factor: ' + str(load_factor))
    hash_table_size = len(h_table.bucket)
    print('Size of hash table: ' + str(hash_table_size))
    percent_usage = round(h_table.percentUsage(), 6)
    print('Percent usage: ' + str(percent_usage))
    total_time = end_time - start_time
    print('Running time for hash table with chaining construction: ' +
          str(round(total_time, 6)) + ' seconds.\n')
    
    if compare_words == 'y':
        start_time = time.time()
        similarity = we.findSimilarityHTC_V2(h_table, user_words, h_function)
        end_time = time.time()
        print('Word similarities found:')
        print('Similarity [' + user_words[0] + ',' + user_words[1] + '] = ' +
              str(round(similarity, 4)))
        print()
        total_time = end_time - start_time
        print('Running time for hash table with chaining query processing: ' +
              str(round(total_time, 6)) + ' seconds.\n')
        
    elif compare_words == 'n':
        print('Reading word file to determine similarities\n')
        start_time = time.time()
        similarities = we.findSimilarityHTC(h_table, word_pairs, h_function)
        end_time = time.time()
        print('Word similarities found:')
        we.displaySimilarityHT(similarities, word_pairs)
        print()
        total_time = end_time - start_time
        print('Running time for hash table with chaining query processing: ' +
              str(round(total_time, 6)) + ' seconds.\n')
        
elif hash_table_implement == '2':
    print('\nBuilding hash table with linear probing\n')
    # Size of the hash table is modified to allow every word and its embedding
    # in the file to be inserted in the hash table that solves collisions by
    # linear probing according to the hash function provided by the user.
    h_table = htlp.HashTableLP(table_size*5)
    start_time = time.time()
    h_table = htlp.buildHashTableLP(h_table, words_file, h_function)
    end_time = time.time()
    print('Hash Table with Linear Probing stats:')
    load_factor = h_table.loadFactor()
    print('Load factor: ' + str(load_factor))
    hash_table_size = len(h_table.item)
    print('Size of hash table: ' + str(hash_table_size))
    percent_usage = round(h_table.percentUsage(), 6)
    print('Percent usage: ' + str(percent_usage))
    total_time = end_time - start_time
    print('Running time for hash table with linear probing construction: ' +
          str(round(total_time, 6)) + ' seconds.\n')
    
    if compare_words == 'y':
        start_time = time.time()
        similarity = we.findSimilarityHTLP_V2(h_table, user_words, h_function)
        end_time = time.time()
        print('Word similarities found:')
        print('Similarity [' + user_words[0] + ',' + user_words[1] + '] = ' +
              str(round(similarity, 4)))
        print()
        total_time = end_time - start_time
        print('Running time for hash table with linear probing query ' +
              'processing: ' + str(round(total_time, 6)) + ' seconds.\n')
        
    elif compare_words == 'n':
        print('Reading word file to determine similarities\n')
        start_time = time.time()
        similarities = we.findSimilarityHTLP(h_table, word_pairs, h_function)
        end_time = time.time()
        print('Word similarities found:')
        we.displaySimilarityHT(similarities, word_pairs)
        print()
        total_time = end_time - start_time
        print('Running time for hash table with linear probing query ' +
              'processing: ' + str(round(total_time, 6)) + ' seconds.\n')
else:
    print('ERROR: Invalid choice. Please run the program again.')