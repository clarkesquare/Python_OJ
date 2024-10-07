pattern = {}
tmp = []
answer = []

for _ in range(int(input())):
    tmp = input().split()[2:]
    for i in tmp:
        if i not in pattern:
            pattern[i] = 1
        
        else:
            pattern[i] += 1

for k, v in pattern.items():
    answer.append([k, v])

answer.sort(key= lambda x:x[1], reverse = True)

if len(answer) >= 2:
    if answer[0][1] == answer[1][1]:
        print("-1")
    
    else:
        print(answer[0][0])

else:
    print(answer[0][0])