# Course: CS 2302 Data Structures
# Author: Alonso Monarrez (original source code provided by Olac Fuentes)
# Assignment: Lab 4 Trees
# Instructor: Olac Fuentes
# TA: Anindita Nath
# Date of last modification: October 20
# Purpose: The purpose of this program is to implement the necessary functions
# to build a B-Tree that holds WordEmbedding objects, which contain a word and
# its embedding.
import WordEmbedding

class BTree(object):
    # Constructor
    def __init__(self,data,child=[],isLeaf=True,max_data=5):  
        self.data = data
        self.child = child 
        self.isLeaf = isLeaf
        if max_data <3: #max_data must be odd and greater or equal to 3
            max_data = 3
        if max_data%2 == 0: #max_data must be odd and greater or equal to 3
            max_data +=1
        self.max_data = max_data
        
def buildBTree(T, file):
    """
    Read through the text file to retrieve each word and its embedding. If a
    word starts with an alphabetic character, create a WordEmbedding object
    for that word and its embedding and insert it in its proper place in the
    B-Tree.
    """
    for line in file:
        word_line = line.split(' ')
        word = word_line[0]
        embedding = word_line[1:]
        embedding = [float(i) for i in embedding]
        if word[0].isalpha():
            word_emb_object = WordEmbedding.WordEmbedding(word, embedding)
            insertElement(T, word_emb_object)
    return T  

def findChildA(T,k):
    """
    If k, a WordEmbedding object, is in the B-Tree, determine the value of c,
    such that k must be in the subtree T.child[c]. This function helps
    determine the proper place of each WordEmbedding object in the B-Tree.
    """   
    for i in range(len(T.data)):
        if k.word < T.data[i].word:
            return i
    return len(T.data)

def findChildB(T,k):
    """
    If k, a word string, is in the B-Tree, determine the value of c, such that
    k must be in the subtree T.child[c]. This function helps search a word
    in the B-Tree by comparing it to the word in each WordEmbedding object in
    the node.
    """
    for i in range(len(T.data)):
        if k < T.data[i].word:
            return i
    return len(T.data)
             
def insertInternal(T,i):
    """
    Insert a WordEmbedding object into an internal node of the B-Tree. If the
    node is full, split it so that the object can be inserted into a non-full,
    internal node.
    """
    if T.isLeaf:
        insertLeaf(T,i)
    else:
        k = findChildA(T,i)   
        if isFull(T.child[k]):
            m, l, r = split(T.child[k])
            T.data.insert(k,m) 
            T.child[k] = l
            T.child.insert(k+1,r) 
            k = findChildA(T,i)  
        insertInternal(T.child[k],i)   
            
def split(T):
    """
    If a full node is found while inserting WordEmbedding objects into the
    B-Tree, break it by prompting its median to the parent node.
    """
    mid = T.max_data//2
    if T.isLeaf:
        leftChild = BTree(T.data[:mid],max_data=T.max_data) 
        rightChild = BTree(T.data[mid+1:],max_data=T.max_data) 
    else:
        leftChild = BTree(T.data[:mid],T.child[:mid+1],T.isLeaf,max_data=T.max_data) 
        rightChild = BTree(T.data[mid+1:],T.child[mid+1:],T.isLeaf,max_data=T.max_data) 
    return T.data[mid], leftChild,  rightChild   
      
def insertLeaf(T,i):
    """
    Insert a WordEmbedding object into the B-Tree. The sort() function for the
    list of the contents in the node is modified to accomodate for a list of
    WordEmbedding objects.
    """
    T.data.append(i)  
    T.data.sort(key=lambda x: x.word)

def isFull(T):
    """
    Determine whether a node in the B-Tree is full.
    """
    return len(T.data) >= T.max_data
        
def insertElement(T,i):
    """
    Insert a WordEmbedding object into a node of the B-Tree. If the
    node is full, split it so that the object can be inserted into a non-full
    node.
    """
    if not isFull(T):
        insertInternal(T,i)
    else:
        m, l, r = split(T)
        T.data = [m]
        T.child = [l,r]
        T.isLeaf = False
        k = findChildA(T,i)  
        insertInternal(T.child[k],i)
        
def search(T,k):
    """
    Return the WordEmbedding object from the node where k, a word string, is
    found in the B-Tree. If k is not in the tree, return None.
    """
    for t in T.data:
        if k == t.word:
            return t
    if T.isLeaf:
        return None
    return search(T.child[findChildB(T,k)],k)
        
def numNodes(T):
    """
    Traverse through the entire B-Tree to calculate the number of nodes it has.
    """
    n = 1
    if T.isLeaf:
        return n
    for i in range(len(T.child)):
        n += numNodes(T.child[i])
    return n
     
def height(T):
    """
    Traverse through a single path of the B-Tree (from the root to a single
    leaf) to calculate its height.
    """
    if T.isLeaf:
        return 0
    return 1 + height(T.child[0])    