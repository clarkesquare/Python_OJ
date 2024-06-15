for _ in range(int(input())):
    answer = 0
    area = []
    for _ in range(int(input())):
        word = input()
        if word not in area:
            area.append(word)
    
    print(len(area))