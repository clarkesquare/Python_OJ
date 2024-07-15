import sys

input = sys.stdin.readline
send = []
tmp = ""
answer = 0

for _ in range(int(input())):
    send.append(input())

for _ in range(int(input())):
    tmp = input()
    if tmp in send:
        answer += 1

print(answer)