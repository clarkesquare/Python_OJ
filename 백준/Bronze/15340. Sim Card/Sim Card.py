while True:
    answer = []
    a, b = map(int, input().split())
    if a != 0 and b != 0:
        answer.append(a*30 + b*40)
        answer.append(a*35 + b*30)
        answer.append(a*40 + b*20)
        print(min(answer))
    
    else:
        break