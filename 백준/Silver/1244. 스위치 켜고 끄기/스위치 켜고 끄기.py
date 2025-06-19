n = int(input())
lights = list(map(int, input().split()))

for _ in range(int(input())):
    pattern = list(map(int, input().split()))
    if pattern[0] == 1: # 끈 학생이 남자인 경우
        for i in range(pattern[1]-1, n, pattern[1]):
            if lights[i] == 0:
                lights[i] = 1
            
            else:
                lights[i] = 0
    
    else: # 끈 학생이 여자인 경우
        if lights[pattern[1]-1] == 0:
            lights[pattern[1]-1] = 1
        
        else:
            lights[pattern[1]-1] = 0

        if n // 2 < pattern[1]: # 오른쪽에서 끝남
            for i in range(1, n - pattern[1]+1):
                if lights[pattern[1]-1-i] == lights[pattern[1]-1+i]:
                    if lights[pattern[1]-1-i] == 0:
                        lights[pattern[1]-1-i] = 1
                        lights[pattern[1]-1+i] = 1
                    
                    else:
                        lights[pattern[1]-1-i] = 0
                        lights[pattern[1]-1+i] = 0
                
                else:
                    break
            
        else: # 왼쪽에서 끝남
            for i in range(1, pattern[1]):
                if lights[pattern[1]-1-i] == lights[pattern[1]-1+i]:
                    if lights[pattern[1]-1-i] == 0:
                        lights[pattern[1]-1-i] = 1
                        lights[pattern[1]-1+i] = 1
                    
                    else:
                        lights[pattern[1]-1-i] = 0
                        lights[pattern[1]-1+i] = 0
                
                else:
                    break

for i in range(0, n+1, 20):
    print(*lights[i:i+20])