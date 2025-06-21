candidates = {}
score = {}
chk = []

for _ in range(int(input())):
    name = input()
    party = input()
    candidates[name] = party
    score[name] = 0

for _ in range(int(input())):
    name = input()
    if name in score:
        score[name] += 1

chk = sorted(list(score.items()), key=lambda x:x[1], reverse=True)

if chk[0][1] > chk[1][1]:
    print(candidates[chk[0][0]])

else:
    print('tie')