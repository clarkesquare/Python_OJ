pattern = ''
answer = 0
for _ in range(int(input())):
    pattern = input()
    answer = 0
    for i in range(len(pattern)):
        if i % 2 == 0:
            if len(str(int(pattern[i]) * 2)) >= 2:
                answer += int(str(int(pattern[i]) * 2)[0]) + int(str(int(pattern[i]) * 2)[1])
            else:
                answer += int(pattern[i]) * 2

        else:
            answer += int(pattern[i])

    print("T" if answer % 10 == 0 else "F")