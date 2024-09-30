import sys

input = sys.stdin.readline

pattern = []

for _ in range(int(input())):
    word = input().strip("\n").split()
    if word[0] == "push":
        pattern.append(word[1])
    
    else:
        if word[0] == "top":
            if len(pattern) != 0:
                print(pattern[-1])
            
            else:
                print("-1")
        
        elif word[0] == "pop":
            if len(pattern) != 0:
                print(pattern[-1])
                pattern.pop()
            
            else:
                print("-1")
        
        elif word[0] == "size":
            print(len(pattern))
        
        elif word[0] == "empty":
            if len(pattern) == 0:
                print("1")
            
            else:
                print("0")