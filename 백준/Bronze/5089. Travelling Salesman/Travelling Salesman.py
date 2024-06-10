i = 0
while True:
    n = int(input())
    if n != 0:
        i += 1
        visit = []
        for _ in range(n):
            word = input()
            if word not in visit:
                visit.append(word)
        

        print(f"Week {i} {len(visit)}")
    
    else:
        break