n = int(input())
scores = list(map(int, input().split()))
x, y = map(int, input().split())
answer = 0

for i in scores:
    if i >= y:
        answer += 1

print(((n * x)//100), answer)