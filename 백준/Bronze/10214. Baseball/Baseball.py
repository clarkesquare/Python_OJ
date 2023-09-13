for _ in range(int(input())):
    yonsei, korea = 0, 0
    for _ in range(9):
        n, m = map(int, input().split())
        yonsei, korea = yonsei + n, korea + m

    if yonsei > korea:
        print('Yonsei')
    elif yonsei < korea:
        print('Korea')
    else:
        print('Draw')