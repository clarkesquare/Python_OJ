for _ in range(int(input())):
    n, m, word = input().split()
    n, m = int(n), int(m)

    for _ in range(m):
        word = word[n:] + word
    
    print(word)