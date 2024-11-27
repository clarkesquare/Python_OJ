import sys

input = sys.stdin.readline
tmp = ""
email = []

for _ in range(int(input())):
    a, b = input().strip("\n").split("@")
    tmp = ""
    for i in a:
        if i.isalpha():
            tmp += i
        
        elif i == "+":
            break
    
    a = tmp
    if [a, b] not in email:
        email.append([a, b])

print(len(email))