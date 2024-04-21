word = ""
temp = ""
cnt = 1
pattern = []

for _ in range(int(input())):
    word = input()
    temp = word[0]
    cnt = 1
    pattern = []
    for i in range(1, len(word)):
        if word[i] == temp and i != len(word)-1:
            cnt += 1

        else:
            if i == len(word)-1:
                if word[i] == temp:
                    cnt += 1
                else:
                    pattern.append(str(cnt))
                    pattern.append(temp)
                    temp = word[i]
                    cnt = 1

            pattern.append(str(cnt))
            pattern.append(temp)
            temp = word[i]
            cnt = 1
        
    print(" ".join(pattern))