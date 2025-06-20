x, k = map(int, input().split())
numbers = list(map(int, input().split()))
second = {}
answer = x ** 2

for i in range(x, x*2):
    if numbers[i] not in second:
        second[numbers[i]] = 1
    
    else:
        second[numbers[i]] += 1

for i in range(x):
    if numbers[i] in second:
        answer -= second[numbers[i]]

print(answer)