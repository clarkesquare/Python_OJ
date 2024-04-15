lottery = list(range(1, 50))
check = []
temp = []
n = 0

while True:
    n = int(input())
    if n != 0:
        check = []
        for _ in range(n):
            for i in list(map(int, input().split())):
                if i not in check:
                    check.append(i)
            
        check.sort()
        print("Yes" if check == lottery else "No")

    else:
        break