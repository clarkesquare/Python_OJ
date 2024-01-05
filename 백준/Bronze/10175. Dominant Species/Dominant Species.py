name = ['Coyote', 'Bobcat', 'Wolf', 'Mountain Lion']
animals = ['C', 'B', 'W', 'M']
scores = [1, 2, 3, 4]
answer = [0, 0, 0, 0]

for _ in range(int(input())):
    n, m = input().split()
    answer = [0, 0, 0, 0]
    for i in m:
        answer[animals.index(i)] += scores[animals.index(i)]
    
    if answer.count(max(answer)) >= 2:
        print(f'{n}: There is no dominant species')
    else:
        print(f'{n}: The {name[answer.index(max(answer))]} is the dominant species')