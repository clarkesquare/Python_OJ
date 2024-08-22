import sys

input = sys.stdin.readline

n, m = map(int, input().split())
notepad = {}
keyword = {}
tmp = ""

for _ in range(n):
    notepad[input().strip()] = ""

for _ in range(m):
    words = input().strip("\n").split(",")
    for i in words:
        if i in notepad and i not in keyword:
            keyword[i] = ""
    
    print(len(notepad) - len(keyword))