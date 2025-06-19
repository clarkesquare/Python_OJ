n, score, p = map(int, input().split())
if n > 0:
    numbers = list(map(int, input().split()))
    if n < p:
        numbers += [-1] * (p - n)

    for i in range(p):
        if score > numbers[i]:
            if score == numbers[i-1]:
                answer = numbers.index(score) + 1

            else:
                answer = i + 1
            
            break
    
    else:
        answer = -1

else:
    answer = 1

print(answer)