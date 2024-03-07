teams = []
answer1 = ''
answer2 = ''

for _ in range(3):
    a, b, c = input().split()
    a, b, c = int(a), int(b) % 100, c[0]
    teams.append([a, b, c])

teams.sort(key = lambda x:x[1])
for i in teams:
    answer1 += str(i[1])

print(answer1)

teams.sort(key = lambda x:x[0], reverse=True)
for j in teams:
    answer2 += j[2]

print(answer2)