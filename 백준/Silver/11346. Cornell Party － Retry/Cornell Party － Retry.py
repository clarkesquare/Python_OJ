import sys
input = sys.stdin.readline

data = {}
tmp = []

for _ in range(int(input())):
    input()
    n, m = map(int, input().split())
    data = {}
    tmp = input().strip("\n").split()
    for i in tmp:
        if i not in data:
            data[i] = ""
    
    tmp = input().strip("\n").split()
    for i in tmp:
        if i not in data:
            data[i] = ""
    
    print(len(data))