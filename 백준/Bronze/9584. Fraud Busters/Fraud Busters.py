answer = []
word = input()
for _ in range(int(input())):
    tmp = input()
    for i in range(9):
        if word[i] != '*' and (word[i] != tmp[i]):
            break

    else:
        answer.append(tmp)

print(len(answer))
print(*answer, sep='\n')