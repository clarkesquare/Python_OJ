n = int(input())
A = set(map(int, input().split()))
m = int(input())
B = map(int, input().split())
answer = []

for i in B:
    answer.append(1 if i in A else 0)

print(*answer)