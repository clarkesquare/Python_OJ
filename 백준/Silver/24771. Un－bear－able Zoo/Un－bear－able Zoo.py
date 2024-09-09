cnt = 0

while True:
    pattern = {}
    answer = []
    n = int(input())
    cnt += 1
    if n != 0:
        for _ in range(n):
            word = input().lower().split()
            tmp = word[-1]
            if tmp not in pattern:
                pattern[tmp] = 1
            
            else:
                pattern[tmp] += 1
        
        for k, v in pattern.items():
            answer.append([k, v])
        
        answer.sort(key= lambda x:x[0])
        print(f"List {cnt}:")
        for i in answer:
            print(i[0], "|", i[1])
        
    else:
        break