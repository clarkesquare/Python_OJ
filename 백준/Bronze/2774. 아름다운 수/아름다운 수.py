for _ in range(int(input())):
    n = input()
    pattern = []
    answer = 0
    for i in n:
        if i not in pattern:
            pattern.append(i)
            answer += 1
    
    print(answer)