dance = {"ChongChong": ""}

for _ in range(int(input())):
    a, b = input().split()
    if a in dance or b in dance:
        if a not in dance:
            dance[a] = ""
        
        elif b not in dance:
            dance[b] = ""

print(len(dance))