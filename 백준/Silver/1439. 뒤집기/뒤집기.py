answer = [0, 0]
pattern = input()
tmp = pattern[0]

for i in pattern[1:]:
    if tmp != i:
        answer[int(tmp)] += 1
        tmp = i

if i == "0":
    answer[0] += 1

else:
    answer[1] += 1

print(min(answer))