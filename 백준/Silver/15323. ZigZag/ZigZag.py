from string import ascii_lowercase
import sys

input = sys.stdin.readline
alphabets = {}
for i in ascii_lowercase:
    alphabets[i] = 0

pattern = {}
n, m = map(int, input().split())
for _ in range(n):
    word = input().strip("\n")
    if word[0] not in pattern:
        pattern[word[0]] = [word]
    
    else:
        pattern[word[0]].append(word)

for i in pattern:
    pattern[i].sort()

for _ in range(m):
    word = input().strip("\n")
    print(pattern[word][alphabets[word] % len(pattern[word])])
    alphabets[word] += 1