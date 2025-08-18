vowels = {'a': None, 'e': None, 'i': None, 'o': None, 'u': None}

while True:
    word = input().strip()
    if word == 'end':
        break

    answer = ''
    check = [0, '']      # [모음 등장 여부(0/1), 직전 문자]
    straight = [0, 0]    # [모음 연속 길이, 자음 연속 길이]

    # 첫 글자 처리
    check[1] = word[0]
    if word[0] in vowels:
        check[0] = 1
        straight[0] = 1   # 첫 글자가 모음이면 모음 연속을 1로 시작
        straight[1] = 0
    else:
        straight[0] = 0
        straight[1] = 1   # 첫 글자가 자음이면 자음 연속을 1로 시작

    # 나머지 글자 순회
    for i in range(1, len(word)):
        ch = word[i]

        # 모음/자음 연속 업데이트
        if ch in vowels:
            check[0] = 1
            straight[0] += 1
            straight[1] = 0
        else:
            straight[0] = 0
            straight[1] += 1

        # 3개 연속 금지
        if straight[0] == 3 or straight[1] == 3:
            answer = 'not '
            break

        # 같은 글자 연속 금지(ee, oo만 예외)
        if check[1] == ch and ch not in ('e', 'o'):
            answer = 'not '
            break

        check[1] = ch

    # 모음이 하나도 없으면 비허용
    if check[0] == 0:
        answer = 'not '

    print(f"<{word}> is {answer}acceptable.")
