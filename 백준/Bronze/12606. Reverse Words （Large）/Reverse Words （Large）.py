word = []

for i in range(1, int(input())+1):
    word = list(input().split())
    print(f'Case #{i}:', ' '.join(word[::-1]))