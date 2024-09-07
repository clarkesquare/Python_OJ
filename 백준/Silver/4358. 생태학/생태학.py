import sys

input = sys.stdin.readlines
pattern = {}
trees = input()
answer = []
cnt = len(trees)

for i in trees:
    tmp = i[:-1]
    if tmp not in pattern:
        pattern[tmp] = 1
    
    else:
        pattern[tmp] += 1

for k, v in pattern.items():
    answer.append([k, v/cnt * 100])

answer.sort(key=lambda x:x[0])

for k, v in answer:
    print(f"{k} {v:.4f}")