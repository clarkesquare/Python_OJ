answer, temp, cnt = 0, 0, 0

for _ in range(int(input())):
    n, m = input().split()
    temp, n = n, n.replace(m, '')
    cnt = (len(temp) - len(n)) // len(m)
    answer = len(n) + cnt
    print(answer)