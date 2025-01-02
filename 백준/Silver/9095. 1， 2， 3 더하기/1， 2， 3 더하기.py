for _ in range(int(input())):
    pattern = (1, 2, 3)
    answer = (0, )
    tmp = ()
    num = 0
    cnt = 0
    total = 0
    n = int(input())
    while len(answer) != 0:
        tmp = ()
        for i in answer:
            for j in pattern:
                num = i + j
                if num == n:
                    cnt += 1
                
                elif num < n:
                    tmp += (num, )
        
        answer = tmp

    print(cnt)