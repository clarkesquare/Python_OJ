a, b = map(int, input().split())
a_sum = sum(map(int, input().split()))
b_sum = sum(map(int, input().split()))

print(abs(a_sum - b_sum))