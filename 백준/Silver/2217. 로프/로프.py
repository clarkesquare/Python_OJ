n = int(input())
ropes = []
for _ in range(n):
    ropes.append(int(input()))

ropes.sort(reverse=True)
answer = []

for j in range(n):
    answer.append(ropes[j] * (j+1))

print(max(answer))