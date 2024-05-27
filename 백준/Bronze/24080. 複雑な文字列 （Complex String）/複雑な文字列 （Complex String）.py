pattern = ["A", "B", "C", "D", "E"]
answer = 0

n = int(input())
word = input()
for i in pattern:
    if i in word:
        answer += 1

print("Yes" if answer >= 3 else "No")