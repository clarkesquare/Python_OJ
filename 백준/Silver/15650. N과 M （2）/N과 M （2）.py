from itertools import combinations as comb

n, m = map(int, input().split())
numbers = list(range(1, n+1))
perm = list(comb(numbers, m))

for i in perm:
    print(*i)