n = int(input())

for _ in range(n):
    n, m = input().split()
    if sorted(n) == sorted(m):
        print(n, '&', m, 'are anagrams.')
    else:
        print(n, '&', m, 'are NOT anagrams.')