documents = input()
word = input()
answer = 0

while word in documents:
    answer += 1
    documents = documents.replace(word, '1', 1)

print(answer)