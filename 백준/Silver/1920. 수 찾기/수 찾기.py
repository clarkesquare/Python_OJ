a = int(input())
before = set(map(int, input().split()))

b = int(input())
after = list(map(int, input().split()))

for i in after:
    print(1 if i in before else 0)