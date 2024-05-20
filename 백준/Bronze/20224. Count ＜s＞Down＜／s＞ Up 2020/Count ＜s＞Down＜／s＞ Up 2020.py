olympic = "2020"
answer = 0

while True:
    n = int(input())
    if n != 0:
        answer = 0
        numbers = list(input().split())
        numbers = "".join(numbers)
        for i in range(len(numbers[:-3])):
            if numbers[i] == "2":
                if numbers[i:i+4:] == "2020":
                    answer += 1

        print(answer)
    else:
        break