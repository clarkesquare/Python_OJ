from string import ascii_uppercase
alphabets = list(ascii_uppercase) + ["_", "."]

word = ""
answer = ""

while True:
    word = list(input().split())
    if word != ["0"]:
        word[0], word[1] = int(word[0]), word[1][::-1]
        answer = ""
        for i in word[1]:
            answer += alphabets[(alphabets.index(i)+word[0]) % 28]
        
        print(answer)
    else:
        break