import time

a, k = map(int, input().split())

chk = [k]
tmp = []
numbers = {}
answer = 0

while True:
    answer += 1
    tmp = []
    for i in chk:
        if i - 1 == a:
            tmp = []
            break

        elif i / 2 == a:
            tmp = []
            break
        
        else:
            if i - 1 not in numbers:
                tmp.append(i-1)
                numbers[i-1] = None

            if (int(i / 2) == i / 2) and ((i // 2) > a) and ((i // 2) not in numbers):
                tmp.append(i // 2)
                numbers[i//2] = None

    chk = tmp
    if len(tmp) == 0:
        break

print(answer)