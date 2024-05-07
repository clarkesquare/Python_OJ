n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
answer = 0

for i in a:
    if i in b:
        answer += 1

print(answer)