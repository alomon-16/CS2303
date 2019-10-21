# Course: CS 2302 Data Structures
# Author: Alonso Monarrez (original source code provided by Olac Fuentes)
# Assignment: Lab 4 Trees
# Instructor: Olac Fuentes
# TA: Anindita Nath
# Date of last modification: October 20
# Purpose: The purpose of this program is to implement the necessary functions
# to build a BST that holds WordEmbedding objects, which contain a word and
# its embedding.
import WordEmbedding

class BST(object):
    # Constructor
    def __init__(self, data, left=None, right=None):  
        self.data = data
        self.left = left 
        self.right = right

def buildBST(T,file):
    """
    Read through the text file to retrieve each word and its embedding. If a
    word starts with an alphabetic character, create a WordEmbedding object
    for that word and its embedding and insert it in its proper place in the
    BST.
    """
    for line in file:
        word_line = line.split(' ')
        word = word_line[0]
        embedding = word_line[1:]
        embedding = [float(i) for i in embedding]
        if word[0].isalpha():
            word_emb_object = WordEmbedding.WordEmbedding(word, embedding)
            T = insert(T, word_emb_object)
    return T
        
def insert(T,newdata):
    """
    Traverse through a single path of the BST to insert a WordEmbedding
    object as a single node in the tree.
    """
    if T == None:
        T = BST(newdata)
    elif T.data.word > newdata.word:
        T.left = insert(T.left,newdata)
    else:
        T.right = insert(T.right,newdata)
    return T

def search(T,word):
    """
    Return the WordEmbedding object node where the word is found in the BST.
    If the word is not in the tree, return None.
    """
    if T == None:
        return None
    if T.data.word == word:
        return T.data
    elif T.data.word > word:
        return search(T.left, word)
    else:
        return search(T.right, word)
    
def numNodes(T):
    """
    Traverse through the entire BST to calculate the number of nodes it has.
    """
    if T == None:
        return 0
    return 1 + numNodes(T.left) + numNodes(T.right)

def height(T):
    """
    Traverse through the entire BST to determine its longest path, which is the
    same as finding the height of the tree.
    """
    if T == None:
        return -1
    return max(height(T.left)+1, height(T.right)+1)