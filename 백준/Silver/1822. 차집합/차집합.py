n, m = map(int, input().split())
n = set(map(int, input().split()))
m = set(map(int, input().split()))
answer = list(n-m)

print(len(answer))
if len(answer) != 0:
    answer.sort()
    print(*answer)