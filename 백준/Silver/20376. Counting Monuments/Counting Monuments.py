import sys

input = sys.stdin.readlines
areas = {}

word = input()
for i in word:
    i = i[11:-1]
    if i not in areas:
        areas[i] = ""

print(len(areas))