patterns = ['-', '\\', '(', '@', '?', '>', '&', '%', '/']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, -1]

while True:
    word = input()
    answer = 0
    if word != '#':
        for i in range(len(word)):
            answer += numbers[patterns.index(word[i])] * (8 ** (len(word)-i-1))

        print(answer)

    else:
        break