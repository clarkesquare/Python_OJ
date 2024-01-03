word = input()
n = int(input())

if word == word[::-1]:
    print('YES')
else:
    print('NO')