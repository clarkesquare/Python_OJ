answer = []

for _ in range(int(input())):
    a, b = input().split()
    answer = []
    for _ in range(int(b)):
        words = list(input().split())
        if len(words) == len(a):
            for i in range(len(a)):
                if words[i][0] != a[i]:
                    break

            else:
                answer.append(words)
    
    print(a)
    for j in answer:
        print(*j)