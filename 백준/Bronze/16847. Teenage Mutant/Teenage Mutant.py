main = ""
pattern = []
cnt = 0

for i in range(1, int(input())+1):
    n, m = map(int, input().split())
    main = input()
    cnt = m
    pattern = []
    for _ in range(n):
        pattern.append(input())
    
    for j in range(m):
        for k in pattern:
            if k[j] == main[j]:
                cnt -= 1
                break
    
    print(f"Data Set {i}:")
    print(f"{cnt}/{m}")
    print()