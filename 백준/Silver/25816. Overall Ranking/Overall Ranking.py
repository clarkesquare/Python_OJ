import sys

input = sys.stdin.readline
pattern = {}
answer = []

for i in range(1, int(input())+1):
    word = input().strip()
    if word not in pattern:
        pattern[word] = [i]
    
    else:
        pattern[word].append(i)

for k, v in pattern.items():
    answer.append([k, v])

for i in range(len(answer)):
    answer[i][1] = (sum(answer[i][1])) / len(answer[i][1])

answer.sort(key= lambda x:x[1])
for j in answer:
    print(j[0])