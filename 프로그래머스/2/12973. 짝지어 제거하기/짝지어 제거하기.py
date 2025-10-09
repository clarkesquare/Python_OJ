from collections import deque

def solution(s):
    tmp = deque()
    answer = 0

    for i in range(len(s)):
        tmp.append(s[i])
        if len(tmp) >= 2:
            while tmp[-1] == tmp[-2]:
                tmp.pop()
                tmp.pop()
                if len(tmp) < 2:
                    break

    if len(tmp) == 0:
        answer = 1

    return answer