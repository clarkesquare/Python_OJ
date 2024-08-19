import sys

input = sys.stdin.readline
pattern = {}
tmp = []
lyrics = ""
animal = ""

for _ in range(int(input())):
    lyrics = input().split()
    while True:
        animal = input().strip()
        if animal != "what does the fox say?":
            tmp = animal.split()
            if tmp[2] not in pattern:
                pattern[tmp[2]] = ""
        
        else:
            break

    for i in lyrics:
        if i not in pattern:
            print(i, end=" ")