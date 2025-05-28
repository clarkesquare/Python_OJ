money = input()
answer = 0

while True:
    if len(str(int(money) * 2)) <= len(money):
        answer += 1
        money = str(int(money) * 2)
    
    else:
        break

print(answer)