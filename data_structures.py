# data structures

# lists - can be changed
my_list = [1, 2, 3, 4, 5]
print(my_list)
print(3 in my_list)

# list comprehensions (can generate lists using rules)
odd_nums = [i + 1 for i in range(10) if i % 2 == 0]
print(odd_nums)

# tuples - like lists but cannot be changed
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print("my tuple position zero is {0}".format(my_tuple[0]))
print(f"my tuple position one is {my_tuple[1]}")

# sets - like lists but no duplicate entries or indexing, use add not append
my_set = set([1, 2, 3, 4, 5, 5])
print(my_set)

# dictionaries - key value pairs (hashtable)
my_dict = {
    "a" : 1,
    "b" : 2,
    "c" : 3,
    "d" : 4,
    "e" : 5
}
print(my_dict["d"])
print("c" in my_dict)

# count values within dictionaries
def how_many(aDict):
    ans = 0
    for v in aDict.values():
        ans += len(v)
    return ans

hashtable = {
    "a" : ["hello", "goodbye"],
    "b" : ["hi", "bye"],
    "c" : ["hallo", "bis spater"],
    "d" : ["salut", "a bientot"]
}

print(how_many(hashtable))