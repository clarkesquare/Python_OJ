word = ""
tmp = {}

for _ in range(int(input())):
    word = input()
    for i in range(len(word)):
        if (word[(-1 * i):] + word[:(-1 * i)]) in tmp:
            tmp[(word[(-1 * i):] + word[:(-1 * i)])] += 1
            break

    else:
        tmp[word] = 1

print(len(tmp))