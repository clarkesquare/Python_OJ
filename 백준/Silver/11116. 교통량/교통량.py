for _ in range(int(input())):
    answer = 0
    m = int(input())
    chk = 0
    left = {}
    right = {}
    for i in list(map(int, input().split())):
        left[i] = None
    
    for i in list(map(int, input().split())):
        right[i] = None

    for i in left:
        if i+500 in left and i + 1000 in right and i + 1500 in right:
            answer += 1
    
    print(answer)