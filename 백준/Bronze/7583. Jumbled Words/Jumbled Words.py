while True:
    words = list(input().split())
    if words[0] != '#':
        answer = []
        for i in range(len(words)):
            temp = ''
            if len(words[i]) >= 4:
                words[i] = words[i][0] + words[i][-2:0:-1] + words[i][-1]

        print(" ".join(words))

    else:
        break