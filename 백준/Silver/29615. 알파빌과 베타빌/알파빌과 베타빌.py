n, m = map(int, input().split())
pattern = list(map(int, input().split()))
friends = list(map(int, input().split()))
answer = 0

for i in pattern[:len(friends):]:
    if i not in friends:
        answer += 1

print(answer)