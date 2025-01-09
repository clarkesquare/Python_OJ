numbers = {'xxxxxx...xx...xx...xx...xx...xxxxxx' : '0',
           '....x....x....x....x....x....x....x' : '1',
           'xxxxx....x....xxxxxxx....x....xxxxx' : '2',
           'xxxxx....x....xxxxxx....x....xxxxxx' : '3',
           'x...xx...xx...xxxxxx....x....x....x' : '4',
           'xxxxxx....x....xxxxx....x....xxxxxx' : '5',
           'xxxxxx....x....xxxxxx...xx...xxxxxx' : '6',
           'xxxxx....x....x....x....x....x....x' : '7',
           'xxxxxx...xx...xxxxxxx...xx...xxxxxx' : '8',
           'xxxxxx...xx...xxxxxx....x....xxxxxx' : '9',
           '.......x....x..xxxxx..x....x.......' : '+'
           }

numbers_pattern = {}
for k, v in numbers.items():
    numbers_pattern[v] = k

tmp = ''
tmp_number = ''
check = []
answer = 0
answer_pattern = [''] * 7

# 패턴 입력
pattern = []
for _ in range(7):
    pattern.append('.' + input())

for i in range(1, len(pattern[0]), 6):
    tmp = ''
    for j in range(7):
        tmp += pattern[j][i:i+5]
    
    if numbers[tmp] == '+':
        check.append(tmp_number)
        tmp_number = ''
        
    else:
        tmp_number += numbers[tmp]
    
if len(tmp_number) != 0:
    check.append(tmp_number)

# 답 합산 및 문자로 바꾸기
for i in check:
    answer += int(i)

answer = str(answer)
for i in range(len(answer)):
    for j in range(7):
        answer_pattern[j] += numbers_pattern[answer[i]][(j*5):(j*5)+5]
        if i != len(answer)-1:
            answer_pattern[j] += '.'

print(*answer_pattern, sep='\n')