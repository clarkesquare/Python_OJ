from string import ascii_lowercase
pattern = {}

for cnt in range(1, int(input())+1):
    for i in ascii_lowercase:
        pattern[i] = 0 

    word = input().lower()
    min = 3
    for j in word:
        if j.islower():
            pattern[j] += 1
    
    print(f"Case {cnt}: ", end="")
    for k in pattern:
        if pattern[k] < min:
            min = pattern[k]
    
    if min == 0:
        print("Not a pangram")
    
    elif min == 1:
        print("Pangram!")
    
    elif min == 2:
        print("Double pangram!!")
    
    else:
        print("Triple pangram!!!")