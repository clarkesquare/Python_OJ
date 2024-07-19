a, b = map(int, input().split())
pattern = []
tmp = []

for _ in range(b):
    tmp = list(input().split())
    tmp[0], tmp[1] = int(tmp[0]), int(tmp[1])
    pattern.append(tmp)

pattern.sort(key = lambda x:x[0])
pattern.sort(key = lambda x:x[1])

for i in pattern:
    print(i[2], end="")