stack = 0

while True:
    word = input()
    if word == '고무오리 디버깅 시작':
        pass
    elif word == '문제':
        stack += 1
    elif word == '고무오리':
        if stack >= 1:
            stack -=1
        else:
            stack += 2

    else:
        print('고무오리야 사랑해' if stack == 0 else '힝구')
        break