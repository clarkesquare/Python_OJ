import sys
input = sys.stdin.readline

a = int(input())

for _ in range(a):
    box = []
    cnt = 0
    m, n = map(int, input().split())
    for _ in range(m): # 이중 리스트 생성
        box.append(list(map(int, input().split(' '))))
    
    for i in range(n):
        temp = []
        for j in range(m-1, -1, -1):
            temp.append(box[j][i])
        for k in range(m):
            if temp[k] == 1:
                for l in range(k):
                    if temp[l] == 0:
                        temp[l] = 1
                        temp[k] = 0
                        cnt += k-l
                        break

    print(cnt)