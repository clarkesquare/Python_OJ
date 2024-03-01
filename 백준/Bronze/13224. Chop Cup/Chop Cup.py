pattern = input()
answer = [1, 0, 0]

for i in pattern:
    if i == "A":
        answer[0], answer[1] = answer[1], answer[0]
    elif i == "B":
        answer[1], answer[2] = answer[2], answer[1]
    else:
        answer[0], answer[2] = answer[2], answer[0]

print(answer.index(1) + 1)