n = int(input())
numbers = map(int, input().split())
answer = 0

for i in numbers:
    if str(i) == str(i)[::-1]:
        answer += i

print(answer)