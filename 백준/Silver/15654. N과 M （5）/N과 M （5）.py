from itertools import permutations as perm

n, m = map(int, input().split())
numbers = map(int, input().split())
numbers = list(perm(numbers, m))
numbers.sort()

for i in numbers:
    print(*i)