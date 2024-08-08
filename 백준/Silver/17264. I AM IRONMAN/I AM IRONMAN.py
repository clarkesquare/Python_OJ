n, m = map(int, input().split())
w, l, g = map(int, input().split())
pattern = {}
score = 0
answer = "I AM IRONMAN!!"

for _ in range(m):
    a, b = input().split()
    if b == "W":
        pattern[a] = ""

for _ in range(n):
    if input() in pattern:
        score += w

    else:
        score -= l
        if score < 0:
            score = 0
    
    if score >= g:
        answer = "I AM NOT IRONMAN!!"

print(answer)