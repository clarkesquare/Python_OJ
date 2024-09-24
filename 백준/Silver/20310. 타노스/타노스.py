word = list(input())
answer = [word.count("0")//2, word.count("1")//2]

# 앞에서부터 1 제거, 뒤에서부터 0 제거!!

for _ in range(answer[1]):
    for i in range(len(word)):
        if word[i] == "1":
            word[i] = ""
            break

for j in range(answer[0]):
    for j in range(len(word)-1, 0, -1):
        if word[j] == "0":
            word[j] = ""
            break

print(*word, sep="")