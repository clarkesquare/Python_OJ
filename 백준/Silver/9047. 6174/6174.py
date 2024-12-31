for _ in range(int(input())):
    number = input()
    after = ''
    cnt = 0
    while True:
        after = ''
        number = str(number)
        if len(number) < 4:
            number = '0' * (4 - len(number)) + number

        after = int(''.join(sorted(number, reverse=True))) - int(''.join(sorted(number)))
        if number == str(after):
            print(cnt)
            break

        cnt += 1
        number = after