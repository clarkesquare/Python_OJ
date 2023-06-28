S = []

for i in range(int(input())):
    S.append(list(input().split()))
    S[i][1], S[i][2], S[i][3] = int(S[i][1]), int(S[i][2]), int(S[i][3])

S.sort(key = lambda x: (x[3], x[2], x[1]))
print(S[-1][0])
print(S[0][0])