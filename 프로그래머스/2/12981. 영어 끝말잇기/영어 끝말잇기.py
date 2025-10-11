def solution(n, words):
    answer = [0, 0]
    check = {words[0]: None}

    for i in range(1, len(words)):
        if words[i][0] == words[i-1][-1]:
            if words[i] in check:
                answer = [(i % n) + 1, (i // n) + 1]
                break

            else:
                check[words[i]] = None


        else:
            answer = [(i % n) + 1, (i // n) + 1]
            break
    
    return answer