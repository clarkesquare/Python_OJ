heart = [0, 0]
body = [0, 0, 0, 0, 0]

# 반복문 횟수동안 검사
for i in range(int(input())):
    tmp = input()
    if "*" in tmp and heart == [0, 0]: # 심장 저장
        heart = [i+2, tmp.index("*")+1]

    elif i == heart[0]-1 and heart != [0, 0]: # 팔 검사
        for j in tmp[heart[1]-2::-1]:
            if j == "*":
                body[0] += 1

            else:
                break

        for k in tmp[heart[1]::]:
            if k == "*":
                body[1] += 1

            else:
                break
    
    elif body[0] != 0 and body[1] != 0 and tmp[heart[1]-1] == "*": # 허리 검사
        body[2] += 1
    
    elif body[0] != 0 and body[1] != 0 and body[2] != 0 and tmp[heart[1]-1] == "_": # 다리 검사
        if tmp[heart[1]-2] == "*":
            body[3] += 1
        
        if tmp[heart[1]] == "*":
            body[4] += 1


# body는 차례대로 왼손, 오른손, 허리, 왼다리, 오른다리 결과 출력.
print(*heart)
print(*body)