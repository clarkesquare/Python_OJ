word = ''
answer = 0
end = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v']

n = int(input())
word = input()

if word[-1] in end:
    answer = 1

print(answer)