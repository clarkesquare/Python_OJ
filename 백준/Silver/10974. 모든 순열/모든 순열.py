from itertools import permutations as perm

n = int(input())
numbers = list(range(1, n+1))

numbers = perm(numbers, n)
for i in numbers:
    print(*i)