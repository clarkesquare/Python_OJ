n = 0
m = 0
a_temp = []
b_temp = []

for _ in range(int(input())):
    a, b = input().split()
    a_temp, b_temp = list(a), list(b)
    n = 0
    m = 0
    #같은 위치 확인
    for i in range(4):
        if a_temp[i] == b_temp[i]:
            a_temp[i], b_temp[i] = "*", "*"
            n += 1

    # 다른 위치 확인, 이 때 같은 위치 것은 제외하고 검사해야 함 + 검사한 것은 제외?
    for j in range(4):
        for k in range(4):
            if a_temp[j] == b_temp[k] and a_temp[j] != "*":
                a_temp[j], b_temp[k] = "*", "*"
                m += 1

    print(f"For secret = {a} and guess = {b}, {str(n)} circles and {str(m)} squares will light up.")