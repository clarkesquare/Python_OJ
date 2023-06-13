n = int(input())

for i in range(1, n+1):
    words = list(input().split())
    answer = ''
    for j in words[-1::-1]:
        answer += j
        answer += ' '
    answer = answer[:-1:]
    print('Case #'+str(i)+':', answer)