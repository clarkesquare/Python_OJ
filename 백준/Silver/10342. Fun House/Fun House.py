import sys

input = sys.stdin.readline
start = [0, 0]
direction = 1 # 1 오른쪽, 시계 방향으로 2, 3, 4
cnt = 0

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    else:
        cnt += 1
        pattern = []
        coordinate = [0, 0]
        position = 0

        # 값 입력 
        for i in range(m):
            tmp = list(input().strip("\n"))
            if "*" in tmp:
                coordinate = [i, tmp.index("*")] # 시작 지점 체크

            pattern.append(tmp)
        
        # 시작 지점에 따른 방향 확인
        if coordinate[0] == 0:
            position = 2

        elif coordinate[0] == m - 1:
            position = 4
        
        elif coordinate[1] == 0:
            position = 1
        
        else:
            position = 3
        
        while True:
            if position == 1:
                while pattern[coordinate[0]][coordinate[1]] != "x" and pattern[coordinate[0]][coordinate[1]] != "/" and pattern[coordinate[0]][coordinate[1]] != "\\":
                    coordinate[1] += 1
                
                if pattern[coordinate[0]][coordinate[1]] == "/":
                    coordinate[0] -= 1
                    position = 4
                
                elif pattern[coordinate[0]][coordinate[1]] == "\\":
                    coordinate[0] += 1
                    position = 2
            
            elif position == 2:
                while pattern[coordinate[0]][coordinate[1]] != "x" and pattern[coordinate[0]][coordinate[1]] != "/" and pattern[coordinate[0]][coordinate[1]] != "\\":
                    coordinate[0] += 1
                
                if pattern[coordinate[0]][coordinate[1]] == "/":
                    coordinate[1] -= 1
                    position = 3
                
                elif pattern[coordinate[0]][coordinate[1]] == "\\":
                    coordinate[1] += 1
                    position = 1
            
            elif position == 3:
                while pattern[coordinate[0]][coordinate[1]] != "x" and pattern[coordinate[0]][coordinate[1]] != "/" and pattern[coordinate[0]][coordinate[1]] != "\\":
                    coordinate[1] -= 1
                
                if pattern[coordinate[0]][coordinate[1]] == "/":
                    coordinate[0] += 1
                    position = 2
                
                elif pattern[coordinate[0]][coordinate[1]] == "\\":
                    coordinate[0] -= 1
                    position = 4
                
            else:
                while pattern[coordinate[0]][coordinate[1]] != "x" and pattern[coordinate[0]][coordinate[1]] != "/" and pattern[coordinate[0]][coordinate[1]] != "\\":
                    coordinate[0] -= 1
                
                if pattern[coordinate[0]][coordinate[1]] == "/":
                    coordinate[1] += 1
                    position = 1
                
                elif pattern[coordinate[0]][coordinate[1]] == "\\":
                    coordinate[1] -= 1
                    position = 3
                
            if pattern[coordinate[0]][coordinate[1]] == "x":
                pattern[coordinate[0]][coordinate[1]] = "&"
                break

        # 정답 출력
        print(f"HOUSE {cnt}")
        for i in pattern:
            print(*i, sep="")