import copy

word = input()

answer = copy.deepcopy(word)
for i in range(1, len(word)-1):
    for j in range(i+1, len(word)):
        if word[:i][::-1] + word[i:j][::-1] + word[j:][::-1] < answer:
            answer = word[:i][::-1] + word[i:j][::-1] + word[j:][::-1]

print(answer)