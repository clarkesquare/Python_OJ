for _ in range(int(input())):
    number = input()
    temp = str(int(number) ** 2)
    print('YES' if number == temp[(len(temp)-len(number))::] else 'NO')