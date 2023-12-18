word = ''
word1 = ''
word2 = ''

for _ in range(int(input())):
    word1 = ''
    word2 = ''
    word = input()
    i = 0
    while True:
        if len(word1) == len(word2):
            if word[i] in word1:
                break
            else:
                word1 += word[i]
        else:
            if word[i] in word2:
                break
            else:
                word2 += word[i]

        i += 1
        if i >= len(word):
            i -= len(word)
    
    print(word1)
    print(word2)