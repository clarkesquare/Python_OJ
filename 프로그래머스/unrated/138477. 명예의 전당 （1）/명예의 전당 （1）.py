def solution(k, score):
    answer = []
    hof = []
    
    for i in score:
        hof.append(i)
        hof.sort()
        if len(hof) > k:
            hof.remove(hof[0])
        answer.append(hof[0])
    return answer