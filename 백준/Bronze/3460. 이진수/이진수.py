n = int(input())

for _ in range(n):
    answer = ''
    position = []
    number = int(input())
    while number // 2 != 0:
        answer += str(number % 2)
        number //= 2
    answer += str(number)

    for i in range(len(answer)):
        if answer[i] == '1':
            position.append(i)

    print(*position)