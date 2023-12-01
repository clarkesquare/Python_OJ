seats = []
participant = 0
answer = 0

for _ in range(int(input())):
    n, m = map(int, input().split())
    seats = []
    participant, answer = 0, 0
    for _ in range(n):
        participant = int(input())
        if participant not in seats:
            seats.append(participant)
        else:
            answer += 1
    
    print(answer)