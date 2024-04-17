from string import ascii_uppercase

alphabets = list(ascii_uppercase)

word = ""

while True:
    word = input()
    if word != "END":
        for i in word:
            if word.count(i) > 1 and i != " ":
                break
        
        else:
            print(word)
    
    else:
        break