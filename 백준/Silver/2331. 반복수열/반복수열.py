tmp = {}
cnt = 0
number = 0

a, p = input().split()
answer = a
p = int(p)
while True:
    cnt += 1
    number = 0
    for i in range(len(answer)):
        number += int(answer[i]) ** p

    if answer in tmp:
        break

    else:
        tmp[answer] = cnt
        answer = str(number)

print(tmp[answer] - 1)