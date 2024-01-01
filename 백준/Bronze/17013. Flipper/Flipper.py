grid = [[1, 2], [3, 4]]
pattern = input()
for i in pattern:
    if i == 'H':
        grid[0], grid[1] = grid[1], grid[0]
    else:
        grid[0][0], grid[0][1], grid[1][0], grid[1][1] = grid[0][1], grid[0][0], grid[1][1], grid[1][0]

for j in grid:
    print(*j)