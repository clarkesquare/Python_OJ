import sys

input = sys.stdin.readlines

pattern = {}
word = ""

tmp = input()
for i in tmp:
    word = i.strip("\n")
    if " " in word:
        n, m = word.split()
        pattern[m] = n
    
    elif word == "":
        pass

    else:
        if word in pattern:
            print(pattern[word])
        
        else:
            print("eh")