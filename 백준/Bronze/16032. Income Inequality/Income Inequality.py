n = 0
people = []
avr = 0
answer = 0

while True:
    n = int(input())
    if n != 0:
        answer = 0
        people = list(map(int, input().split()))
        avr = sum(people) / len(people)
        for i in people:
            if i <= avr:
                answer += 1
            
        print(answer)
    
    else:
        break