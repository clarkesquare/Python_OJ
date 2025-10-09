def solution(record):
    id = {}
    tmp = []
    answer = []

    for i in record:
        if len(i.split()) == 3:
            a, b, c = i.split()
            id[b] = c

        else:
            a, b = i.split()

        if a != 'Change':
            tmp.append((a, b))

    for status in tmp:
        if status[0] == 'Enter':
            answer.append(f'{id[status[1]]}님이 들어왔습니다.')

        else:
            answer.append(f'{id[status[1]]}님이 나갔습니다.')

    return answer