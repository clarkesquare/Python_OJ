pattern = []
temp = 0
answer = []

for cnt in range(1, int(input())+1):
    a, b = map(int, input().split())
    pattern = []
    answer = []
    for _ in range(a):
        pattern.append(input())
    
    pattern = list(map(list, zip(*pattern)))
    for i in range(b):
        if "X" not in pattern[i]:
            answer.append("N")
        else:
            temp = 0
            for j in pattern[i]:
                if j == "H":
                    temp += 3
                elif j == "S":
                    temp += 1
                else:
                    answer.append(str(temp))
                    break

    print(f"Data Set {cnt}:")
    print(*answer)
    print()