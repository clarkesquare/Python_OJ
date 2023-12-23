finger_a = [' ', '1', 'Q', 'A', 'Z']
finger_b = ['2', 'W', 'S', 'X']
finger_c = ['3', 'E', 'D', 'C']
finger_d = ['4', '5', 'R', 'T', 'F', 'G', 'V', 'B']
finger_e = ['6', '7', 'Y', 'U', 'H', 'J', 'N', 'M']
finger_f = ['8', 'I', 'K', ',']
finger_g = ['9', 'O', 'L', '.']
finger_h = ['0', '-', '=', 'P', '[', ']', 'L', '\'', '/']
answer = [0] * 8

word = input()

for i in word:
    if i in finger_a:
        answer[0] += 1
    elif i in finger_b:
        answer[1] += 1
    elif i in finger_c:
        answer[2] += 1
    elif i in finger_d:
        answer[3] += 1
    elif i in finger_e:
        answer[4] += 1
    elif i in finger_f:
        answer[5] += 1
    elif i in finger_g:
        answer[6] += 1
    else:
        answer[7] += 1

for j in answer:
    print(j)