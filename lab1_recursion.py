# Course: CS 2302 Data Structures
# Author: Alonso Monarrez
# Assignment: Lab 1 Recursion
# Instructor: Olac Fuentes
# TA: Anindita Nath
# Date of last modification: September 7
# Purpose: The purpose of this program is to recursively find the anagrams
# of a word entered by the user and print the anagrams.
import time

words_file = open("words_alpha.txt", "r")

words_set = set()
for word in words_file:
    words_set.add(word.strip())
    
prefix_set = set()
for word in words_set:
    for i in range(len(word)):
        prefix_set.add(word[:i])
                
anagrams_set = set()

# Part 1
 
def anagrams(word, permutation):
    """
    Store every valid anagram of a word in a set.
    Each recursive call moves a letter from the word
    to a permutation.
    """
    if len(word) == 0 and permutation in words_set:
        # Base case: A permutation of the word is formed and
        # checked to see if it is a valid anagram.
        anagrams_set.add(permutation)
    else:
        # Recursive case: For each call to this function,
        # move a letter from the word to a permutation.
        for i in range(len(word)):
            # The letter at index i will be added to form a permutation.
            single_letter = word[i]
            # The rest of the letters will be passed to the recursive call.
            leftover_letters = word[:i] + word[i+1:]
            # Call the function to continue forming permutations.
            anagrams(leftover_letters, permutation + single_letter)
            
# Part 2
            
def unique_anagrams(word, permutation):
    """
    Store every valid anagram of a word in a set.
    Each recursive call moves a letter from the word
    to a permutation.
    If the word has duplicate letters, only make the recursive
    call the first time the letter appears.
    """
    if len(word) == 0 and permutation in words_set:
        # Base case: A permutation of the word is formed and
        # checked to see if it is a valid anagram.
        anagrams_set.add(permutation)
    else:
        # Recursive case: For each call to this function,
        # move a letter from the word to a permutation.
        for i in range(len(word)):
            # If the letter at index i is not repeated throughout
            # the rest of the word, proceed with the recursive call.
            if word[i] not in word[i+1:]:
                # The letter at index i will be added to form a permutation.
                single_letter = word[i]
                # The rest of the letters will be passed to the recursive call.
                leftover_letters = word[:i] + word[i+1:]
                # Call the function to continue forming permutations.
                unique_anagrams(leftover_letters, permutation + single_letter)
                
def prefix_anagrams(word, permutation):
    """
    Store every valid anagram of a word in a set.
    Each recursive call moves a letter from the word
    to a permutation.
    If the word has duplicate letters, only make the recursive
    call the first time the letter appears.
    If a permutation is not a prefix of a word in the word set,
    do not make the recursive call.
    """
    if len(word) == 0 and permutation in words_set:
        # Base case: A permutation of the word is formed and
        # checked to see if it is a valid anagram.
        anagrams_set.add(permutation)
    else:
        # Recursive case: For each call to this function,
        # move a letter from the word to a permutation.
        for i in range(len(word)):
            # If the letter at index i is not repeated throughout
            # the rest of the word, proceed with the recursive call.
            if word[i] not in word[i+1:]:
                # If the permutation is a prefix of a word in the word
                # set, proceed with the recursive call.
                if permutation in prefix_set:
                    # The letter at index i will be added to form a
                    # permutation.
                    single_letter = word[i]
                    # The rest of the letters will be passed to the recursive
                    # call.
                    leftover_letters = word[:i] + word[i+1:]
                    # Call the function to continue forming permutations.
                    prefix_anagrams(leftover_letters, permutation + 
                                    single_letter)
                    
print("1. Run program and apply no optimizations.")
print("2. Run program and apply the first optimization.")
print("3. Run program and apply both optimizations.")

option = input("Enter 1, 2, or 3 to run the corresponding program: ")
if option == '1' or option == '2' or option == '3':
    continue_program = True
else:
    print("ERROR: %s is invalid! Please run the program again." % option)
    continue_program = False

while continue_program:
    user_word = input("Enter a word or empty string to finish: ")
    if user_word in words_set:
        start_time = time.time()
        if option == '1':
            anagrams(user_word, "")
        elif option == '2':
            unique_anagrams(user_word, "")
        elif option == '3':
            prefix_anagrams(user_word, "")
                    
        anagrams_set.remove(user_word)
        num_anagrams = str(len(anagrams_set))
        
        print("The word %s has the following %s anagrams:" 
              % (user_word, num_anagrams))
        
        for anagram in sorted(anagrams_set):
            print(anagram)
        end_time = time.time()

        total_time = str(round(end_time - start_time, 6))
        print("It took %s seconds to find the anagrams." % total_time)
        
        anagrams_set.clear()
    elif user_word == "":
        continue_program = False
    else:
        print("ERROR: %s is not valid! Please enter a valid word." % user_word)
    
print("Bye, thanks for using this program!")