from itertools import permutations as per

n, m = map(int, input().split())
numbers = list(range(1, n+1))
perm = list(per(numbers, m))

for i in perm:
    print(*i)