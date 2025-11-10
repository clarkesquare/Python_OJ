while True:
    n = int(input())
    if n != 0:
        check = {}
        answer = []
        for _ in range(n):
            word = input()
            tmp = tuple(sorted(list(word)))
            if tmp not in check:
                check[tmp] = [word]
            
            else:
                check[tmp].append(word)
        
        answer = list(check.items())
        answer.sort(key=lambda x: len(x[1]), reverse=True)
        print(answer[0][1][0], len(answer[0][1]) - 1)
    
    else:
        break