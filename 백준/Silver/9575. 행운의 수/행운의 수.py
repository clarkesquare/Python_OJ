for _ in range(int(input())):
    pattern_a = {}
    pattern_b = {}
    pattern_c = {}
    answer = {}

    a = int(input())
    for i in map(int, input().split()):
        if i not in pattern_a:
            pattern_a[i] = ""
    
    b = int(input())
    for i in map(int, input().split()):
        if i not in pattern_b:
            pattern_b[i] = ""
    
    c = int(input())
    for i in map(int, input().split()):
        if i not in pattern_c:
            pattern_c[i] = ""
    
    for j in pattern_a:
        for k in pattern_b:
            for l in pattern_c:
                tmp = str(j+k+l)
                for num in tmp:
                    if not(num == "5" or num == "8"):
                        break
                
                else:
                    if tmp not in answer:
                        answer[tmp] = ""

    print(len(answer))