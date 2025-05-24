cnt = 0

while True:
    n = int(input())
    if n != 0:
        cnt += 1
        answer = 0
        tmp = 0
        numbers = list(map(int, input().split()))
        tmp = sum(numbers) // n
        for i in numbers:
            if i > tmp:
                answer += (i - tmp)
        
        print(f'Set #{cnt}')
        print(f'The minimum number of moves is {answer}.')
        print()
    
    else:
        break