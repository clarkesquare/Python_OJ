pattern = {"a": "4", "e": "3", "i": "1", "o": "0", "s": "5"}
word = list(input())

for i in word:
    if i in pattern:
        print(pattern[i], end="")
    
    else:
        print(i, end="")