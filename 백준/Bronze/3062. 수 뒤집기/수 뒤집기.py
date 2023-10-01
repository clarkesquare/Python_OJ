for _ in range(int(input())):
    number = int(input())
    number = number + int(str(number)[::-1])
    print('YES' if str(number) == str(number)[::-1] else 'NO')