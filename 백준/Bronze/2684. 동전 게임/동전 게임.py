pattern = ['TTT', 'TTH', 'THT', 'THH', 'HTT', 'HTH', 'HHT', 'HHH']
answer = [0] * 8

for _ in range(int(input())):
    test_case = input()
    answer = [0] * 8
    for i in range(38):
        answer[pattern.index(test_case[i:i+3])] = answer[pattern.index(test_case[i:i+3])] + 1
    
    print(*answer)