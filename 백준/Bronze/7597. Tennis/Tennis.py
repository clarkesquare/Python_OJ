game = ""
A = 0
B = 0
score = ["A", 0, "B", 0]

while True:
    game = input()
    if game != "#":
        A = 0
        B = 0
        score = ["A", 0, "B", 0]
        for i in game:
            if i == "A":
                A += 1
            else:
                B += 1
            
            if A >= 4 or B >= 4:
                if (A-B) >= 2:
                    A, B = 0, 0
                    score[1] += 1
                elif (B-A) >= 2:
                    A, B = 0, 0
                    score[3] += 1
        
        print(*score)
    
    else:
        break