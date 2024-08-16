import sys

input = sys.stdin.readline

candidates = {}

while True:
    word = input().strip()
    if word != "***":
        if word not in candidates:
            candidates[word] = 1
        
        else:
            candidates[word] += 1

    else:
        break

candidates = list(candidates.items())
candidates.sort(key= lambda x:x[1], reverse=True)

if candidates[0][1] != candidates[1][1]:
    print(candidates[0][0])

else:
    print("Runoff!")