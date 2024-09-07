n = int(input())
answer = ["G...", ".I.T", "..S."]
tmp = ""

for i in answer:
    for _ in range(n):
        tmp = ""
        for j in i:
            tmp += j * n
    
        print(tmp)