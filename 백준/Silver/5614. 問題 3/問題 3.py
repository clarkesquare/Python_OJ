import sys

input = sys.stdin.readline
pattern = {}
answer = []

for _ in range(int(input())):
    a, b = input().strip().split()
    b = int(b)
    if a not in pattern:
        pattern[a] = b

    else:
        pattern[a] += b

for k, v in pattern.items():
    answer.append([k, v, len(k)])

answer.sort(key= lambda x:x[1], reverse=True)
answer.sort(key= lambda x:x[0])
answer.sort(key= lambda x:x[2])

for i in answer:
    print(*i[:2])