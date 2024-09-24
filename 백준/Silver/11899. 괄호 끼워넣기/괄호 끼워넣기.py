word = input()

while "()" in word:
    word = word.replace("()", "")

print(len(word))