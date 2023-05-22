def solution(lines):
    answer = 0
    temp = []
    line_a, line_b, line_c = [], [], []
    n = 0
    
    if lines[0] == lines[1] == lines[2]:
        answer = lines[0][1] - lines[0][0]
    else:
        for i in range(len(lines)):
            for j in range(lines[i][0]+1, int(lines[i][-1])+1):
                if lines.index(lines[i]) == 0:
                    line_a.append(j)
                elif lines.index(lines[i]) == 1:
                    line_b.append(j)
                else:
                    line_c.append(j)

        for i in line_a:
            if (i in line_b or i in line_c) and i not in temp:
                temp.append(i)
                answer += 1

        for i in line_b:
            if (i in line_c) and i not in temp:
                temp.append(i)
                answer += 1
    
    return answer