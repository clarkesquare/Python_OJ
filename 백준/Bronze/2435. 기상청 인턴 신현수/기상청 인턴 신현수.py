n, k = map(int, input().split())

temp_list = list(map(int, input().split()))
highest = []

for i in range(n-k+1):
    highest.append(sum(temp_list[i:i+k]))

print(max(highest))
