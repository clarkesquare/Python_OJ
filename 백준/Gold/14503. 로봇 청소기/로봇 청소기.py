import time

n, m = map(int, input().split())
r, c, d = map(int, input().split())
maps = []

answer = 0
cnt = 0

for _ in range(n):
    maps.append(list(map(int, input().split())))

while True:
    if maps[r][c] == 0: # 1-1 칸 청소 안했으면 청소, 된건 2로 변경
        maps[r][c] = 2
        answer += 1
    
    elif maps[r][c] == 2: # 해당 칸 이미 청소함
        if maps[r-1][c] != 0 and maps[r][c-1] != 0 and maps[r+1][c] != 0 and maps[r][c+1] != 0: # 1 - 2주변에 청소할 거 없으면
            if d == 0:
                r += 1
            
            elif d == 1:
                c -= 1
            
            elif d == 2:
                r -= 1
            
            else:
                c += 1
        
        else:
            for i in range(4): # 방향 기준으로 반시계 방향 돌고 0 찾기기
                d -= 1
                if d == -1:
                    d = 3
                
                if d == 0 and maps[r-1][c] == 0:
                    r -= 1
                    break

                elif d == 1 and maps[r][c+1] == 0:
                    c += 1
                    break

                elif d == 2 and maps[r+1][c] == 0:
                    r += 1
                    break
                
                elif d == 3 and maps[r][c-1] == 0:
                    c -= 1
                    break
    
    else: # 해당 위치가 1이면 시스템 종료
        break

print(answer)