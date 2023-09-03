n, m = map(int, input().split())
array = list(map(int, input().split(',')))
answer = ''

for _ in range(m):
    temp = []
    for i in range(1, len(array)):
        temp.append(array[i]-array[i-1])
    array = temp

for j in array:
    answer += str(j) + ','

print(answer[:-1:])