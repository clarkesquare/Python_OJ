while True:
    number = list(map(int, input()))
    if number != [0]:
        cnt = 0
        while True:
            if number == number[::-1]:
                print(cnt)
                break

            else:
                number[-1] += 1
                cnt += 1
                for i in range(1, len(number)+1):
                    if number[i * -1] == 10:
                        number[i * -1 - 1], number[i * -1] = number[i * -1 - 1] + 1, 0

                    else:
                        break

    else:
        break