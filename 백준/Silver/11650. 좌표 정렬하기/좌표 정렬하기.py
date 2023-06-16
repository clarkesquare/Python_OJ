n = int(input())

dots = []

for _ in range(n):
    dots.append(list(map(int, input().split())))

dots.sort()

for i in dots:
    print(i[0], i[1])