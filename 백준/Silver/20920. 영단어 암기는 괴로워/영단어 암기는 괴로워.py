import sys

input = sys.stdin.readline

n, m = map(int, input().split())
words = {}

for _ in range(n):
    tmp = input().strip("\n")
    if len(tmp) >= m:
        if tmp not in words:
            words[tmp] = 1
        else:
            words[tmp] += 1

words = dict(sorted(words.items(), key= lambda x:x[0]))
words = dict(sorted(words.items(), key= lambda x:len(x[0]), reverse=True))
words = sorted(words.items(), key= lambda x:x[1], reverse=True)

for i in words:
    print(i[0])