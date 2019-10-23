# Course: CS 2302 Data Structures
# Author: Alonso Monarrez
# Assignment: Lab 4 Trees
# Instructor: Olac Fuentes
# TA: Anindita Nath
# Date of last modification: October 20
# Purpose: The purpose of this program is to implement a BST and a B-Tree to
# retrieve word embeddings that allow the comparison of two words and compare
# the running times of these two data structures.
import BST
import BTree
import WordEmbedding
import time

print('Choose table implementation')
print('Type 1 for binary search tree or 2 B-tree')      
tree_implement = input('Choice: ')

compare_words = input('Would you like to enter two words to find their ' +
                      'similarity? (y/n): ')
if compare_words == 'y':
    user_words = []
    for i in range(2):
        user_word = input('Enter word ' + str(i+1) + ': ')
        user_words.append(user_word)

words_file = open('glove.6B.50d.txt', 'r', encoding="utf-8-sig")
word_pairs_file = open('word.pairs.txt', 'r')

if tree_implement == '1':
    print('\nBuilding binary search tree\n')
    BST_tree = None
    start_time = time.time()
    BST_tree = BST.buildBST(BST_tree, words_file)
    end_time = time.time()
    print('Binary Search Tree stats:')
    num_nodes = BST.numNodes(BST_tree)
    print('Number of nodes: ' + str(num_nodes))
    height = BST.height(BST_tree)
    print('Height: ' + str(height))
    total_time = end_time - start_time
    print('Running time for binary search tree construction: ' +
          str(round(total_time, 6)) + ' seconds.\n')
    
    if compare_words == 'y':
        start_time = time.time()
        similarity = WordEmbedding.findSimilarityC(BST_tree, user_words)
        end_time = time.time()
        print('Word similarities found:')
        print('Similarity [' + user_words[0] + ',' + user_words[1] + '] = ' +
              str(round(similarity, 4)))
        print()
        total_time = end_time - start_time
        print('Running time for binary search tree query processing: ' +
              str(round(total_time, 6)) + ' seconds.\n')
        
    elif compare_words == 'n':
        print('Reading word file to determine similarities\n')
        start_time = time.time()
        similarities = WordEmbedding.findSimilarityA(BST_tree, word_pairs_file)
        end_time = time.time()
        print('Word similarities found:')
        WordEmbedding.displaySimilarity(similarities, word_pairs_file)
        print()
        total_time = end_time - start_time
        print('Running time for binary search tree query processing: ' +
              str(round(total_time, 6)) + ' seconds.\n')
    
elif tree_implement == '2':
    max_items = int(input('Maximum number of items in node: '))
    print('\nBuilding B-tree\n')
    B_tree = BTree.BTree([], max_data=max_items)
    start_time = time.time()
    B_tree = BTree.buildBTree(B_tree, words_file)
    end_time = time.time()
    print('B-tree stats:')
    num_nodes = BTree.numNodes(B_tree)
    print('Number of nodes: ' + str(num_nodes))
    height = BTree.height(B_tree)
    print('Height: ' + str(height))
    total_time = end_time - start_time
    print('Running time for B-tree construction (with max_items = ' +
          str(max_items) + '): ' + str(round(total_time, 6)) + ' seconds.\n')
    
    if compare_words == 'y':
        start_time = time.time()
        similarity = WordEmbedding.findSimilarityD(B_tree, user_words)
        end_time = time.time()
        print('Word similarities found:')
        print('Similarity [' + user_words[0] + ',' + user_words[1] + '] = ' +
              str(round(similarity, 4)))
        print()
        total_time = end_time - start_time
        print('Running time for B-tree query processing (with max_items = ' +
              str(max_items) + '): ' + str(round(total_time, 6)) +
              ' seconds.\n')
        
    elif compare_words == 'n':
        print('Reading word file to determine similarities\n')
        start_time = time.time()
        similarities = WordEmbedding.findSimilarityB(B_tree, word_pairs_file)
        end_time = time.time()
        print('Word similarities found:')
        WordEmbedding.displaySimilarity(similarities, word_pairs_file)
        print()
        total_time = end_time - start_time
        print('Running time for B-tree query processing (with max_items = ' +
              str(max_items) + '): ' + str(round(total_time, 6)) +
              ' seconds.\n')
else:
    print('ERROR: Invalid choice. Please run the program again.')