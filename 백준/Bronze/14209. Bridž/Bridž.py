answer = 0

for _ in range(int(input())):
    word = input()
    answer += word.count('A') * 4 + word.count('K') * 3 + word.count('Q') * 2 + word.count('J') * 1

print(answer)