words = input().split()
answer = 'yes'
temp = []

for i in words:
    if i in temp:
        answer = 'no'
        break
    else:
        temp.append(i)

print(answer)