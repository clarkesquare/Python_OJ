n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
S = 0

A.sort(reverse=True)
for i in range(len(A)):
    if A[i] == 0:
        S += A[i] * max(B)
        B.remove(max(B))
    else:
        S += A[i] * min(B)
        B.remove(min(B))

print(S)