n = int(input())
numbers = list(map(int, input().split()))
answer = 0

numbers.sort()
numbers.append(numbers[0])

for i in range(1, n+1):
    answer += abs(numbers[i] - numbers[i-1])

print(answer)