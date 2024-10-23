pattern = ["..#..", ".#.#.", "#.@.#", ".#.#.", "..#.."]
peterpan_frame = [".#..", "#.#.", ".@.#", "#.#.", ".#.."]
wendy_frame = [".*..", "*.*.", ".@.*", "*.*.", ".*.."]
word = input()

pattern[2] = pattern[2].replace("@", word[0])
for i in range(1, len(word)):
    for j in range(5):
        if (i + 1) % 3 != 0:
            pattern[j] += peterpan_frame[j]
        
        else:
            if j == 2:
                pattern[j] = pattern[j][:-1] + "*" + wendy_frame[j]
            
            else:
                pattern[j] += wendy_frame[j]

        if j == 2:
            pattern[j] = pattern[j].replace("@", word[i])

print(*pattern, sep="\n")