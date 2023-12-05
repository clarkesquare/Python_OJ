pattern1 = ['i', 'o', 'v', 'w', 'x']
pattern2 = ['b', 'd']
pattern3 = ['p', 'q']
word = ''
answer = ''

while True:
    word = input()
    if word != '#':
        answer = ''
        for i in word[::-1]:
            if i in pattern1:
                answer += i

            elif i in pattern2:
                if i == pattern2[0]:
                    answer += pattern2[1]
                else:
                    answer += pattern2[0]

            elif i in pattern3:
                if i == pattern3[0]:
                    answer += pattern3[1]
                else:
                    answer += pattern3[0]

            else:
                answer = 'INVALID'
                break
        
        print(answer)
    else:
        break