n = int(input())

pattern = {"B": 0, "S": 0, "A": 0}

for i in input():
    pattern[i] += 1

pattern = list(pattern.items())
pattern.sort(key= lambda x:x[1], reverse= True)

if pattern[0][1] == pattern[1][1]:
    if pattern[1][1] == pattern[2][1]:
        print("SCU")
    
    else:
        print(f"{pattern[0][0]}{pattern[1][0]}")

else:
    print(pattern[0][0])