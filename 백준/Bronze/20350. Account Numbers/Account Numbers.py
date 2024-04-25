from string import ascii_uppercase

alphabets = list(ascii_uppercase)

pattern = input()
pattern = pattern[4:] + pattern[:4]
answer = ""

for i in pattern:
    answer += i if i not in alphabets else str(alphabets.index(i) + 10)

print("correct" if int(answer) % 97 == 1 else "incorrect")