chips = ['B', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'V', 'Z']
chips_number = [1, 2, 1, 1, 1, 1, 2, 1, 1, 1]
temp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
answer = 0

n = int(input())
word = input()
for i in word:
    if i in chips:
        temp[chips.index(i)] += 1

while temp[0] >= chips_number[0] and temp[1] >= chips_number[1] and temp[2] >= chips_number[2] and temp[3] >= chips_number[3] and temp[4] >= chips_number[4] and temp[5] >= chips_number[5] and temp[6] >= chips_number[6] and temp[7] >= chips_number[7] and temp[8] >= chips_number[8] and temp[9] >= chips_number[9]:
    answer += 1
    for i in range(10):
        temp[i] -= chips_number[i]

print(answer)