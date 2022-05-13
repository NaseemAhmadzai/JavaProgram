from readWords import fixWord, load_words
filename =  input("Type in the filename to load: ")
wordList = load_words(filename) #Load the words from the file.
def freqDictionary(aList):
    '''Generates a frequency dictionary of the contents in
aList.
params: aList - a list of words.
returns: a dictionary with each unique word and how often it is
found in the text.'''
    
    wordFreqDict = {} #word frequency dictionary.
    #General algorithm for this function:
    for word in aList:
        word = fixWord(word.lower())
        if word == "":
            continue
        wordFreqDict[word] = wordFreqDict.get(word, 0) + 1
#         if word in wordFreqDict: #Make sure the key exists.
#             wordFreqDict[word] += 1
#         else: #Word isn't in the dictionary - yet!
#             wordFreqDict[word] = 1
    return wordFreqDict



d = freqDictionary(wordList)
print(d)
