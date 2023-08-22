name = []
for _ in range(int(input())):
    name.append(input())

if name == sorted(name):
    print('INCREASING')
elif name == sorted(name, reverse=True):
    print('DECREASING')
else:
    print('NEITHER')