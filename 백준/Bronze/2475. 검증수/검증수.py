answer = 0

numbers = list(map(int, input().split()))

for i in numbers:
    answer += i ** 2

print(answer%10)