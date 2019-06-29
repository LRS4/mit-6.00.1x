# count number of times bob occurs
s = 'obobjbooboboojdmoobobbibobbobobo'

count = 0
i = 0
while i < len(s) - 2:
    if s[i] == "b":
        if s[i+1] == "o":
            if s[i+2] == "b":
                count += 1
    i += 1

print("Number of times bob occurs: " + str(count))


# 6 + 5 + 4 + 3 + 2 + 1
end = 6
x = 0
while end > 0:
    x += end
    end -= 1
print(x)

# or
for i in range(end):
    x += end
    end -= 1
print(x)