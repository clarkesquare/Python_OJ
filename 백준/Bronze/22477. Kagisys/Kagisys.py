pattern = {}
answer = 0
door = ["Opened by", "Closed by"]

for _ in range(int(input())):
    pattern[input()] = ""

for _ in range(int(input())):
    word = input()
    if word in pattern:
        if answer == 0:
            print(door[0], word)
            answer = 1
        
        else:
            print(door[1], word)
            answer = 0
    
    else:
        print("Unknown", word)