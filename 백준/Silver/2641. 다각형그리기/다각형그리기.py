n = int(input())
pattern = ''.join(input().split())
tmp = ''
check = {}
answer = []
cnt = 0

# 비교 셋팅
for i in range(4):
    tmp = ''
    for j in range(n):
        if int(pattern[j]) + i >= 5:
            tmp += str((int(pattern[j]) + i) % 4)
        
        else:
            tmp += str(int(pattern[j]) + i)
    
    check[tmp] = ''
    check[tmp[::-1]] = '' # 뒤집는 패턴도 고려해야 함

# 입력한 패턴 하나씩 돌려가며 검사
for _ in range(int(input())):
    tmp_original = input().split()
    tmp = ''
    tmp = ''.join(tmp_original)
    for i in range(n):
        if tmp in check:
            cnt += 1
            answer.append(tmp_original)
            break

        else:
            tmp = tmp[-1] + tmp[:-1]

# 최종 결과 출력력
print(cnt)
for i in answer:
    print(*i)