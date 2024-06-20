n, m = input().split()
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(int(n), int(m)+1):
    for j in str(i):
        cnt[numbers.index(int(j))] += 1

print(*cnt)