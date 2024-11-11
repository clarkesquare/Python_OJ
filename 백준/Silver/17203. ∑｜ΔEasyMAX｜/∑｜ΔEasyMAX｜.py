n, m = map(int, input().split())
pattern = list(map(int, input().split()))
answer = 0

for _ in range(m):
    a, b = map(int, input().split())
    answer = 0
    for i in range(a, b):
        answer += abs(pattern[i] - pattern[i-1])
    
    print(answer)