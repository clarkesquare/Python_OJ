for _ in range(int(input())):
    sentense = input()
    answer = ""
    for i in range(1, 101):
        if i ** 2 >= len(sentense):
            pattern = []
            if i ** 2 != len(sentense):
                sentense += ((i ** 2) - (len(sentense))) * "*"
                
            for a in range(i):
                pattern.append(sentense[a*i:(a+1)*i])
            
            for j in range(i):
                for k in range(i-1, -1, -1):
                    if pattern[k][j] != "*":
                        answer += pattern[k][j]

            print(answer)
            break