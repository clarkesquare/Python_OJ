n = int(input())
magnets = input()
answer = 'Yes'

for i in range(1, len(magnets)):
    if magnets[i] == magnets[i-1]:
        answer = 'No'
        break

print(answer)