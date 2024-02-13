n = int(input())

for _ in range(n):
    name = input()
    if len(name) >= 6 and len(name) <= 9:
        print('yes')
    else:
        print('no')