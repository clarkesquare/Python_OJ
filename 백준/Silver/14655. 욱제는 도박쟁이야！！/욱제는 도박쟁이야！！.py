answer = 0
temp = 0
n = int(input())

for _ in range(2):
    numbers = map(int, input().split())
    temp = 0
    for i in numbers:
        temp += abs(i)
    
    answer += temp

print(answer)