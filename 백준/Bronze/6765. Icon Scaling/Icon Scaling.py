pattern = ["*x*", " xx", "* *"]

n = int(input())
temp = ""

for j in pattern:
    temp = ""
    for k in j:
        temp += k * n
    
    for _ in range(n):
        print(temp)