while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    
    else:
        numbers = [a, b]
        answer = [0, 0, 0]
        chk_a = {a: None}
        chk_b = {b: None}
        while a != 1:
            if a % 2 == 0:
                a //= 2
            
            else:
                a = a * 3 + 1
            
            chk_a[a] = None
        
        while b != 1:
            if b % 2 == 0:
                b //= 2
            
            else:
                b = b * 3 + 1
            
            chk_b[b] = None
        
        for i in chk_b:
            if i in chk_a:
                if answer[-1] == 0:
                    answer[-1] = i
                
                del chk_a[i]
            
            else:
                answer[1] += 1
        
        answer[0] = len(chk_a)

        print(f"{numbers[0]} needs {answer[0]} steps, {numbers[1]} needs {answer[1]} steps, they meet at {answer[2]}")