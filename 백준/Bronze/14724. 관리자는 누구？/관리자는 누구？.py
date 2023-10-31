clubs = ['PROBRAIN', 'GROW', 'ARGOS', 'ADMIN', 'ANT', 'MOTION', 'SPG', 'COMON', 'ALMIGHTY']
scores = []

n = int(input())
for _ in range(9):
    scores.append(max(map(int, input().split())))

print(clubs[scores.index(max(scores))])