for _ in range(int(input())):
    pattern = input()
    answer = 0
    cnt = 0
    for i in range(len(pattern)):
        if pattern[i] == "O":
            cnt += 1
            answer += cnt
        
        else:
            cnt = 0

    print(answer)