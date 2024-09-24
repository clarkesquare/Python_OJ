for _ in range(int(input())):
    n = int(input())
    word = input().split()
    tmp = word[0]
    for i in word[1:]:
        if i <= tmp[0]:
            tmp = i + tmp
        
        else:
            tmp += i
    
    print(tmp)