a, b = input().split("*")
answer = [0, 0]

while "()" in a:
    a = a.replace("()","")

while "()" in b:
    b = b.replace("()","")

answer = [a.count("("), b.count(")")]

print(min(answer))