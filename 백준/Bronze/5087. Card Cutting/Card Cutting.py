cheryl, tania = 0, 0

while True:
    word = input()
    if word != '#':
        word = word.replace('A', '1')
        cheryl, tania = 0, 0
        for i in word:
            if i.isdigit():
                if int(i) % 2 == 1:
                    cheryl += 1
                else:
                    tania += 1
        
        if cheryl > tania:
            print("Cheryl")
        elif cheryl < tania:
            print("Tania")
        else:
            print("Draw")
    
    else:
        break