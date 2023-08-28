a, b = map(int, input().split())
favorite = []
answer = abs(a-b)

for i in range(int(input())):
    favorite.append(int(input()))

for j in favorite:
    if abs(j-b) < answer:
        answer = abs(j-b)+1

print(answer)