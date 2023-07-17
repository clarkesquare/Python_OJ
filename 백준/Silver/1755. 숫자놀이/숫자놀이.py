words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

n, m = map(int, input().split())
numbers = list(map(str, range(n, m+1)))
answer = []
temp = ''

for i in numbers:
    temp = ''
    for j in i:
        temp += words[int(j)]
    answer.append([temp, int(i)])

answer.sort(key=lambda x:x[0])

cnt = 0
for i in range(len(answer)):
    cnt += 1
    if cnt != 10:
        print(answer[i][1], end=' ')
    else:
        print(answer[i][1])
        cnt = 0