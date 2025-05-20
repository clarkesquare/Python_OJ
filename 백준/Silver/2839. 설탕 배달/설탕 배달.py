n = int(input())
answer = n // 5

while answer != -1:
    if answer != 0:
        if n % (answer * 5) == 0:
            break

        else:
            if (n - (answer * 5)) % 3 == 0:
                answer += (n - (answer * 5)) // 3
                break
    
    else:
        if n % 3 == 0:
            answer = n // 3
            break

    answer -= 1

print(answer)