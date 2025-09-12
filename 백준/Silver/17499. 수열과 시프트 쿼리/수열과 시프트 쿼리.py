import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
sft = 0  # 논리적 a1의 물리 인덱스

for _ in range(m):
    tmp = list(map(int, input().split()))
    t = tmp[0]

    if t == 1:
        i, x = tmp[1], tmp[2]
        idx = (sft + i - 1) % n   # ★ 물리 인덱스 보정
        numbers[idx] += x

    elif t == 2:  # 오른쪽 s
        s = tmp[1] % n            # ★ s 자체도 줄여두면 안정적
        sft = (sft - s) % n

    else:         # 왼쪽 s
        s = tmp[1] % n
        sft = (sft + s) % n

# 현재 상태를 논리 순서로 출력
print(*(numbers[sft:] + numbers[:sft]))