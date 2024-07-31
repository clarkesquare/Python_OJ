tmp = []
answer = []
book = ""

for _ in range(int(input())):
    book = input()
    if book != "READ":
        tmp.append(book)
    
    else:
        answer.append(tmp.pop(-1))

print(*answer, end="\n")