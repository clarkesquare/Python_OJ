import sys

input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n != 0 and m != 0:
        cd = {}
        tmp = ""
        answer = 0

        for _ in range(n):
            tmp = input().strip()
            cd[tmp] = ""

        for _ in range(m):
            tmp = input().strip()
            if tmp in cd:
                answer += 1

        print(answer)
    
    else:
        break