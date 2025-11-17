answer = [0, '']
maximum = 0

for _ in range(int(input())):
    name = input()
    k, m = map(int, input().split())
    tmp = 0
    while k <= m:
        m -= k
        m += 2
        tmp += 1
    
    answer[0] += tmp
    if maximum < tmp:
        maximum = tmp
        answer[1] = name

print(*answer, sep='\n')