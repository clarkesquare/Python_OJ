n, m = map(int, input().split())
pattern = {}
answer = []

for _ in range(n):
    a = input()
    pattern[a] = 0

for _ in range(m):
    tmp = input()
    if tmp in pattern:
        answer.append(tmp)

answer.sort()
print(len(answer))
print(*answer, sep="\n")