# e = 짝수 / o = 홀수

while True:
    pattern = input()
    cnt = 0
    if pattern != '#':
        cnt = pattern.count('1')
        if pattern[-1] == 'e':
            if cnt % 2 == 0:
                print(pattern[:-1] + '0')
            
            else:
                print(pattern[:-1] + '1')
        
        else:
            if cnt % 2 == 0:
                print(pattern[:-1] + '1')
            
            else:
                print(pattern[:-1] + '0')
    
    else:
        break