array = []
max, x, y = 0, 1, 1

for _ in range(9):
    array.append(list(map(int, input().split())))

for i in range(9):
    for j in range(9):
        if array[i][j] > max:
            max, x, y = array[i][j], i+1, j+1

print(max)
print(x, y)