r, c = map(int, input().split())

position = []
position.append(["x"] * (c + 2))
for _ in range(r):
    position.append(["x"] + ["*"] * (c) + ["x"])

position.append(["x"] * (c + 2))

for _ in range(int(input())):
    a, b = map(int, input().split())
    position[a + 1][b + 1] = "x"

x, y = map(int, input().split())
x += 1
y += 1
position[x][y] = "x"

pattern = list(map(int, input().split()))
while True:
    for i in range(len(pattern)):
        if pattern[i] == 1 and position[x-1][y] != "x":
            while position[x-1][y] != "x":
                x -=1
                position[x][y] = "x"
                    
        elif pattern[i] == 2 and position[x+1][y] != "x":
            while position[x+1][y] != "x":
                x += 1
                position[x][y] = "x"
        
        elif pattern[i] == 3 and position[x][y-1] != "x":
            while position[x][y-1] != "x":
                y -= 1
                position[x][y] = "x"
        
        elif pattern[i] == 4 and position[x][y+1] != "x":
            while position[x][y+1] != "x":
                y += 1
                position[x][y] = "x"
    
    if position[x-1][y] == "x" and position[x+1][y] == "x" and position[x][y-1] == "x" and position[x][y+1] == "x":
        break

print(x-1, y-1)