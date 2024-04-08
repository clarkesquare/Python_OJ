answer = 0

for _ in range(int(input())):
    word = input()
    if word.count("for") + word.count("while") > answer:
        answer = word.count("for") + word.count("while")

print(answer)