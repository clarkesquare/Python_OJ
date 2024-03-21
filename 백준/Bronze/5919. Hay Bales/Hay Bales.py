bales = []
answer = 0

n = int(input())
for _ in range(n):
    bales.append(int(input()))

for i in bales:
    answer += abs(i - (sum(bales)//len(bales)))

print(answer//2)