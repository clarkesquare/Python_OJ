import sys

input = sys.stdin.readline

n, m = map(int, input().split())
pokedex = {}
pokedex_number = {}

for i in range(1, n+1):
    pokedex[input().strip()] = i

pokedex_number = dict(map(reversed, pokedex.items()))

for _ in range(m):
    tmp = input().strip()
    if tmp.isnumeric():
        print(pokedex_number[int(tmp)])
    
    else:
        print(pokedex[tmp])