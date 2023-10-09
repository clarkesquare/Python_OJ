n, m = map(int, input().split())
name = []

for _ in range(n):
    name.append(input())

name.sort()
print(name[m-1])