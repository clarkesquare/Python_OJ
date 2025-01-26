n, k = map(int, input().split())
obstacles = {}
answer = [0, 0]

for _ in range(n):
    a, b = map(int, input().split())
    obstacles[(a, b)] = ''

pattern = input()
for i in pattern:
    if i == 'U' and (answer[0], answer[1]+1) not in obstacles:
        answer[1] += 1

    elif i == 'D' and (answer[0], answer[1]-1) not in obstacles:
        answer[1] -= 1
    
    elif i == 'L' and (answer[0]-1, answer[1]) not in obstacles:
        answer[0] -= 1

    elif i == 'R' and (answer[0]+1, answer[1]) not in obstacles:
        answer[0] += 1

print(*answer)