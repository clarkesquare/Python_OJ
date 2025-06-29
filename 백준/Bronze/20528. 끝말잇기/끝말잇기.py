n = int(input())
word = input().split()

for i in range(n-1):
    if word[i][-1] != word[i+1][0]:
        print(0)
        break

else:
    print(1)