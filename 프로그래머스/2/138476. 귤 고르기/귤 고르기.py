def solution(k, tangerine):
    gyul = {}
    answer = []

    for i in range(len(tangerine)):
        gyul[tangerine[i]] = gyul.get(tangerine[i], 0) + 1

    answer = list(gyul.items())
    answer.sort(key=lambda x:x[1], reverse=True)

    for i in range(len(answer)-1, -1, -1):
        if answer[i][1] <= (len(tangerine) - k):
            k += answer[i][1]
            answer.pop()

        else:
            break

    return len(answer)