# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''    
    # FILL IN YOUR CODE HERE...
    correctGuess = True
    for curChar in secretWord:
        if curChar not in lettersGuessed:
            return False
        
    return correctGuess


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    
    # Create list of "_" with length of secretword
    guessedWord = ["_ "] * len(secretWord)
    # loop through every char in letterGuessed
    for curChar in lettersGuessed:        
        # find index(s) of curChar in secretWord
        # and use it to fill guessedWord with curChar        
        for index in range(len(secretWord)):            
            if (secretWord[index] == curChar):                
                guessedWord[index] = secretWord[index]
                
    # create string from guessedWord list each char is separated by a space
    return ("").join(guessedWord)
    



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    availableLetters = list(string.ascii_lowercase)
    for curChar in lettersGuessed:
        availableLetters.remove(curChar)
        
    return ("").join(availableLetters)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) +  " letters long.")
    print("-----------")
    lettersGuessed = []
    mistakesMade = 8
    
    while mistakesMade > 0:        
        print("You have " + str(mistakesMade) + " guesses left.")       
        print("Available letters: " + getAvailableLetters(lettersGuessed))
        guess  = input("Please guess a letter: ") 
        guessInLowerCase = guess.lower()
                
        if guessInLowerCase in lettersGuessed:            
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        else:            
            lettersGuessed.append(guessInLowerCase)            
            curGuessWord = getGuessedWord(secretWord, lettersGuessed)            
            
            if guessInLowerCase in curGuessWord :
                print("Good guess: " + curGuessWord)                                
            else:
                print("Oops! That letter is not in my word: " + curGuessWord)
                mistakesMade = mistakesMade - 1
        
        print("-----------")
        if isWordGuessed(secretWord, lettersGuessed):
            print("Congratulations, you won!")
            return
    
    print("Sorry, you ran out of guesses. The word was " + secretWord)
    
        
    
            
                
            
            





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
#secretWord = "apple"
hangman(secretWord)
