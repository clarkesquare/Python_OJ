import sys
input = sys.stdin.readline
factorial, answer = 1, 0

for i in range(1, int(input())+1):
    factorial *= i

factorial = str(factorial)[::-1]

for i in range(len(factorial)):
    if factorial[i] == '0':
        answer += 1
    else:
        break

print(answer)