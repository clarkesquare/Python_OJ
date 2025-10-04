M = list(map(int, input().split()))
answer = 0

for _ in range(int(input())):
    b, l, s = input().split()
    b = int(b)
    l = float(l)
    s = int(s)
    if l >= 2.0 and s >= 17:
        answer += M[b]

print(answer)