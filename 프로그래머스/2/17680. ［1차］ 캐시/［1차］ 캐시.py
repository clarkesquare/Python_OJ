def solution(cacheSize, cities):
    check = []
    answer = 0
    if cacheSize != 0:
        for i in range(len(cities)):
            cities[i] = cities[i].lower()
            if cities[i] not in check:
                if len(check) == cacheSize:
                    check.pop(0)

                check.append(cities[i])
                answer += 5

            else:
                if check[-1] != cities[i]:
                    check.remove(cities[i])
                    check.append(cities[i])

                answer += 1

    else:
        answer = len(cities) * 5
        
    return answer