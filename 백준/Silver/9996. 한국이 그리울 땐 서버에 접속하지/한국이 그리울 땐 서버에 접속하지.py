n = (int(input()))

a, b = input().split("*")
word = ""

for _ in range(n):
    word = input()
    if word[:len(a)] == a and word[len(a):][len(b)*-1:] == b:
        print("DA")
    
    else:
        print("NE")