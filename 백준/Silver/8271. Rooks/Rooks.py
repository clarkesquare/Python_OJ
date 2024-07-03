n = int(input())
pattern = []
answer = [0] * n

for i in range(n):
    tmp = list(input())
    pattern.append(tmp)
    if "W" in tmp:
        pattern[i][pattern[i].index("W")] = "W"
        answer[pattern[i].index("W")] = 1

for j in range(n):
    if "W" not in pattern[j]:
        for k in range(n):
            if answer[k] == 0:
                pattern[j][k] = "W"
                answer[k] = 1
                break

for l in pattern:
    print(*l, sep="")