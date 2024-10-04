import sys

input = sys.stdin.readline

a, b, c = input().strip("\n").split()
pattern = {"gender": b, "age": int(c)}
answer = []

for _ in range(int(input())):
    a, b, c = input().strip("\n").split()
    if b == pattern["gender"]:
        if pattern["age"] >= int(c):
            answer.append(a)
    
    else:
        if pattern["gender"] == "MF" or pattern["gender"] == "FM":
            if pattern["age"] >= int(c):
                answer.append(a)

if len(answer) != 0:
    answer.sort()
    print(*answer, sep="\n")

else:
    print("No one yet")