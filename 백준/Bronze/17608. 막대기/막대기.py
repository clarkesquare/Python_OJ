import sys

input = sys.stdin.readline

n = int(input())
numbers = []
answer = 1

for _ in range(n):
    numbers.append(int(input()))

maximum_number = numbers[-1]
for i in numbers[-2::-1]:
    if i > maximum_number:
        maximum_number = i
        answer += 1

print(answer)