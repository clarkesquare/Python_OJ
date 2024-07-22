n, m = map(int, input().split())

words = []
money = []
pattern = []
tmp = ""
answer = 0
salary = []

for _ in range(n):
    a, b = input().split()
    words.append(a)
    money.append(int(b))

for _ in range(m):
    pattern = []
    answer = 0
    while True:
        tmp = input()
        if tmp != ".":
            pattern += list(tmp.split())
        
        else:
            break
    
    for i in pattern:
        if i in words:
            answer += money[words.index(i)]
    
    print(answer)