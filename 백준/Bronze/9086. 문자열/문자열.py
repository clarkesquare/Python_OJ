n = int(input())

for _ in range(n):
    word = input()
    print(word[0] + word[-1], sep='')