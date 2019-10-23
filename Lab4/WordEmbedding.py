# Course: CS 2302 Data Structures
# Author: Alonso Monarrez
# Assignment: Lab 4 Trees
# Instructor: Olac Fuentes
# TA: Anindita Nath
# Date of last modification: October 20
# Purpose: The purpose of this program is to find and display the similarities
# of paired words provided by a text file or the user.
import BST
import BTree
import numpy as np

class WordEmbedding(object):
    # Constructor
    def __init__(self,word,embedding):
        self.word = word
        self.emb = np.array(embedding, dtype=np.float32)
            
def findSimilarityA(T, file):
    """
    Read through the text file to retrieve each pair of words to be searched
    in a BST. Once both words are found, retrieve their corresponding
    embeddings and use the cosine distance to calculate their similarity.
    Store the similarity for each pair of words in the file in a list and 
    return that list.
    """
    L = []
    for line in file:
        word_line = line.strip()
        word_pair = word_line.split(' ')
        first_word = BST.search(T, word_pair[0])
        second_word = BST.search(T, word_pair[1])
        first_emb = first_word.emb
        second_emb = second_word.emb
        dot_product = np.dot(first_emb, second_emb)
        magnitude = np.linalg.norm(first_emb) * np.linalg.norm(second_emb)
        similarity = dot_product / magnitude
        L.append(round(similarity, 4))
    return L

def findSimilarityB(T, file):
    """
    Read through the text file to retrieve each pair of words to be searched
    in a B-Tree. Once both words are found, retrieve their corresponding
    embeddings and use the cosine distance to calculate their similarity.
    Store the similarity for each pair of words in the file in a list and 
    return that list.
    """
    L = []
    for line in file:
        word_line = line.strip()
        word_pair = word_line.split(' ')
        first_word = BTree.search(T, word_pair[0])
        second_word = BTree.search(T, word_pair[1])
        first_emb = first_word.emb
        second_emb = second_word.emb
        dot_product = np.dot(first_emb, second_emb)
        magnitude = np.linalg.norm(first_emb) * np.linalg.norm(second_emb)
        similarity = dot_product / magnitude
        L.append(round(similarity, 4))
    return L

def findSimilarityC(T, L):
    """
    Search through the BST to find each one of the paired words provided by
    the user. Once both words are found, retrieve their
    corresponding embeddings and use the cosine distance to calculate and
    return their similarity.
    """
    first_word = BST.search(T, L[0])
    second_word = BST.search(T, L[1])
    first_emb = first_word.emb
    second_emb = second_word.emb
    dot_product = np.dot(first_emb, second_emb)
    magnitude = np.linalg.norm(first_emb) * np.linalg.norm(second_emb)
    similarity = dot_product / magnitude
    return similarity

def findSimilarityD(T, L):
    """
    Search through the B-Tree to find each one of the paired words provided by
    the user. Once both words are found, retrieve their
    corresponding embeddings and use the cosine distance to calculate and
    return their similarity.
    """
    first_word = BTree.search(T, L[0])
    second_word = BTree.search(T, L[1])
    first_emb = first_word.emb
    second_emb = second_word.emb
    dot_product = np.dot(first_emb, second_emb)
    magnitude = np.linalg.norm(first_emb) * np.linalg.norm(second_emb)
    similarity = dot_product / magnitude
    return similarity

def displaySimilarity(L, file):
    """
    Read through the text file and traverse a list of similarity values to
    display each pair of words in the text file with its corresponding
    similarity.
    """
    file.seek(0)
    index = 0
    for line in file:
        word_line = line.strip()
        word_pair = word_line.split(' ')
        print('Similarity [' + word_pair[0] + ',' + word_pair[1] + '] = '
              + str(L[index]))
        index += 1