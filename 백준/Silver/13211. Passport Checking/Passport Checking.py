import sys

input = sys.stdin.readline

passports = {}
name = ""
answer = 0

for _ in range(int(input())):
    name = input().strip()
    passports[name] = ""

for _ in range(int(input())):
    name = input().strip()
    if name in passports:
        answer += 1

print(answer)