number, n = 0, 0
temp = []

while len(temp) <= 1000:
    n += 1
    for _ in range(n):
        temp.append(n)

n, m = map(int, input().split())

print(sum(temp[n-1:m]))