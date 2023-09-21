for _ in range(int(input())):
    answer = ''
    name = list(input().split(' '))
    name[0] = 'god'
    for i in name:
        answer += i
        
    print(answer)