def fact(x):
    """
    Find the factorial of any number
    """ 
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)

print("Factorial of 4 is " + str(fact(4)))

def fib(x):
    """
    Find the Fibonacci of x
    """
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)

for i in range(15):
    print(fib(i))

sentence = "Able was I, ere I saw Elba"
def isPalandrome(sentence):
    """ 
    Determine if a sentence is a palandrome
    """
    sentence = sentence.lower().replace(" ", "").replace(",", "")
    if len(sentence) <= 1:
        return True
    else:
        return sentence[0] == sentence[-1] and isPalandrome(sentence[1:-1])

print(isPalandrome(sentence))