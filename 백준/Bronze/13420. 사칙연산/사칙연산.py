calculate = []
result = 0

for _ in range(int(input())):
    calculate = list(input().split())
    calculate[0], calculate[2], calculate[4] = int(calculate[0]), int(calculate[2]), int(calculate[4])
    result = 0
    
    if calculate[1] == '+':
        result = calculate[0] + calculate[2]
    elif calculate[1] == '-':
        result = calculate[0] - calculate[2]
    elif calculate[1] == '*':
        result = calculate[0] * calculate[2]
    else:
        result = int(calculate[0] / calculate[2])
    
    print('correct' if result == calculate[4] else 'wrong answer')