import string

lettersGuessed = ["a", "b", "t", "z", "c", "s", "q", "y"]

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabet = string.ascii_lowercase
    notGuessed = ""
    for i in range(len(alphabet)):
        if alphabet[i] not in lettersGuessed:
            notGuessed += alphabet[i]
    return notGuessed

print(getAvailableLetters(lettersGuessed))