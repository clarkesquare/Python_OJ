n = int(input())

for i in range(n):
    answer = ''
    word = list(map(str, input().split()))
    for i in word:
        answer += i[-1::-1]
        answer += ' '
    answer = answer[:-1:]
    print(answer)