A, B, C = map(int, (input().split()))

score = [A, B, C]
score.sort(reverse=True)

print(score[1])