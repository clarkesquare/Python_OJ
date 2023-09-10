answer, temp1, temp2 = 0, 0, 0

for _ in range(int(input())):
    n, m = input().split()
    temp1, n = n, n.replace(m, '')
    temp2 = (len(temp1) - len(n)) // len(m)
    answer = len(n) + temp2
    print(answer)