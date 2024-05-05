for cnt in range(1, int(input())+1):
    c = int(input())
    i = int(input())
    numbers = list(map(int, input().split()))
    answer = [0, 0]

    for j in range(i-1):
        for k in range(j+1, i):
            if numbers[j] + numbers[k] == c:
                answer[0], answer[1] = j + 1, k + 1
                break
        
        if answer != [0, 0]:
            break

    print(f"Case #{cnt}: {answer[0]} {answer[1]}")