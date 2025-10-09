def solution(dirs):
    position = {}
    x, y = 0, 0

    for i in range(len(dirs)):
        if dirs[i] == 'U' and y + 1 != 6:
            if (x, y, y+1) not in position:
                position[(x, x, y, y+1)] = None

            y += 1

        elif dirs[i] == 'D' and y - 1 != -6:
            if (x, y-1, y) not in position:
                position[(x, x, y-1, y)] = None

            y -= 1

        elif dirs[i] == 'L' and x - 1 != -6:
            if (x-1, x, y, y) not in position:
                position[(x-1, x, y, y)] = None

            x -= 1

        elif dirs[i] == 'R' and x + 1 != 6:
            if (x, x+1, y, y) not in position:
                position[(x, x+1, y, y)] = None

            x += 1
    
    return len(position)