# Course: CS 2302 Data Structures
# Author: Alonso Monarrez
# Assignment: Lab 5 Hash Tables
# Instructor: Olac Fuentes
# TA: Anindita Nath
# Date of last modification: November 3
# Purpose: The purpose of this program is to find and display the similarities
# of paired words provided by a text file or the user. The paired words will
# be searched in a hash table that solves collisions by either chaining or
# linear probing.
import HashTableChain as htc
import HashTableLP as htlp
import numpy as np

class WordEmbeddingHashTable(object):
    # Constructor
    def __init__(self,word,embedding):
        self.word = word
        self.emb = np.array(embedding, dtype=np.float32)
        
def findSimilarityHTC(H, file, hash_function):
    """
    Read through the text file to retrieve each pair of words to be searched
    in a hash table that solves collisions by chaining according to the hash
    function provided by the user.
    Once both words are found in the table, retrieve their corresponding
    embeddings and use the cosine distance to calculate their similarity.
    Store the similarity for each pair of words in the file in a list and 
    return that list.
    """
    L = []
    for line in file:
        word_line = line.strip()
        word_pair = word_line.split(' ')
        first_word = H.find(word_pair[0], hash_function)
        second_word = H.find(word_pair[1], hash_function)
        first_emb = first_word.emb
        second_emb = second_word.emb
        dot_product = np.dot(first_emb, second_emb)
        magnitude = np.linalg.norm(first_emb) * np.linalg.norm(second_emb)
        similarity = dot_product / magnitude
        L.append(round(similarity, 4))
    return L

def findSimilarityHTC_V2(H, L, hash_function):
    """
    Search through the hash table that solves collisions by chaining to find
    each one of the paired words provided by the user according to the hash
    function provided by the user.
    Once both words are found, retrieve their corresponding embeddings and use
    the cosine distance to calculate and return their similarity.
    """
    first_word = H.find(L[0], hash_function)
    second_word = H.find(L[1], hash_function)
    first_emb = first_word.emb
    second_emb = second_word.emb
    dot_product = np.dot(first_emb, second_emb)
    magnitude = np.linalg.norm(first_emb) * np.linalg.norm(second_emb)
    similarity = dot_product / magnitude
    return similarity

def findSimilarityHTLP(H, file, hash_function):
    """
    Read through the text file to retrieve each pair of words to be searched
    in a hash table that solves collisions by linear probing according to the
    hash function provided by the user.
    Once both words are found, retrieve their corresponding embeddings and use
    the cosine distance to calculate their similarity.
    Store the similarity for each pair of words in the file in a list and 
    return that list.
    """
    L = []
    for line in file:
        word_line = line.strip()
        word_pair = word_line.split(' ')
        first_word = H.find(word_pair[0], hash_function)
        second_word = H.find(word_pair[1], hash_function)
        first_emb = first_word.emb
        second_emb = second_word.emb
        dot_product = np.dot(first_emb, second_emb)
        magnitude = np.linalg.norm(first_emb) * np.linalg.norm(second_emb)
        similarity = dot_product / magnitude
        L.append(round(similarity, 4))
    return L

def findSimilarityHTLP_V2(H, L, hash_function):
    """
    Search through the hash table that solves collisions by linear probing to
    find each one of the paired words provided by the user according to the
    hash function provided by the user.
    Once both words are found, retrieve their corresponding embeddings and use
    the cosine distance to calculate and return their similarity.
    """
    first_word = H.find(L[0], hash_function)
    second_word = H.find(L[1], hash_function)
    first_emb = first_word.emb
    second_emb = second_word.emb
    dot_product = np.dot(first_emb, second_emb)
    magnitude = np.linalg.norm(first_emb) * np.linalg.norm(second_emb)
    similarity = dot_product / magnitude
    return similarity

def displaySimilarityHT(L, file):
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