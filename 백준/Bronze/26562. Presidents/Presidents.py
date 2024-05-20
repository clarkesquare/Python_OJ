presidents = ["Franklin", "Grant", "Jackson", "Hamilton", "Lincoln", "Washington"]
values = [100, 50, 20, 10, 5, 1]
money = []
answer = 0

for _ in range(int(input())):
    money = list(input().split())
    answer = 0
    for i in money:
        answer += values[presidents.index(i)]
    
    print(f"${answer}")