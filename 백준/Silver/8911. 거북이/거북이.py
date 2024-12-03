for _ in range(int(input())):
    max_coordinate = [0, 0]
    min_coordinate = [0, 0]
    coordinate = [0, 0]
    direction = 0
    for i in input():
        if i == "L":
            if direction == 0:
                direction = 3
            
            else:
                direction -= 1
        
        elif i == "R":
            direction += 1
            direction %= 4
        
        elif i == "F":
            if direction == 0:
                coordinate[1] += 1

            elif direction == 1:
                coordinate[0] += 1
            
            elif direction == 2:
                coordinate[1] -= 1
            
            else:
                coordinate[0] -= 1

        else: # Back
            if direction == 0:
                coordinate[1] -= 1
            
            elif direction == 1:
                coordinate[0] -= 1
            
            elif direction == 2:
                coordinate[1] += 1
            
            else:
                coordinate[0] += 1
        
        if max_coordinate[0] < coordinate[0]:
            max_coordinate[0] = coordinate[0]
        
        if max_coordinate[1] < coordinate[1]:
            max_coordinate[1] = coordinate[1]
        
        if min_coordinate[0] > coordinate[0]:
            min_coordinate[0] = coordinate[0]
        
        if min_coordinate[1] > coordinate[1]:
            min_coordinate[1] = coordinate[1]

    answer = (max_coordinate[0] - min_coordinate[0]) * (max_coordinate[1] - min_coordinate[1])
    print(answer)