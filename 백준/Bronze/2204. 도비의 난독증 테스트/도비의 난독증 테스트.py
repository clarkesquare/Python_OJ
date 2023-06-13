while True:
    n = int(input())
    if n != 0:
        words = []
        for _ in range(n):
            words.append(input())
        words.sort(key=str.lower)
        print(words[0])
    else:
        break