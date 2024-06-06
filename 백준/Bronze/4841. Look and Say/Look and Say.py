answer = ""

for _ in range(int(input())):
    word = input()
    tmp = word[0]
    cnt = 1
    answer = ""
    for i in range(1, len(word)):
        if word[i] == tmp:
            cnt += 1
        
        else:
            answer += str(cnt) + tmp
            tmp = word[i]
            cnt = 1
    
    answer += str(cnt) + tmp
    print(answer)