import sys

input = sys.stdin.readline
bio = {}
test = []
answer = [0, 0]

for _ in range(int(input())):
    word = input().strip()
    if word not in bio:
        bio[word] = 1
    else:
        bio[word] += 1

test = list(bio.items())
test.sort(key = lambda x:x[1], reverse=True)

answer[0] = test[0][1]
for i in range(1, len(test)):
    answer[1] += test[i][1]

print(test[0][0] if answer[0] > answer[1] else "NONE")