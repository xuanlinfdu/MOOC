# 6.00 Problem Set 3
# 
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
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print len(wordlist), "words loaded."
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
    count = 0
    for i in secretWord:
        if i in lettersGuessed:
            count += 1
    if count == len(secretWord):
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    word_printed = []
    for i in secretWord:
        if i in lettersGuessed:
            word_printed.append(i)
        else:
            word_printed.append('_ ')
    return ''.join(word_printed)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    letteroriginal = list(string.ascii_lowercase)
    for i in lettersGuessed:
        if i in letteroriginal:
            letteroriginal.remove(i)
    return ''.join(letteroriginal)
    

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
#     FILL IN YOUR CODE HERE...
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is', len(secretWord), 'letters long.'
    print '-------------'
    number_remain = 8
    lettersGuessed = []
    while number_remain > 0:
        repeat_status = True
        while repeat_status:
            print 'You have', number_remain, 'guesses left'
            print 'Available Letters:', getAvailableLetters(lettersGuessed)
            letter_guess = raw_input("Please guess a letter: ").lower()
            if letter_guess in lettersGuessed:
                print 'Oops! You\'ve already guessed that letter:', getGuessedWord(secretWord, lettersGuessed)
            else:
                repeat_status = False
                lettersGuessed.append(letter_guess)
                if letter_guess in secretWord:
                    print 'Good guess:', getGuessedWord(secretWord, lettersGuessed)
                else:
                    print 'Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed)
                    number_remain -= 1
            print '------------'
        if not ('_' in getGuessedWord(secretWord, lettersGuessed)):
            print 'Congratulations, you won!'
            break
    if number_remain == 0 and ('_' in getGuessedWord(secretWord, lettersGuessed)):
        print 'Sorry, you ran out of guesses. The word was', secretWord
            
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)