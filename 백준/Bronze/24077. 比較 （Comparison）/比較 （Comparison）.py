n, m = map(int, input().split())
before = list(map(int, input().split()))
after = list(map(int, input().split()))
answer = 0

for i in before:
    for j in after:
        if i <= j:
            answer += 1

print(answer)