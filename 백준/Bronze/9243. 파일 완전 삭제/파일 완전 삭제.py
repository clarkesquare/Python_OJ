n = int(input())
word1 = input()
word2 = input()
delete, delete_fail = 'Deletion succeeded', 'Deletion failed'

if n % 2 == 0:
    if word1 == word2:
        print(delete)
    else:
        print(delete_fail)
else:
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            print(delete_fail)
            break
    else:
        print(delete)