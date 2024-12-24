from collections import deque

n, m = map(int, input().split()) # N 개의 주차 공간, M 개의 자동차
price = []
weight = []
space = [0] * n
answer = 0
dq = deque() # 주차장 자리 없어서 밀린 차들 쌓아두기

for _ in range(n): # 단위 무게당 요금
    price.append(int(input()))

for _ in range(m): # 차량들의 무게
    weight.append(int(input()))

for _ in range(2 * m): # 차량 정리 및 정산
    car = int(input())
    if car >= 0:
        for i in range(n):
            if space[i] == 0:
                space[i] = car
                break
        
        else:
            dq.append(car)
    
    else:
        for i in range(n):
            if space[i] == car * -1:
                space[i] = 0
                if len(dq) >= 1:
                    space[i] = dq.popleft()
                
                break

        answer += price[i] * weight[(car * -1) -1]

print(answer)