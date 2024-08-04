n, m = map(int, input().split())
passwords = {}

for _ in range(n):
    a, b = input().split()
    passwords[a] = b

for _ in range(m):
    print(passwords[input()])