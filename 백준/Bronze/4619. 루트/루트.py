while True:
    a, b = map(int, input().split())
    if a != 0 and b != 0:
        answer = 1
        while True:
            tmp = answer **  b
            if a <= tmp:
                if a < tmp:
                    if abs(tmp - a) > abs((answer - 1) ** b - a):
                        answer -= 1

                break
            
            answer += 1

        print(answer)

    else:
        break