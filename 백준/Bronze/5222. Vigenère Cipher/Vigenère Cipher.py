from string import ascii_uppercase

alphabets = list(ascii_uppercase)
pattern = []

for _ in range(int(input())):
    a, b = input().split()
    answer = ""
    pattern = []
    for i in a:
        pattern.append(alphabets.index(i))
    
    cnt = -1
    for j in b:
        cnt = (cnt + 1) % len(pattern)
        answer += alphabets[(alphabets.index(j) + pattern[cnt]) % 26]
    
    print(f"Ciphertext: {answer}")