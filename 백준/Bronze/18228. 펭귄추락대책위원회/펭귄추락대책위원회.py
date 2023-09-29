n = int(input())
ice = list(map(int, input().split()))

print(min(ice[:ice.index(-1):]) + min(ice[ice.index(-1)+1::]))