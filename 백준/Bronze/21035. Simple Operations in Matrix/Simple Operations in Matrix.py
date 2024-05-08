matrices = []
pattern = ["", "", ""]
temp = []

n, m = map(int, input().split())
for _ in range(n):
    matrices.append(list(map(int,input().split())))

for _ in range(int(input())):
    pattern = list(input().split())
    pattern[1], pattern[2] = int(pattern[1]) - 1, int(pattern[2])
    if pattern[0] == "row":
        for i in range(m):
            matrices[pattern[1]][i] += pattern[2]
    
    else:
        for j in range(n):
            matrices[j][pattern[1]] += pattern[2]

for k in matrices:
    temp += k

print(sum(temp), min(temp), max(temp))