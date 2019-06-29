# using functions

# import a function from helpers.py (another file in this directory)
from helpers import add
import math

def main():
    # add two numbers using imported function
    print(add(10,20))
    
    # create single line functions using lambda
    print((lambda x: (x * 5) - 5) (10))
    print((lambda x, y: x + y) (10,20))

    # check if s is in string using function
    print(isIn("y", "bcdefghijklmnopqrstuvwxy"))


def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    mid = len(aStr)//2
    if len(aStr) == 1:
      return aStr == char
    # bisection search using recursion
    if aStr[mid] == char:
        return True
    elif char < aStr[mid]:
        return isIn(char, aStr[:mid])
    else :
        return isIn(char, aStr[mid:])
    
if __name__ == "__main__":
    main()
