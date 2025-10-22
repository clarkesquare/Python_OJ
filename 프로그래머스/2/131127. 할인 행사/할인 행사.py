def solution(want, number, discount):
    total = sum(number)
    answer = 0
    check = {}
    for i in range(len(want)):
        check[want[i]] = number[i]

    tmp = {}

    for i in range(total):
        if discount[i] not in tmp:
            tmp[discount[i]] = 1

        else:
            tmp[discount[i]] += 1

    if tmp == check:
        answer += 1

    for i in range(len(discount) - total):
        before = discount[i]
        if before in tmp:
            if tmp[before] >= 2:
                tmp[before] -= 1

            else:
                tmp.pop(before)

        if discount[i+total] in tmp:
            tmp[discount[i+total]] += 1

        else:
            tmp[discount[i+total]] = 1

        if tmp == check:
            answer += 1

    return answer