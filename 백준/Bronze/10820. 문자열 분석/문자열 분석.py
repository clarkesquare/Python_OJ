import sys

while True:
    words = sys.stdin.readline().rstrip('\n')

    if not words:
        break

    A, B, C, D = 0, 0, 0, 0
    for i in words:
        if i.islower():
            A += 1
        elif i.isupper():
            B += 1
        elif i.isnumeric and i != ' ':
            C += 1
        elif i == ' ':
            D += 1

    print(A, B, C, D)