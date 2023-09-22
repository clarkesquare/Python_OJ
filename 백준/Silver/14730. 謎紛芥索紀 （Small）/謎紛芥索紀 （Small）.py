answer = 0
for _ in range(int(input())):
    n, m = map(int, input().split())
    answer += n*m

print(answer)