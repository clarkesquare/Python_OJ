n = input()
answer = 0

for _ in range(int(input())):
    pattern = input() * 2
    if n in pattern:
        answer += 1

print(answer)