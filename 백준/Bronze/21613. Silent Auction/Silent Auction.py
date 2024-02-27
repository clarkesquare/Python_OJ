max_name = ''
max_score = 0
name = ''
score = 0

for _ in range(int(input())):
    name = input()
    score = int(input())
    if score > max_score:
        max_name = name
        max_score = score

print(max_name)