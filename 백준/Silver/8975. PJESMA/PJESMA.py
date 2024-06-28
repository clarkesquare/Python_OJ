lyrics = []
tmp = []
answer = 0
test = ""

for _ in range(int(input())):
    lyrics.append(input())

for i in range(1, int(input())+1):
    test = input()
    if test in lyrics and test not in tmp:
        tmp.append(test)
    
    if ((len(tmp) > ( len(lyrics) // 2 )) if (len(lyrics) % 2 == 1) else (len(tmp) >= ( len(lyrics) // 2 ))) and answer == 0:
        answer = i

print(answer)