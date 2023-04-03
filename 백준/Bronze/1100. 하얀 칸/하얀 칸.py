lane = [input() for _ in range(8)]
count = 0

for x in range(8):
    for y in range(8):
        if x % 2 == y % 2 and lane[x][y] == 'F':
            count += 1

print(count)