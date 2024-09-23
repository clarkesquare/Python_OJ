numbers = input()
cnt = 1
answer = 0
tmp = ""

for i in numbers:
    if i == "-" or i == "+":
        answer += int(tmp) * cnt
        tmp = ""
        if i == "-":
            cnt = -1
    
    else:
        tmp += i

if len(tmp) != 0:
    answer += int(tmp) * cnt

print(answer)