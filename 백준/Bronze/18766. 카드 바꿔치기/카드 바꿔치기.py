case1, case2 = [], []

for _ in range(int(input())):
    n = int(input())
    case1 = list(input().split())
    case2 = list(input().split())
    case1.sort()
    case2.sort()
    print('CHEATER' if case1 != case2 else 'NOT CHEATER')