patterns = input().split()
answer = []

for i in patterns:
    if i == "tapioka":
        pass
    elif i == "bubble":
        pass
    else:
        answer.append(i)

if len(answer) >= 1:
    print(*answer)
else:
    print("nothing")