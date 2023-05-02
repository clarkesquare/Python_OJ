n, m = map(str, input().split())
min, max = 0, 0

min = int(n.replace('6', '5')) + int(m.replace('6', '5'))
max = int(n.replace('5', '6')) + int(m.replace('5', '6'))

print(min, max)