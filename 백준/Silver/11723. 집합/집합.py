import sys

input = sys.stdin.readline

answer = {}

for _ in range(int(input())):
    word = input().strip("\n").split()
    if len(word) != 1:
        word[1] = int(word[1])
        if word[0] == "add":
            if word[1] not in answer:
                answer[word[1]] = ""
        
        elif word[0] == "remove":
            if word[1] in answer:
                answer.pop(word[1])
        
        elif word[0] == "check":
            if word[1] in answer:
                print("1")
            
            else:
                print("0")
        
        elif word[0] == "toggle":
            if word[1] in answer:
                answer.pop(word[1])
            
            else:
                answer[word[1]] = ""

    else:
        if word[0] == "all":
            answer = {}
            for i in range(1, 21):
                answer[i] = ""
        
        elif word[0] == "empty":
            answer = {}