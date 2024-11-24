import sys

input = sys.stdin.readline
answer = []

for _ in range(int(input())):
    word = input().strip("\n").split()
    if len(word) == 1:
        if word[0] == "size":
            print(len(answer))
        
        if word[0] == "empty":
            if len(answer) == 0:
                print(1)
            
            else:
                print(0)
        
        elif word[0] == "front":
            if len(answer) != 0:
                print(answer[0])
            
            else:
                print(-1)
        
        elif word[0] == "back":
            if len(answer) != 0:
                print(answer[-1])
            
            else:
                print(-1)
        
        elif word[0] == "pop_front":
            if len(answer) != 0:
                print(answer.pop(0))

            else:
                print(-1)
        
        elif word[0] == "pop_back":
            if len(answer) != 0:
                print(answer.pop())
            
            else:
                print(-1)
    
    else:
        if word[0] == "push_front":
            answer.insert(0, word[1])
        
        elif word[0] == "push_back":
            answer.append(word[1])