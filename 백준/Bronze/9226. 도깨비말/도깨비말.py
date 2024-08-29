vowels = ["a", "e", "i", "o", "u"]
tmp = ""

while True:
    word = input()
    if word != "#":
        tmp = ""
        for i in range(len(word)):
            if word[i] not in vowels:
                tmp += word[i]
            
            else:
                word = word[i:] + tmp + "ay"
                break
        
        if word[-2:] != "ay":
            word += "ay"
            
        print(word)

    else:
        break