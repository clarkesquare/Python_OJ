import sys

input = sys.stdin.readline

bowlings = {}
answer = []

for _ in range(int(input())):
    numbers = list(map(int, input().split()))
    if numbers[0] == 1: # 볼링공 넣기
        bowlings[numbers[2]] = numbers[1]

    else: # 볼링공 빼기
        answer.append(bowlings[numbers[1]])

print(*answer, sep="\n")