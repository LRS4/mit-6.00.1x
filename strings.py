# print longest substring in alphabetical order
s = "azcbobobegghakl"
longest = s[0]
current = s[0]
for c in s[1:]:
    if c >= current[-1]:
        current += c
        if len(current) > len(longest):
            longest = current
    else:
        current = c
print("Longest substring in alphabetical order is: " + longest)

# replace and strip
animals = "a cat, dog, mouse, horse, lion and elephant"    
animals = animals.strip("a").replace("and", ",").replace(" ", "")  

# split to and join from array 
animals = animals.split(",")
print(animals)
print(", ".join(animals))

# isX
password = "test123"
print(password.isalpha())
print(password.isalnum())

# copy paste
import pyperclip
pyperclip.copy('Hello world!')
pyperclip.paste()