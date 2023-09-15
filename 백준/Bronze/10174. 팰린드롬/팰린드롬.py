for _ in range(int(input())):
    word = list(input())
    for i in range(len(word)):
        if word[i].isupper():
            word[i] = word[i].lower()

    print('Yes' if word == word[::-1] else 'No')