from string import ascii_lowercase
alphabets = list(ascii_lowercase)
tmp = []

while True:
    word = input()
    if word != "*":
        tmp = []
        for i in word:
            if i in alphabets and i not in tmp:
                tmp.append(i)
        
        if len(tmp) == 26:
            print("Y")
        else:
            print("N")
    
    else:
        break