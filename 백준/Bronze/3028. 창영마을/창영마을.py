pattern = input()
place = [1, 0, 0]

for i in pattern:
    if i == 'A':
        place[0], place[1] = place[1], place[0]
    elif i == 'B':
        place[1], place[2] = place[2], place[1]
    else:
        place[0], place[2] = place[2], place[0]

print(place.index(1)+1)