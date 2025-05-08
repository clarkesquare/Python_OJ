n, m = input().split()
tmp = 0
answer = 0

for i in n:
    tmp += int(i)

for j in m:
    answer += tmp * int(j)

print(answer)