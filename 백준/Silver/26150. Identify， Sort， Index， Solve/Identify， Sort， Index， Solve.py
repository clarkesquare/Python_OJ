pattern = []
answer = ''

for _ in range(int(input())):
    datas = list(input().split())
    datas[1], datas[2] = int(datas[1]), int(datas[2])
    pattern.append(datas)

pattern = sorted(pattern, key=lambda x:x[1])

for i in pattern:
    n = i[2] - 1
    answer += i[0][n].upper()

print(answer)