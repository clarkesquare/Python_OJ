vowels = ['a', 'e', 'i', 'o', 'u']
word = ''
answer = 0

for _ in range(int(input())):
    word = input()
    answer = 0
    for i in word:
        if i in vowels:
            answer += 1
    
    print(f"The number of vowels in {word} is {answer}.")