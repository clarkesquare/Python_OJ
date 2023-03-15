list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))
a = 0
b = 0
w = 0

for i in range(len(list_a)):
    if list_a[i] > list_b[i]:
        a += 3
        w = 'A'
    elif list_a[i] < list_b[i]:
        b += 3
        w = 'B'
    else:
        a += 1
        b += 1

print(a, b)

if a > b or (a == b and w == 'A'):
    print('A')
elif a < b or (a == b and w == 'B'):
    print('B')
else:
    print('D')