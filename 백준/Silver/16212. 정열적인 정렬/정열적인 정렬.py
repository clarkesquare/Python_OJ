n = int(input())
array = list(map(int, input().split()))

array.sort()
print(*array)