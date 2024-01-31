for _ in range(int(input())):
    n = int(input())
    cnt = 0
    first = list(map(int, input().split()))
    second = list(map(int, input().split()))
    for i in range(n):
        if first[i] != second[i]:
            cnt += 1
    
    print(cnt)