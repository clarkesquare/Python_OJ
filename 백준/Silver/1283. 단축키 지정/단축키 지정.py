import sys

input = sys.stdin.readline

pattern = {}
for _ in range(int(input())):
    word = input().strip("\n").split()
    answer = 0

    # 먼저 앞의 것들을 체크
    for i in range(len(word)):
        if word[i][0].lower() not in pattern:
            pattern[word[i][0].lower()] = ""
            word[i] = "[" + word[i][0] + "]" + word[i][1:]
            answer = 1
            break
            
    # 그 다음에 순차 체크
    if answer == 0:
        for i in range(len(word)):
            for j in range(len(word[i])):
                if word[i][j].lower() not in pattern:
                    pattern[word[i][j].lower()] = ""
                    word[i] = word[i][:j] + "[" + word[i][j] + "]" + word[i][j+1:]
                    answer = 1
                    break
            
            if answer == 1:
                break
    
    # 각 옵션 출력
    print(*word, sep=" ")