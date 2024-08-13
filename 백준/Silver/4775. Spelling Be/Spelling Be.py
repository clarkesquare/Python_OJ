import sys

input = sys.stdin.readline
dictionary = {}
answer = []

for _ in range(int(input())):
    dictionary[input().strip()] = ""

for i in range(1, int(input()) + 1):
    answer = []
    while True:
        word = input().strip()
        if word != "-1":
            if word not in dictionary:
                answer.append(word)

        else:
            break
    
    if len(answer) == 0:
        print(f"Email {i} is spelled correctly.")
    
    else:
        print(f"Email {i} is not spelled correctly.")
        print(*answer, sep="\n")

print("End of Output")