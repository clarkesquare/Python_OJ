n = input()
answer = 0

for _ in range(len(n)):
    n = n[-1] + n[:-1:]
    answer += int(n)

print(answer)