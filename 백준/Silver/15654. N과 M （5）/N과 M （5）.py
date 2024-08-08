from itertools import permutations as perm

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
numbers = list(perm(numbers, m))

for i in numbers:
    print(*i)