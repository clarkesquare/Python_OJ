def solution(s):
    answer = [0, 0]

    while len(s) != 1:
        answer[0] += 1
        if s.count('0') != 0:
            answer[1] += s.count('0')

        s = bin(s.count('1'))[2:]

    print(answer)
    return answer