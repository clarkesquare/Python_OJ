n, m = map(int, input().split())
numbers = [0]
num = 0
answer = 0
n += 1

for i in list(map(int, input().split())):
    num += i
    numbers.append(num)

for i in range(n-1):
    for j in range(i, n):
        if numbers[j] - numbers[i] == m:
            answer += 1

print(answer)