n = int(input())
numbers = list(map(int, input().split()))
answer = 1 + 1 + numbers[0] * 4

for i in range(1, n):
    answer += 1 + 1 + numbers[i] * 4
    answer -= min(numbers[i-1], numbers[i]) * 2

print(answer)