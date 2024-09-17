answer = []

for i in range(1, 6):
    word = input()
    if "FBI" in word:
        answer.append(i)

answer.sort()
if len(answer) != 0:
    print(*answer)

else:
    print("HE GOT AWAY!")