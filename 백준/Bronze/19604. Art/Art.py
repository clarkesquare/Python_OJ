minimum = [100, 100]
maximum = [0, 0]

for _ in range(int(input())):
    a, b = map(int, input().split(","))
    if minimum[0] > a:
        minimum[0] = a
    if minimum[1] > b:
        minimum[1] = b
    
    if maximum[0] < a:
        maximum[0] = a
    if maximum[1] < b:
        maximum[1] = b

minimum[0] -= 1
minimum[1] -= 1
maximum[0] += 1
maximum[1] += 1

print(*minimum, sep=",")
print(*maximum, sep=",")