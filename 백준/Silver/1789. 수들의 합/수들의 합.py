n = int(input())
answer = 0
temp = 0

while temp <= n:
    answer += 1
    temp += answer

print(answer-1)