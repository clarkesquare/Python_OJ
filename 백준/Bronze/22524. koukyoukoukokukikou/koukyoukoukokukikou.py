left = "QWERTASDFGZXCVB"
right = "YUIOPHJKLNM"
word = ""
answer = 0

while True:
    word = input()
    if word != "#":
        word = word.upper()
        answer = 0
        for i in range(1, len(word)):
            if word[i] in left and word[i-1] not in left:
                answer += 1
            elif word[i] in right and word[i-1] not in right:
                answer += 1

        print(answer)

    else:
        break