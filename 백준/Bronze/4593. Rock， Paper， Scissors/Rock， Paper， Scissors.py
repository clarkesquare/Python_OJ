RSP = ['R', 'S', 'P']

while True:
    p1 = input()
    p2 = input()
    score = [0, 0]
    if (p1 != 'E') and (p2 != 'E'):
        for i in range(len(p1)):
            if p1[i] != p2[i]:
                if p1[i] == RSP[0]:
                    if p2[i] == RSP[1]:
                        score[0] += 1
                    else:
                        score[1] += 1

                elif p1[i] == RSP[1]:
                    if p2[i] == RSP[2]:
                        score[0] += 1
                    else:
                        score[1] += 1

                else:
                    if p2[i] == RSP[0]:
                        score[0] += 1
                    else:
                        score[1] += 1
                        
        print('P1:', score[0])
        print('P2:', score[1])

    else:
        break