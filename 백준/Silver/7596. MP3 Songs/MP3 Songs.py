pattern = []
i = 0

while True:
    n = int(input())
    if n != 0:
        i += 1
        pattern = []
        for _ in range(n):
            pattern.append(input())
        
        pattern.sort()
        print(i)
        print(*pattern, sep="\n")

    else:
        break