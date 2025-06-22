n, k = map(int, input().split())
coexist = {}
numbers = {k: None}
tmp = {}
answer = 0
cnt = 0

if n != k:
    while True:
        cnt += 1
        tmp = {}
        for i in numbers:
            if i / 2 == i // 2: # 반절 나눠도 됨
                if i // 2 == n:
                    answer = 1
                    break

                else:
                    if i // 2 not in coexist:
                        coexist[i//2] = None
                        tmp[i//2] = None
            
            if i + 1 == n:
                answer = 1
                break

            else:
                if (i + 1) not in coexist:
                    coexist[i+1] = None
                    tmp[i+1] = None
            
            if i - 1 == n:
                answer = 1
                break

            else:
                if (i - 1) not in coexist and i - 1 >= 0:
                    coexist[i-1] = None
                    tmp[i-1] = None

        if answer != 0:
            break
        
        numbers = tmp

print(cnt)