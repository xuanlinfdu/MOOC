import pylab
import string
# You may have to change this path
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    prop_vowel = []
    for word in wordList:
        vowel_count = 0
        word_temp = word.lower()
        for letter in word_temp:
            if letter in 'aeiou':
                vowel_count += 1
        prop_vowel.append(float(vowel_count)/float(len(word_temp)))
    pylab.figure()
    pylab.hist(prop_vowel, bins = numBins)
    pylab.show()
            

if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
