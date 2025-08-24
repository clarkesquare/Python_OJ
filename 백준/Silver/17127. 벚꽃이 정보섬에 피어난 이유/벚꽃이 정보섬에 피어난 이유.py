import math

n = int(input())
numbers = list(map(int, input().split()))
tmp = 0
answer = 0

for i in range(n-3):
    for j in range(i+1, n-2):
        for k in range(j+1, n-1):
            tmp = math.prod(numbers[:i+1]) + math.prod(numbers[i+1:j+1]) + math.prod(numbers[j+1:k+1]) + math.prod(numbers[k+1:])
            if answer < tmp:
                answer = tmp

print(answer)