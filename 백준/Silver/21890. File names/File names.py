answer = 0

for _ in range(int(input())):
    word = input()
    if word.count(".") == 1:
        a, b = word.split(".")
        if 1 <= len(a) and len(a) <= 8 and 1 <= len(b) and len(b) <= 3:
            answer += 1

print(answer)