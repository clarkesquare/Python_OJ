n, m = map(int, input().split())
streets = []
start, end = [], []

for _ in range(n):
    streets.append(list(map(int, input().split())))

for i in range(n):
    if start != [] and end != []:
        break

    if 1 in streets[i]:
        for j in range(m):
            if streets[i][j] == 1:
                if start == []:
                    start = [i, j]
                else:
                    end = [i, j]

print(abs(end[0] - start[0] + abs(end[1] - start[1])))