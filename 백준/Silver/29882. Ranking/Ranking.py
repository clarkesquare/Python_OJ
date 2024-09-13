import sys

input = sys.stdin.readline
pattern = {}
answer = {}
answer_list = []

for _ in range(int(input())):
    word = input().strip("\n").split()
    tmp = word[0] + " " + word[1]
    tmp_number = int(word[-1])
    if tmp not in pattern:
        pattern[tmp] = tmp_number
    
    else:
        if pattern[tmp] < tmp_number:
            pattern[tmp] = tmp_number

for i in pattern:
    word = i.split()
    if word[0] not in answer:
        answer[word[0]] = pattern[i]
    
    else:
        answer[word[0]] += pattern[i]

for k, v in answer.items():
    answer_list.append([k, v])

answer_list.sort(key= lambda x:x[0])
answer_list.sort(key= lambda x:x[1], reverse=True)
for j in answer_list:
    print(*j)