for _ in range(int(input())):
    word = input().lower()
    answer = 0
    tmp = ""
    for i in word:
        if tmp == "":
            if i == "p":
                tmp = "p"
        
        elif tmp == "p":
            if i == "l":
                tmp = "l"
            
        elif tmp == "l":
            if i == "u":
                tmp = ""
                answer += 1
    
    print(answer)