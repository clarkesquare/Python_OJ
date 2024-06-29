while True:
    word = list(input())
    if word[0] != "#":
        small = []
        large = []
        number = []
        for i in word:
            if i.islower():
                small.append(i)
            elif i.isupper():
                large.append(i)
            else:
                number.append(i)

        small.sort()
        large.sort()
        number.sort()
        answer = small + large + number
        print(*answer, sep= "")
    
    else:
        break