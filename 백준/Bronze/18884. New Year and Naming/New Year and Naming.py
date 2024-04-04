n, m = map(int, input().split())
sipgan = input().split()
ganji = input().split()
number = 0

for _ in range(int(input())):
    number = int(input())
    print(sipgan[(number - 1) % n] + ganji[(number - 1) % m])