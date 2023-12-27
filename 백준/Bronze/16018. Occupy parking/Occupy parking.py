pattern = []
answer = 0
n = int(input())

for _ in range(2):
    pattern.append(input())

for i in range(n):
    if pattern[0][i] == 'C' and pattern[0][i] == pattern[1][i]:
        answer += 1

print(answer)