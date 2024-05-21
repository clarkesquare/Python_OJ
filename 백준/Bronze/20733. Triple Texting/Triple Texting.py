word = input()
words = []
tmp = ""
answer = ""

for i in range(len(word)):
    tmp += word[i]
    if len(tmp) == (len(word)//3):
        words.append(tmp)
        tmp = ""

for j in range(len(word)//3):
    tmp = [words[0][j], words[1][j], words[2][j]]
    if tmp.count(words[0][j]) == 3:
        answer += words[0][j]
    else:
        for k in tmp:
            if tmp.count(k) >= 2:
                answer += k
                break

print(answer)