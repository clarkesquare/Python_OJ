n = int(input())

for _ in range(n):
    n, m = map(str, input().split())
    answer = ''
    m = list(m)
    del m[int(n)-1]
    for i in m:
        answer += i
    print(answer)