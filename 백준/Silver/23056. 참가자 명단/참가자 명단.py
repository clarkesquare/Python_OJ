n, m = map(int, input().split())
answer_even = {}
answer_odd = {}

while True:
    a, b = input().split()
    if a != '0' and b != '0':
        a = int(a)
        if a % 2 == 1:
            if a not in answer_odd:
                answer_odd[a] = [b]
            
            else:
                if len(answer_odd[a]) < m:
                    answer_odd[a].append(b)
        
        else:
            if a not in answer_even:
                answer_even[a] = [b]
            
            else:
                if len(answer_even[a]) < m:
                    answer_even[a].append(b)
    
    else:
        break

for k, v in sorted(answer_odd.items()):
    v = sorted(v)
    v = sorted(v, key=len)
    for i in v:
        print(k, i)

for k, v in sorted(answer_even.items()):
    v = sorted(v)
    v = sorted(v, key=len)
    for i in v:
        print(k, i)