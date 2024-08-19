import sys

input = sys.stdin.readline
word = ""
tmp = ""
dictionary = {}

for _ in range(int(input())):
    word = input().strip()
    tmp = tuple(sorted(word))
    if tmp not in dictionary:
        dictionary[tmp] = word

dictionary = list(dictionary.items())

for i in dictionary:
    print(i[1])