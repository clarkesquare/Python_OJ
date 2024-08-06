n, m = map(int, input().split())
groups = {}

for _ in range(n):
    name = input()
    tmp = []
    for _ in range(int(input())):
        tmp.append(input())

    tmp.sort()
    groups[name] = tmp

for _ in range(m):
    test = input()
    n = int(input())
    if n == 1:
        for i in groups:
            if test in groups[i]:
                print(i)
                break
    
    else:
        print(*groups[test], sep="\n")