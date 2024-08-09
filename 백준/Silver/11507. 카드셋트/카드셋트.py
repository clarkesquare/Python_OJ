cards = {"P": 13, "K": 13, "H": 13, "T": 13}
greska = []
tmp = ""
answer = ""

pattern = input()
for i in range(0, len(pattern), 3):
    tmp = pattern[i:i+3]
    if tmp not in greska:
        cards[tmp[0]] -= 1
        greska.append(tmp)
    
    else:
        answer = "GRESKA"
        break

if len(answer) == 0:
    answer = list(cards.items())
    for i in answer:
        print(i[1], end=" ")

else:
    print(answer)