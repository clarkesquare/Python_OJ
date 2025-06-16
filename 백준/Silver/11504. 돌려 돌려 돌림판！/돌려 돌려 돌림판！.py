for _ in range(int(input())):
    n, m = map(int, input().split())

    # 최소, 최대 셋팅
    minimum = int(''.join(input().split()))
    maximum = int(''.join(input().split()))

    # 답 검새
    answer = 0
    chk = ''.join(input().split()) * 2
    for i in range(n):
        tmp = int(''.join(chk[i:i+m]))
        if minimum <= tmp and tmp <= maximum:
            answer += 1
    
    print(answer)