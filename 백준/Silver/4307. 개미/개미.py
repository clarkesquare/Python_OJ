for _ in range(int(input())):
    n, l = map(int, input().split())
    answer = [0, 0] # 최소, 최대
    half = n // 2
    for _ in range(l):
        num = int(input())
        # 최소, 중앙에 가까울수록
        if num < half:
            if num > answer[0]:
                answer[0] = num
            
        else:
            if n - num > answer[0]:
                answer[0] = n - num

        # 최대, 반대쪽에서 멀수록
        if num < half:
            if n - num > answer[1]:
                answer[1] = n - num
        
        else:
            if num > answer[1]:
                answer[1] = num

    print(*answer)