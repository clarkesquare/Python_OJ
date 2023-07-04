n = int(input())
pattern = []

for _ in range(n):
    pattern.append(list(map(int, input().split())))

pattern.sort(key=lambda x:x[0])
pattern.sort(key=lambda x:x[1])

for i in pattern:
    print(*i)