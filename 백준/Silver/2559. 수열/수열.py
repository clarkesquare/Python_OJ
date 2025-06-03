n, k = map(int, input().split())
tmp = 0
numbers = [0]
answer = -100 * 100000

for i in map(int, input().split()):
    tmp += i
    numbers.append(tmp)

for i in range(n-k+1):
    if numbers[i+k] - numbers[i] > answer:
        answer = numbers[i+k] - numbers[i]

print(answer)