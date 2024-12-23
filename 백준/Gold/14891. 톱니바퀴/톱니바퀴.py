from collections import deque

gears = []
pattern = []
answer = 0

# 처음 셋팅
for _ in range(4):
    pattern.append(deque(input()))

for i in range(int(input())):
    a, b = map(int, input().split())
    left = b
    right = b
    leftcheck = pattern[a-1][-2]
    rightcheck = pattern[a-1][2]
    pattern[a-1].rotate(b) # 최초 변경

    # 오른쪽 쭉쭉
    changed = 1
    for i in range(a, 4):
        if changed == 1:
            if rightcheck != pattern[i][-2]:
                rightcheck = pattern[i][2]
                right *= -1
                pattern[i].rotate(right)
            
            else:
                changed = 0
        
        else:
            break
    
    # 왼쪽 쭉쭉
    changed = 1
    for i in range(a-2, -1, -1):
        if changed == 1:
            if leftcheck != pattern[i][2]:
                leftcheck = pattern[i][-2]
                left *= -1
                pattern[i].rotate(left)
            
            else:
                changed = 0
        
        else:
            break

# 결과 출력
for i in range(4):
    if pattern[i][0] == "1":
        answer += 2 ** i

print(answer)