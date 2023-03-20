n = int(input())
scores = list(map(int, input().split()))

scores.sort()

print(max(scores) - min(scores))