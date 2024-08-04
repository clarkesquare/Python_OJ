import sys

input = sys.stdin.readline

chats = {}
tmp = ""
answer = 0

for _ in range(int(input())):
    tmp = input().strip()
    if tmp == "ENTER":
        answer += len(chats)
        chats = {}
    
    else:
        if tmp not in chats:
            chats[tmp] = ""

answer += len(chats)

print(answer)