pattern_a = ["***", "*.*", "***", "*.*", "*.*"]
pattern_b = ["***", "*.*", "***", "*.*", "***"]
pattern_c = ["***", "*..", "*..", "*..", "***"]
pattern_d = ["***", "*.*", "*.*", "*.*", "***"]
pattern_e = ["***", "*..", "***", "*..", "***"]
answer = ["", "", "", "", ""]
temp = []

n = int(input())
word = input()

for i in word:
    if i == "A":
        temp = pattern_a
    elif i == "B":
        temp = pattern_b
    elif i == "C":
        temp = pattern_c
    elif i == "D":
        temp = pattern_d
    elif i == "E":
        temp = pattern_e
    
    for j in range(5):
        answer[j] += temp[j]

print("\n".join(answer))