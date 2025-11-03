import sys

input = sys.stdin.readline
a, b = input().split()
check = {}

for _ in range(int(a)):
    word = input().strip('\n')
    if word not in check:
        check[word] = None

if b == 'Y':
    print(len(check))

elif b == 'F':
    print(len(check) // 2)

else:
    print(len(check) // 3)