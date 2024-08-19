import sys

input = sys.stdin.readline

word = ""
tmp = ()
dictionary = {}

while True:
    word = input().strip()
    if word != "XXXXXX":
        tmp = tuple(sorted(word))
        if tmp not in dictionary:
            dictionary[tuple(sorted(word))] = [word]
        
        else:
            dictionary[tmp].append(word)
    
    else:
        break

while True:
    word = input().strip()
    if word != "XXXXXX":
        tmp = tuple(sorted(word))
        if tmp in dictionary:
            print(*sorted(dictionary[tmp]), sep="\n")
            
        else:
            print("NOT A VALID WORD")

        print("******")

    else:
        break