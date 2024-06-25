n = int(input())
potatoes = list(map(int, input().split()))
answer = [0, 0]

potatoes.sort()
answer[0] = sum(potatoes[:n//2:])
answer[1] = sum(potatoes[n//2::])

print(*answer)