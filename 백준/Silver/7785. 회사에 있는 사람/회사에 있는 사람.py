import sys

input = sys.stdin.readline
members = {}

for _ in range(int(input())):
    a, b = input().split()
    if b == "enter":
        members[a] = ""
    else:
        del members[a]

answer = list(members.items())
answer.sort(key= lambda x:x[0], reverse=True)

for i in answer:
    print(i[0])