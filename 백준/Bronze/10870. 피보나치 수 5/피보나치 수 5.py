n = int(input())
a, b = 0, 1
answer = 1

if n == 0:
    answer = 0
else:
    for i in range(n-1):
        answer = a + b
        a, b = b, answer

print(answer)