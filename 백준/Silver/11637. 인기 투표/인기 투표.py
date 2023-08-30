for _ in range(int(input())):
    lawmakers = []
    for _ in range(int(input())):
        lawmakers.append(int(input()))

    if lawmakers.count(max(lawmakers)) == 1:
        if (max(lawmakers) / sum(lawmakers)) > 0.5:
            print('majority winner', lawmakers.index(max(lawmakers))+1)
        else:
            print('minority winner', lawmakers.index(max(lawmakers))+1)

    else:
        print('no winner')