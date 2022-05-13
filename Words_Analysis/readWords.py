def fixWord(aword):
    '''Removes the characters listed in charsToRemove from aStr
and returns the "cleaned" string.
Params: aStr - string to remove the bad chars from.
charsToRemove - a string of the characters we don't want.
returns the cleaned string.'''
    
    
    alphas = "abcdefghijklmnopqrstuvwxyz"
    alphas = alphas + str(alphas.upper)
    if len(aword) == 0:
        return ""
    elif (aword[0] in alphas) and (aword[-1] in (alphas + "'-")):
        return aword
    if aword[-1] not in (alphas +"'-"):
        aword = aword[0:-1]
    elif aword[0] not in alphas:
        aword = aword[1:]
    return fixWord(aword) 
    
    
def load_words(fileName):
    """Reads the contents of a text file and separates each word by the space
character.
params: fileName - a string; the file to read from.
Returns a list of all the words in the text file.
    """
    listOfWords = []
    try:
        print("Loading word list from file...")
        # Open the file for reading.
        inFile = open(fileName, 'r')
        
        for line in inFile: #read the lines from the file.
            #split it at the SPACES, remove any non-printing characters.
            wordsInLine = line.strip().split()
            #append it to the list as a tuple.
            listOfWords.extend(wordsInLine)
        inFile.close()
    except FileNotFoundError:
        print("Uh-oh! Couldn't open the file!  ")
        listOfWords = []
    except:
        print("Uh-oh! Something else went wrong! ")
        listOfWords = []
    
    finally: #This block is always executed no matter what.
        print("  ", len(listOfWords), "words loaded.")    
        return listOfWords

