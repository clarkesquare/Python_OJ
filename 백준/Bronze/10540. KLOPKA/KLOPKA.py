minimum = [100, 100]
maximum = [0, 0]
answer = 0

for _ in range(int(input())):
    a, b = map(int, input().split())
    if a < minimum[0]:
        minimum[0] = a
    if b < minimum[1]:
        minimum[1] = b
    if a > maximum[0]:
        maximum[0] = a
    if b > maximum[1]:
        maximum[1] = b
    
if maximum[0] - minimum[0] > maximum[1] - minimum[1]:
    answer = (maximum[0] - minimum[0]) ** 2
else:
    answer = (maximum[1] - minimum[1]) ** 2

print(answer)